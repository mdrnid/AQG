"""
Evaluasi Test Set - Domain Adaptation (Tahap 1)
Metrik: Perplexity dan Reconstruction Accuracy (token exact match)
Jalankan SETELAH colab_domain_adaptation.py selesai.

CLI:
  !python notebooks/colab_domain_eval.py
  !python notebooks/colab_domain_eval.py --adapter_path "/content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter"
"""
import os
import sys
import math
import argparse
import numpy as np

sys.path.append(os.getcwd())

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--adapter_path", type=str,
                        default="/content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter")
    parser.add_argument("--dataset_path", type=str,
                        default="./dataset_aqg/output_domain/accumulated.jsonl")
    if 'ipykernel' in sys.modules or 'google.colab' in sys.modules:
        return parser.parse_args(args=[])
    return parser.parse_args()

args = parse_args()

# --- Load dataset (seed=42 sama → split identik) ---
from src.finetuning.domain_loader import get_domain_dataset
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
from peft import PeftModel

print(f"Loading dataset dari: {args.dataset_path}")
dataset_dict, tokenizer = get_domain_dataset(args.dataset_path)
test_dataset = dataset_dict['test']
print(f"Test set: {len(test_dataset)} sampel\n")

# --- Load base model + adapter ---
print(f"Memuat adapter dari: {args.adapter_path}")
base_model = AutoModelForSeq2SeqLM.from_pretrained("Wikidepia/IndoT5-base")
model = PeftModel.from_pretrained(base_model, args.adapter_path)
model.eval()
print("Model siap.\n")

# --- compute_metrics: Perplexity + Reconstruction Accuracy ---
def compute_metrics(eval_preds):
    predictions, labels = eval_preds

    # Ganti token -100 kembali ke pad_token_id agar bisa di-decode
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)

    # Clip predictions ke rentang valid [0, vocab_size-1]
    # Nilai negatif/overflow bisa muncul dari padding saat generate
    vocab_size = tokenizer.vocab_size
    predictions = np.clip(predictions, 0, vocab_size - 1)

    decoded_preds  = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels,      skip_special_tokens=True)

    # Reconstruction Accuracy (exact string match)
    exact_matches = sum(
        p.strip() == l.strip()
        for p, l in zip(decoded_preds, decoded_labels)
    )
    accuracy = exact_matches / len(decoded_preds) * 100

    return {
        "reconstruction_accuracy (%)": round(accuracy, 2),
    }

# --- Evaluasi ---
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)

eval_args = Seq2SeqTrainingArguments(
    output_dir="/tmp/eval_only",
    per_device_eval_batch_size=4,
    predict_with_generate=True,    # Generate output untuk hitung reconstruction accuracy
    generation_max_length=128,     # Panjang maksimum output yang di-generate
    fp16=False,
    report_to="none",
)

trainer = Seq2SeqTrainer(
    model=model,
    args=eval_args,
    processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

print("Mengevaluasi test set...")
results = trainer.evaluate(eval_dataset=test_dataset)

# Hitung Perplexity dari eval_loss (jika ada)
perplexity = math.exp(results["eval_loss"]) if "eval_loss" in results else None

print("\n===== HASIL EVALUASI TEST SET (Tahap 1) =====")
print(f"  eval_loss               : {results.get('eval_loss', 'N/A'):.4f}")
if perplexity:
    print(f"  Perplexity              : {perplexity:.2f}")
print(f"  Reconstruction Accuracy : {results.get('eval_reconstruction_accuracy (%)', 'N/A'):.2f}%")
print(f"  eval_runtime            : {results.get('eval_runtime', 'N/A'):.2f}s")
print(f"  eval_samples_per_second : {results.get('eval_samples_per_second', 'N/A'):.2f}")
print("=============================================")
