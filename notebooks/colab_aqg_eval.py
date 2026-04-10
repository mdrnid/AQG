"""
Evaluasi Test Set - Task-Specific AQG (Tahap 2)
Metrik: BLEU-4, ROUGE-L, Distinct-1, Distinct-2
Jalankan SETELAH colab_training.py selesai.

CLI:
  !python notebooks/colab_aqg_eval.py
  !python notebooks/colab_aqg_eval.py --model_path "/content/drive/MyDrive/aqg_checkpoints/final_model"
"""
import os
import sys
import argparse
import numpy as np

sys.path.append(os.getcwd())

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str,
                        default="/content/drive/MyDrive/aqg_checkpoints/final_model",
                        help="Path model hasil Tahap 2")
    parser.add_argument("--dataset_path", type=str,
                        default="./dataset_aqg/dataset-task-spesifc",
                        help="Path folder dataset (berisi train/val/test.jsonl)")
    if 'ipykernel' in sys.modules or 'google.colab' in sys.modules:
        return parser.parse_args(args=[])
    return parser.parse_args()

args = parse_args()

IN_COLAB = 'google.colab' in sys.modules or os.path.exists('/content')
if IN_COLAB:
    os.system("pip install -q evaluate rouge-score sacrebleu")

# --- Load dataset ---
from src.finetuning.data_loader import load_aqg_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments
from peft import PeftModel
import evaluate

print(f"Loading dataset dari: {args.dataset_path}")
dataset, tokenizer = load_aqg_dataset(args.dataset_path)
test_dataset = dataset['test']
print(f"Test set: {len(test_dataset)} sampel\n")

# --- Load model Tahap 2 ---
print(f"Memuat model dari: {args.model_path}")
# Coba load sebagai PeftModel dulu, fallback ke model biasa
try:
    base_model = AutoModelForSeq2SeqLM.from_pretrained("Wikidepia/IndoT5-base")
    model = PeftModel.from_pretrained(base_model, args.model_path)
    print("Loaded as PEFT model.")
except Exception:
    model = AutoModelForSeq2SeqLM.from_pretrained(args.model_path)
    print("Loaded as full model.")
model.eval()
print("Model siap.\n")

# --- Metrik ---
rouge_metric = evaluate.load("rouge")
bleu_metric  = evaluate.load("sacrebleu")

def compute_metrics(eval_preds):
    predictions, labels = eval_preds

    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    predictions = np.clip(predictions, 0, tokenizer.vocab_size - 1)

    decoded_preds  = [p.strip() for p in tokenizer.batch_decode(predictions, skip_special_tokens=True)]
    decoded_labels = [l.strip() for l in tokenizer.batch_decode(labels,      skip_special_tokens=True)]

    # ROUGE-L
    rouge_result = rouge_metric.compute(
        predictions=decoded_preds,
        references=decoded_labels
    )

    # BLEU-4
    bleu_result = bleu_metric.compute(
        predictions=decoded_preds,
        references=[[l] for l in decoded_labels]
    )

    # Diversity: Distinct-1 & Distinct-2
    all_tokens  = [tok for pred in decoded_preds for tok in pred.split()]
    all_bigrams = [(all_tokens[i], all_tokens[i+1]) for i in range(len(all_tokens) - 1)]
    distinct_1  = (len(set(all_tokens))  / len(all_tokens)  * 100) if all_tokens  else 0.0
    distinct_2  = (len(set(all_bigrams)) / len(all_bigrams) * 100) if all_bigrams else 0.0

    # Simpan sample untuk inspeksi
    print("\n--- Sample Prediksi (3 pertama) ---")
    for i in range(min(3, len(decoded_preds))):
        print(f"  [Target]  : {decoded_labels[i][:120]}")
        print(f"  [Prediksi]: {decoded_preds[i][:120]}")
        print()

    return {
        "rouge_l"   : round(rouge_result["rougeL"], 4),
        "bleu_4"    : round(bleu_result["score"], 4),
        "distinct_1": round(distinct_1, 2),
        "distinct_2": round(distinct_2, 2),
    }

# --- Evaluasi ---
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)

eval_args = Seq2SeqTrainingArguments(
    output_dir="/tmp/aqg_eval",
    per_device_eval_batch_size=4,
    predict_with_generate=True,
    generation_max_length=256,
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

print("Mengevaluasi test set (Tahap 2 AQG)...")
results = trainer.evaluate(eval_dataset=test_dataset)

print("\n===== HASIL EVALUASI TEST SET (Tahap 2 AQG) =====")
print(f"  ROUGE-L    : {results.get('eval_rouge_l',    'N/A')}")
print(f"  BLEU-4     : {results.get('eval_bleu_4',     'N/A')}")
print(f"  Distinct-1 : {results.get('eval_distinct_1', 'N/A')}%")
print(f"  Distinct-2 : {results.get('eval_distinct_2', 'N/A')}%")
print(f"  eval_loss  : {results.get('eval_loss',       'N/A'):.4f}")
print(f"  Runtime    : {results.get('eval_runtime',    'N/A'):.2f}s")
print("=================================================")
