from datasets import load_dataset
from transformers import AutoTokenizer

def load_aqg_dataset(data_dir, tokenizer_name="Wikidepia/IndoT5-base"):
    """
    Load AQG dataset dari file JSONL.
    
    Args:
        data_dir: Path ke folder dataset (harus berisi train.jsonl, validation.jsonl, test.jsonl)
        tokenizer_name: Nama tokenizer HuggingFace
    
    Returns:
        tokenized_dataset: HuggingFace Dataset object yang sudah ditokenize
        tokenizer: Tokenizer object
    """
    # Load dataset
    dataset = load_dataset('json', data_files={
        'train': f'{data_dir}/train.jsonl',
        'validation': f'{data_dir}/validation.jsonl',
        'test': f'{data_dir}/test.jsonl'
    })
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    # Fungsi Tokenize
    def tokenize_function(examples):
        # Tokenize inputs (input text model)
        model_inputs = tokenizer(
            examples['input'], 
            max_length=512, 
            truncation=True, 
            padding='max_length'
        )
        
        # Tokenize targets (expected output)
        labels = tokenizer(
            text_target=examples['target'], 
            max_length=512, 
            truncation=True, 
            padding='max_length'
        )
        
        # T5 memerlukan labels dalam 'input_ids'
        # PENTING: Ganti pad_token_id menjadi -100 agar diabaikan oleh loss function
        labels_with_ignore_index = []
        for label_example in labels['input_ids']:
            labels_with_ignore_index.append([
                (l if l != tokenizer.pad_token_id else -100) for l in label_example
            ])
            
        model_inputs['labels'] = labels_with_ignore_index
        return model_inputs
    
    # Apply tokenisasi ke seluruh dataset parallel
    tokenized_dataset = dataset.map(
        tokenize_function, 
        batched=True, 
        remove_columns=dataset['train'].column_names
    )
    
    return tokenized_dataset, tokenizer

if __name__ == "__main__":
    # Test local run
    dataset, tokenizer = load_aqg_dataset('./dataset_aqg/dataset-task-spesifc')
    print(f"Train size: {len(dataset['train'])}")
    print(f"Validation size: {len(dataset['validation'])}")
