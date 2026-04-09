# %% [markdown]
# ## 1. Setup Environment & Detect Colab
# Script ini akan otomatis mendeteksi jika dijalankan di Google Colab dan menginstal library yang diperlukan.

# %%
import os
import sys

# Deteksi apakah berjalan di Google Colab
IN_COLAB = 'google.colab' in sys.modules

if IN_COLAB:
    print("Detected Google Colab environment. Installing dependencies...")
    # Update pip dan install dependensi utama
    os.system("pip install -q transformers peft datasets accelerate bitsandbytes evaluate rouge-score sentencepiece")
    
    # Mount Google Drive untuk persistensi model/checkpoints
    from google.colab import drive
    drive.mount('/content/drive')
    
    # Root direktori project di Colab (biasanya di /content/AQG jika dikloning)
    # Sesuaikan dengan nama repo Anda jika berbeda
    PROJECT_NAME = "AQG" 
    project_root = f"/content/{PROJECT_NAME}"
    
    if os.path.exists(project_root):
        os.chdir(project_root)
        if project_root not in sys.path:
            sys.path.append(project_root)
    else:
        print(f"WARNING: Project root {project_root} not found. Please ensure you cloned the repo correctly.")
else:
    print("Detected Local environment.")
    # Konfigurasi path untuk local
    try:
        notebook_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(notebook_dir, '..'))
    except NameError:
        if os.path.basename(os.getcwd()) == 'notebooks':
            project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
        else:
            project_root = os.getcwd()

    if project_root not in sys.path:
        sys.path.append(project_root)
    
    os.chdir(project_root)

print("Current Working Directory:", os.getcwd())

# Konfigurasi path sistem sudah ditangani di blok Setup Environment di atas.

# %% [markdown]
# ## 4. Load Dataset
# Menggunakan modul custom data loader yang di sediakan di src/finetuning
# %%
from src.finetuning.data_loader import load_aqg_dataset

# Path dataset di Colab biasanya ada di dalam repo
# Jika dataset di-upload ke Drive, ubah path ke '/content/drive/MyDrive/path_to_dataset'
DATASET_PATH = './dataset_aqg/dataset-task-spesifc'

if IN_COLAB and not os.path.exists(DATASET_PATH):
    print(f"Dataset not found at {DATASET_PATH}. Checking in Google Drive...")
    # Contoh jika ditaruh di Drive:
    DATASET_PATH = '/content/drive/MyDrive/AQG_Dataset/dataset-task-spesifc'

print(f"Loading dataset from: {DATASET_PATH}")
dataset, tokenizer = load_aqg_dataset(DATASET_PATH)

print(f"Dataset loaded: {len(dataset['train'])} train samples")
print(f"Dataset validation: {len(dataset['validation'])} samples")

# %% [markdown]
# ## 5. Setup LoRA Model
# Inisialisasi model referensi IndoT5 beserta LoRA adapter-nya menggunakan modul src/finetuning
# %%
from src.finetuning.model_setup import setup_model_with_lora

model = setup_model_with_lora(
    model_name="Wikidepia/IndoT5-base",
    lora_r=8,
    lora_alpha=16,
    lora_dropout=0.1
)

# %% [markdown]
# ## 6. Training Configuration (Konfigurasi Trainer)
# %%
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq

# Tentukan direktori checkpoint
# Jika di Colab, simpan ke Google Drive agar tidak hilang jika session terputus
if IN_COLAB:
    OUTPUT_DIR = "/content/drive/MyDrive/aqg_checkpoints"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
else:
    OUTPUT_DIR = "./checkpoints"

training_args = Seq2SeqTrainingArguments(
    output_dir=OUTPUT_DIR,
    eval_strategy="epoch",            # Evaluasi dilakukan setiap akhir epoch
    learning_rate=2e-4,               # LR ideal untuk T5 + LoRA
    per_device_train_batch_size=8,    # Kurangi menjadi 4 jika mendapatkan CUDA Out of Memory
    per_device_eval_batch_size=8,
    num_train_epochs=3,               # Sesuaikan epoch yang dibutuhkan (misal: 10 atau 20)
    weight_decay=0.01,
    save_total_limit=3,               # Menyimpan 3 checkpoint terakhir
    predict_with_generate=True,       # Harus TRUE untuk model sequence to sequence 
    fp16=True,                        # Mixed precision training untuk hemat memori VRAM
    logging_steps=50,
    save_strategy="epoch"
)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['validation'],
    processing_class=tokenizer,
    data_collator=data_collator
)

# %% [markdown]
# ## 7. Start Training 🚀
# Jalankan block ini untuk memulai proses pelatihan.
# %%
trainer.train() 

# (Lepas komentar di atas untuk menjalankan fine-tuning)

# %% [markdown]
# ## 8. Menyimpan Hasil & Model (Save Models)
# Simpan model untuk inference dan deploy.
# %%
trainer.save_model("./final_model")

# Jika menggunakan Colab, segera push ke drive atau kompres (Zip) untuk didownload.
# !zip -r final_model.zip ./final_model
# from google.colab import files
# files.download('final_model.zip')
