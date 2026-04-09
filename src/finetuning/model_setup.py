from transformers import AutoModelForSeq2SeqLM
from peft import LoraConfig, get_peft_model, TaskType

def setup_model_with_lora(
    model_name="Wikidepia/IndoT5-base",
    lora_r=8,
    lora_alpha=16,
    lora_dropout=0.1
):
    """
    Setup model IndoT5 base dengan adapter LoRA.
    
    Args:
        model_name: Nama model referensi di HuggingFace
        lora_r: Target rank matriks dimensi rendah (semakin tinggi = lebih pintar tapi boros memori)
        lora_alpha: Faktor scaling LoRA
        lora_dropout: Probabilitas dropout untuk layer LoRA
    
    Returns:
        model: Model bahasa dengan injeksi layer LoRA siap latih
    """
    # 1. Load base model yang sudah pre-trained
    base_model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # 2. Konfigurasi LoRA untuk model berarsitektur Seq2Seq / T5
    lora_config = LoraConfig(
        task_type=TaskType.SEQ_2_SEQ_LM,
        r=lora_r,
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
        target_modules=["q", "v"],  # Fokus ke layer Attention (Query & Value) milik T5
        bias="none"
    )
    
    # 3. Gabungkan pre-trained model dengan konfigurasi adapter r, alpha
    model = get_peft_model(base_model, lora_config)
    
    # Tampilkan persentase parameter yang dilatih (biasanya hanya < 1%)
    model.print_trainable_parameters()
    
    return model

if __name__ == "__main__":
    # Test eksekusi local
    model = setup_model_with_lora()
    print("Model berhasil ter-setup dengan konfigurasi LoRA!")
