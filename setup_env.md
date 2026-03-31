# Setup Environment — AQG Project

## Lokal (CPU) — Conda

```bash
# 1. Buat environment dari file
conda env create -f environment.yml

# 2. Aktifkan environment
conda activate aqg-indo

# 3. Daftarkan sebagai Jupyter kernel
python -m ipykernel install --user --name aqg-indo --display-name "AQG Indo (Python 3.10)"

# 4. Verifikasi instalasi
python -c "import transformers, peft, datasets, sentence_transformers; print('OK')"
```

## Google Colab Pro — saat fine-tuning

```python
# Cell pertama di notebook Colab
!pip install -r requirements.txt -q

# Verifikasi GPU tersedia
import torch
print(torch.cuda.is_available())       # harus True
print(torch.cuda.get_device_name(0))   # nama GPU
```

## Update environment (jika ada tambahan library)

```bash
conda activate aqg-indo
pip install <library-baru>

# Simpan ke requirements.txt
pip freeze > requirements_freeze.txt
```

## Struktur folder project (rekomendasi)

```
AQG/
├── environment.yml
├── requirements.txt
├── dataset_aqg/          ← materi markdown (sudah ada)
├── data/
│   ├── raw/              ← hasil ekstrak dari markdown
│   ├── processed/        ← setelah preprocessing
│   └── augmented/        ← setelah augmentasi
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_dataset_generation.ipynb
│   └── 03_finetuning_colab.ipynb
├── src/
│   ├── preprocessing.py
│   ├── prompt_builder.py
│   ├── distractor_filter.py
│   └── evaluate.py
└── models/               ← checkpoint lokal (gitignore)
```
