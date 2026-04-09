import os
import glob
from datasets import Dataset
from transformers import AutoTokenizer

def load_domain_text(materi_dir):
    """
    Membaca seluruh file .md dari folder materi secara rekursif.
    """
    all_texts = []
    
    # Cari semua file .md di dalam subfolder materi
    md_files = glob.glob(os.path.join(materi_dir, "**/*.md"), recursive=True)
    
    if not md_files:
        print(f"WARNING: Tidak ditemukan file .md di {materi_dir}")
        return []

    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Pembersihan sederhana (opsional: bisa tambahkan pembersihan markdown yang lebih advanced)
            # Di sini kita biarkan agar model paham struktur teks juga
            if content.strip():
                all_texts.append(content)
                
    return all_texts

def get_domain_dataset(materi_dir, tokenizer_name="Wikidepia/IndoT5-base", max_length=512):
    """
    Menghasilkan Hugging Face Dataset yang siap untuk T5 MLM (Span Masking).
    """
    texts = load_domain_text(materi_dir)
    
    # Bungkus dalam format Dataset
    raw_dataset = Dataset.from_dict({"text": texts})
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    def tokenize_function(examples):
        # Kita hanya butuh tokenisasi teks mentah
        # DataCollatorForT5MLM yang akan menangani masking-nya nanti
        return tokenizer(
            examples["text"],
            truncation=True,
            max_length=max_length,
            padding=False # Kita tidak padding di sini agar hemat memori, dilakukan di collator
        )

    tokenized_dataset = raw_dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=["text"],
        desc="Tokenizing domain materials"
    )
    
    return tokenized_dataset, tokenizer
