**Rencana Awal untuk Memulai Proyek (Prioritas Langkah Pertama)**

Terima kasih telah berbagi draft terbaru proyek (“P -- Quiz v3.pdf”). Draft ini sudah cukup matang dan konsisten dengan scope yang telah kita sepakati (fokus pada pengembangan model **IndoT5 + LoRA** untuk Automatic Question Generation, tanpa integrasi platform Maguru yang mendalam).  

Berikut adalah **urutan prioritas kerja** yang paling efektif dan logis untuk memulai proyek ini. Saya susun berdasarkan ketergantungan antar tahap (dataset adalah fondasi utama).

### 1. **Persiapan Dataset (Paling Prioritas – Minggu 1–2)**
   Ini adalah langkah **paling penting dan pertama** yang harus dilakukan, karena seluruh fine-tuning, training, dan evaluasi bergantung pada kualitas dataset.

   **Tugas konkret yang perlu dikerjakan sekarang:**
   - Ekstrak materi Python Basics dari file Markdown/YAML yang tersedia di Maguru (sesuai bagian 3 draft).
   - Buat **minimal 400–800 pasang data berkualitas tinggi** (text-to-text) sesuai format yang sudah didefinisikan di draft (Input = konteks + prompt; Output = pertanyaan + jawaban benar + 3–4 distraktor + metadata).
   - Gunakan **seed data** yang sudah ada: quiz lama Maguru + dataset publik (Glaive Python QA, Python MCQ dari Kaggle/PYnative) yang diterjemahkan dan diadaptasi ke bahasa Indonesia.
   - Lakukan **human annotation** awal (Anda + 2–3 rekan) untuk 300–500 data inti agar memenuhi standar kualitas tinggi (grammatical correctness, difficulty calibration, distraktor plausible).
   - Terapkan strategi augmentasi awal yang sudah tercantum: back-translation, synonym replacement (IndoWordNet), paraphrasing dengan GPT-4o, dan difficulty-controlled generation.
   - Simpan dalam format Hugging Face Dataset (JSONL atau Arrow) dengan kolom: `input`, `target`, dan `metadata`.

   **Output yang diharapkan**: Folder dataset siap (`train/`, `validation/`, `test/`) dengan target awal 400–800 pasang.

### 2. **Persiapan Lingkungan Teknis (Dilakukan paralel dengan dataset)**
   - Buat environment Python baru (Python 3.10+).
   - Install library utama: `transformers`, `peft` (untuk LoRA), `datasets`, `torch`, `sentence-transformers` (untuk cosine similarity IndoBERT), `huggingface_hub`.
   - Siapkan akses GPU (Colab Pro, RunPod, atau server lokal dengan minimal 16 GB VRAM).
   - Login Hugging Face untuk push model/dataset nanti.

### 3. **Implementasi Preprocessing Pipeline (Minggu 2–3)**
   Setelah dataset minimal tersedia, buat script preprocessing sesuai sub-bagian 4.1 draft:
   - Sentence segmentation & chunking (250–400 token).
   - Tokenisasi dengan tokenizer IndoT5 + mT5.
   - Normalisasi code-mixed.
   - Penambahan metadata.

### 4. **Fine-tuning IndoT5 + LoRA (Minggu 3–5)**
   - Gunakan hyperparameter yang sudah tercantum di draft (rank=8, alpha=16, learning rate=2×10⁻⁴, batch size=8, max 6 epoch, early stopping).
   - Mulai dengan IndoT5 (IndoNanoT5-base) sebagai backbone utama.
   - Simpan checkpoint model terbaik.

### 5. **Implementasi Generation & Evaluasi (Minggu 5–7)**
   - Question Generation (constrained beam search).
   - Distractor Generation hybrid (rule-based + model-based + cosine filter < 0.65).
   - Jalankan evaluasi otomatis (BLEU-4, ROUGE-L, BERTScore, METEOR) dan human evaluation (100 soal acak).

### 6. **Studi Komparatif (Minggu 7–8)**
   Bandingkan dengan baseline yang disebutkan di draft: mT5-base dan IndoBART + LoRA.

**Rekomendasi Urutan Kerja Praktis (2 Minggu Pertama)**  
1. Hari 1–3 → Kumpulkan & anotasi 300–500 data inti (human validation).  
2. Hari 4–7 → Buat script augmentasi data + generate synthetic data dengan GPT-4o/Claude.  
3. Minggu 2 → Setup environment + preprocessing script + verifikasi format dataset.  

Jika Anda setuju dengan urutan ini, saya sarankan kita mulai dari **langkah 1 (Dataset)**. Apakah Anda ingin saya:
- Membuat template script Python untuk ekstraksi Markdown/YAML dan pembuatan pasangan data?
- Membuat contoh 10 pasang data baru yang langsung sesuai format tabel di draft?
- Atau menyusun timeline Gantt sederhana untuk seluruh proyek (8–10 minggu)?

Silakan beri tahu langkah mana yang ingin kita kerjakan **sekarang**.