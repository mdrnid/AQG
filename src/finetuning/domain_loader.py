import os
import json
from datasets import Dataset
from transformers import AutoTokenizer

def load_domain_jsonl(jsonl_path):
    """
    Membaca data dari file .jsonl (output_domain/accumulated.jsonl)
    Format: {"input": "...", "target": "...", "metadata": {...}}
    """
    data = []
    if not os.path.exists(jsonl_path):
        print(f"ERROR: File tidak ditemukan di {jsonl_path}")
        return []

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
            
    return data

def get_domain_dataset(jsonl_path, tokenizer_name="Wikidepia/IndoT5-base", max_length=512):
    """
    Menghasilkan Dataset dari accumulated.jsonl untuk Domain Adaptation.
    """
    raw_data = load_domain_jsonl(jsonl_path)
    
    if not raw_data:
        raise ValueError(f"Dataset kosong! Periksa apakah file ada di: {jsonl_path}")

    # Bungkus dalam format Dataset
    raw_dataset = Dataset.from_list(raw_data)
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    def tokenize_function(examples):
        # Tokenisasi input dan target sekaligus menggunakan text_target (API modern)
        tokenized = tokenizer(
            examples["input"],
            text_target=examples["target"],
            truncation=True,
            max_length=max_length,
            padding="max_length"
        )
        
        # Ganti pad_token_id dengan -100 agar diabaikan loss function
        labels_with_ignore_index = []
        for label_example in tokenized['labels']:
            labels_with_ignore_index.append([
                (l if l != tokenizer.pad_token_id else -100) for l in label_example
            ])
            
        tokenized["labels"] = labels_with_ignore_index
        return tokenized

    tokenized_dataset = raw_dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=raw_dataset.column_names,
        desc="Tokenizing domain dataset from JSONL"
    )
    
    print(f"SUCCESS: Memuat {len(tokenized_dataset)} baris data domain.")
    return tokenized_dataset, tokenizer
