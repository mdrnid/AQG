# %% [markdown]
# # Tahap 1: Domain Adaptation (IndoT5-Python)
# Script ini melatih IndoT5 untuk memahami materi Python menggunakan tugas Span Masking (MLM).

# %%
import os
import sys
import torch
import argparse
from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoTokenizer, 
    Trainer, 
    TrainingArguments
)
from peft import LoraConfig, get_peft_model, TaskType

# Pastikan src terbaca
sys.path.append(os.getcwd())
from src.finetuning.domain_loader import get_domain_dataset

def parse_args():
    parser = argparse.ArgumentParser(description="Domain Adaptation Stage 1")
    parser.add_argument("--dataset_path", type=str, default="./dataset_aqg/output_domain/accumulated.jsonl", help="Path ke file .jsonl domain")
    parser.add_argument("--output_dir", type=str, default=None, help="Path simpan adapter")
    parser.add_argument("--epochs", type=int, default=6, help="Jumlah epoch (default 6)")
    
    if 'ipykernel' in sys.modules or 'google.colab' in sys.modules:
        return parser.parse_args(args=[])
    return parser.parse_args()

args = parse_args()

# %% [markdown]
# ## 1. Environment & GPU Check
# %%
IN_COLAB = 'google.colab' in sys.modules or os.path.exists('/content')

if IN_COLAB:
    print("Detected Colab. Installing dependencies...")
    os.system("pip install -q transformers peft datasets accelerate bitsandbytes")
    if not torch.cuda.is_available():
        print("WARNING: GPU tidak terdeteksi! Training akan sangat lambat.")
    else:
        print(f"Menggunakan GPU: {torch.cuda.get_device_name(0)}")

# %% [markdown]
# ## 2. Load Dataset & Tokenizer
# %%
MODEL_NAME = "Wikidepia/IndoT5-base"

print(f"Loading dataset dari: {args.dataset_path}")
dataset, tokenizer = get_domain_dataset(args.dataset_path, tokenizer_name=MODEL_NAME)

# Gunakan Seq2Seq Collator karena data sudah ter-masking di JSONL
from transformers import DataCollatorForSeq2Seq
data_collator = DataCollatorForSeq2Seq(tokenizer, model=None)

# %% [markdown]
# ## 3. Setup Model with LoRA
# %%
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

lora_config = LoraConfig(
    r=8, 
    lora_alpha=16,
    target_modules=["q", "v"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.SEQ_2_SEQ_LM
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# %% [markdown]
# ## 4. Training Arguments
# %%
if args.output_dir:
    OUTPUT_DIR = args.output_dir
elif IN_COLAB:
    OUTPUT_DIR = "/content/drive/MyDrive/IndoT5-Python-Adapter"
else:
    OUTPUT_DIR = "./output_domain_adaptation"

os.makedirs(OUTPUT_DIR, exist_ok=True)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,     # Total batch = 8
    learning_rate=2e-4,                # Sesuai spesifikasi
    num_train_epochs=args.epochs,
    warmup_ratio=0.1,                  # 10% Warmup steps
    logging_steps=10,
    save_strategy="epoch",
    save_total_limit=2,
    fp16=False, # Dinonaktifkan: T5 sering mengalami NaN loss jika menggunakan fp16
    report_to="none",
    remove_unused_columns=False, # Penting untuk T5 MLM
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer, # Menggunakan processing_class untuk v4.45+
    data_collator=data_collator,
)

# %% [markdown]
# ## 5. Start Training 🚀
# %%
print("Memulai Domain Adaptation (Tahap 1)...")
trainer.train()

# Simpan adapter akhir
final_path = os.path.join(OUTPUT_DIR, "final_adapter")
model.save_pretrained(final_path)
tokenizer.save_pretrained(final_path)
print(f"Selesai! Adapter disimpan di {final_path}")
