"""
Evaluasi Test Set - Domain Adaptation (Tahap 1)
Jalankan file ini SETELAH colab_domain_adaptation.py selesai.
Tidak ada training ulang — hanya load adapter dan evaluasi test set.

CLI:
  !python notebooks/colab_domain_eval.py
  !python notebooks/colab_domain_eval.py --adapter_path "/content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter"
"""
import os
import sys
import argparse

sys.path.append(os.getcwd())

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--adapter_path", type=str,
                        default="/content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter",
                        help="Path adapter hasil Tahap 1")
    parser.add_argument("--dataset_path", type=str,
                        default="./dataset_aqg/output_domain/accumulated.jsonl")
    if 'ipykernel' in sys.modules or 'google.colab' in sys.modules:
        return parser.parse_args(args=[])
    return parser.parse_args()

args = parse_args()

# --- Load dataset (split 80/10/10 dengan seed=42 yang sama) ---
from src.finetuning.domain_loader import get_domain_dataset
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
from peft import PeftModel

print(f"Loading dataset dari: {args.dataset_path}")
dataset_dict, tokenizer = get_domain_dataset(args.dataset_path)
test_dataset = dataset_dict['test']
print(f"Test set: {len(test_dataset)} sampel")

# --- Load base model + adapter ---
print(f"\nMemuat adapter dari: {args.adapter_path}")
base_model = AutoModelForSeq2SeqLM.from_pretrained("Wikidepia/IndoT5-base")
model = PeftModel.from_pretrained(base_model, args.adapter_path)
model.eval()
print("Model siap.")

# --- Evaluasi ---
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)

eval_args = Seq2SeqTrainingArguments(
    output_dir="/tmp/eval_only",
    per_device_eval_batch_size=4,
    predict_with_generate=False,
    fp16=False,
    report_to="none",
)

trainer = Seq2SeqTrainer(
    model=model,
    args=eval_args,
    processing_class=tokenizer,
    data_collator=data_collator,
)

print("\nMengevaluasi test set...")
results = trainer.evaluate(eval_dataset=test_dataset)

print("\n===== HASIL EVALUASI TEST SET =====")
for k, v in results.items():
    print(f"  {k}: {v:.4f}" if isinstance(v, float) else f"  {k}: {v}")
print("====================================")
