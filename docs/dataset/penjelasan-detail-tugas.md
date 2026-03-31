**Penjelasan Detail Tugas Persiapan Dataset (Langkah Prioritas Utama)**

Terima kasih atas konfirmasi bahwa environment sudah siap. Karena Anda ingin fokus pada **Persiapan Dataset** dari materi yang sudah disediakan (`perkenalan-pythn.md` dan `menjalankan-kode-program-pertama.md`), berikut penjelasan lengkap, langkah demi langkah, serta cara praktis mengubah kedua file Markdown tersebut menjadi dataset berkualitas tinggi sesuai format yang tercantum dalam draft proyek.

### 1. Tujuan & Format Dataset yang Dibutuhkan
Dataset harus berupa **pasangan text-to-text** (seq2seq style) untuk fine-tuning IndoT5 + LoRA:
- **Input** (prompt ke model): Konteks materi (chunk 250–400 token) + instruksi tugas (prompt engineering).
- **Target** (output yang diharapkan model): Pertanyaan lengkap + Jawaban benar + 3–4 distraktor + metadata (JSON-like).
- Kolom utama yang disimpan: `input`, `target`, `metadata`.

Format akhir yang paling direkomendasikan untuk Hugging Face dan API Next.js adalah **JSONL** (satu baris JSON per data point) atau list of dicts dalam file JSON. Ini memudahkan pengiriman ke frontend via API.

### 2. Langkah-langkah Praktis Membuat Dataset dari Dua File Markdown
Berikut urutan kerja yang jelas dan dapat Anda kerjakan hari ini:

1. **Chunking Materi**  
   Bagi kedua file Markdown menjadi potongan (chunk) berukuran 250–400 token berdasarkan sub-heading atau learning objective.  
   - Gunakan tool sederhana (Python script dengan `nltk`/`spaCy` atau bahkan manual) untuk memotong per paragraf + code block.

2. **Identifikasi Konsep Utama**  
   Dari `perkenalan-pythn.md`:  
   - Sejarah Python & Guido van Rossum  
   - Ciri khas Python (tidak pakai semicolon)  
   - Versi Python 2.x vs 3.x  
   - Python Software Foundation, PEP, Zen of Python  
   - Mengapa Python (popularitas, gaya pemrograman, use case)  

   Dari `menjalankan-kode-program-pertama.md`:  
   - Sintaks `print()`  
   - Menjalankan file `.py` di terminal  
   - Latihan ubah pesan “Hello World!”

3. **Buat Pasangan Data (Input → Target)**  
   Untuk setiap chunk, buat 1–2 soal (MCQ atau Code Completion).  
   Gunakan prompt template yang konsisten.

4. **Tambahkan Distraktor yang Berkualitas**  
   Buat distraktor berdasarkan *common student mistakes* (misconception).

5. **Human Validation & Augmentasi**  
   Validasi manual 300–500 data pertama, lalu augmentasi (back-translation, paraphrasing GPT-4o, dll.).

6. **Simpan dalam Format JSON**  
   Struktur yang ideal untuk API Next.js:
   ```json
   {
     "input": "Konteks: [chunk materi] Prompt: Buat satu soal MCQ tentang [konsep], difficulty: medium, bahasa Indonesia.",
     "target": "Pertanyaan: [full question]? Jawaban benar: [answer]. Distraktor: 1) ... 2) ... 3) ... 4) ...",
     "metadata": {
       "difficulty": "medium",
       "concept": "python_history",
       "misconception_tags": ["version_confusion", "semicolon"],
       "type": "MCQ"
     }
   }
   ```

### 3. Contoh Konkret Dataset dari Materi yang Anda Berikan (5 Pasang Siap Pakai)
Berikut adalah contoh nyata yang sudah saya buat langsung dari kedua file Markdown. Anda bisa copy-paste dan gunakan sebagai seed.

**Contoh 1 – Topik: Sejarah Python**  
**Input**:  
Konteks: Python dirilis tahun 1991 oleh Guido van Rossum (GvR) sebagai bahasa yang mudah dibaca dan memiliki exception handling. Prompt: Buat satu soal MCQ tentang sejarah Python, difficulty: easy, bahasa Indonesia.  

**Target**:  
Pertanyaan: “Siapa pencipta bahasa pemrograman Python dan pada tahun berapa dirilis?”  
Jawaban benar: Guido van Rossum pada tahun 1991.  
Distraktor: 1) Guido van Rossum pada tahun 2000, 2) Dennis Ritchie pada tahun 1991, 3) James Gosling pada tahun 1995.  
Metadata: difficulty=easy, concept=python_history, misconception_tags=["creator_year_confusion"]

**Contoh 2 – Topik: Ciri khas Python (tanpa semicolon)**  
**Input**:  
Konteks: Python tidak mewajibkan penggunaan titik koma (`;`) pada akhir kode. Contoh: `print("Hello World!")`. Prompt: Buat satu soal MCQ tentang ciri khas sintaks Python, difficulty: medium, bahasa Indonesia.  

**Target**:  
Pertanyaan: “Apakah Python mengharuskan penggunaan titik koma (`;`) di akhir setiap pernyataan?”  
Jawaban benar: Tidak diharuskan.  
Distraktor: 1) Ya, diharuskan seperti bahasa C, 2) Hanya di fungsi, 3) Hanya di loop.  
Metadata: difficulty=medium, concept=syntax_feature, misconception_tags=["semicolon_confusion"]

**Contoh 3 – Topik: Versi Python 2 vs 3**  
**Input**:  
Konteks: Python 3 tidak backward-compatible dengan Python 2. Prompt: Buat satu soal MCQ tentang perbedaan versi Python, difficulty: medium, bahasa Indonesia.  

**Target**:  
Pertanyaan: “Mengapa kode yang berjalan di Python 2.x mungkin tidak berjalan di Python 3.x?”  
Jawaban benar: Karena Python 3 tidak backward-compatible.  
Distraktor: 1) Karena Python 3 lebih lambat, 2) Karena Python 3 tidak mendukung print(), 3) Karena Python 3 hanya mendukung Windows.  
Metadata: difficulty=medium, concept=python_versions, misconception_tags=["backward_compatibility"]

**Contoh 4 – Topik: Zen of Python**  
**Input**:  
Konteks: Zen of Python (PEP 20) menyatakan “Readability counts” dan “Simple is better than complex”. Prompt: Buat satu soal Code Completion tentang filosofi Python, difficulty: hard, bahasa Indonesia.  

**Target**:  
Pertanyaan: “Lengkapi kalimat dari Zen of Python: ‘___ is better than ugly.’”  
Jawaban benar: Beautiful  
Distraktor: 1) Complex, 2) Fast, 3) Explicit.  
Metadata: difficulty=hard, concept=zen_of_python, misconception_tags=["philosophy_misunderstanding"]

**Contoh 5 – Topik: Menjalankan kode pertama**  
**Input**:  
Konteks: Sintaks `print("Hello World!")` dan cara menjalankan `python main.py`. Prompt: Buat satu soal MCQ tentang menjalankan program Python pertama, difficulty: easy, bahasa Indonesia.  

**Target**:  
Pertanyaan: “Perintah apa yang digunakan di terminal untuk menjalankan file `main.py`?”  
Jawaban benar: `python main.py`  
Distraktor: 1) `run main.py`, 2) `python3 main`, 3) `print main.py`.  
Metadata: difficulty=easy, concept=first_program, misconception_tags=["command_line_error"]

### 4. Format Output untuk API Next.js
Ya, sangat disarankan menyimpan dataset dalam **format JSON** atau **JSONL**.  
Anda bisa membuat prompt template yang secara otomatis menghasilkan output dalam struktur JSON di atas. Nantinya, frontend Next.js tinggal memanggil API yang mengembalikan objek JSON tersebut.

### 5. Penggunaan LangChain untuk Memudahkan Pengembangan
**Sangat direkomendasikan**. LangChain sangat cocok untuk tahap ini karena:
- Memberikan **PromptTemplate** yang reusable dan terstruktur.
- Memungkinkan **chaining** (misalnya: chunk material → generate question → generate distractors → filter cosine similarity).
- Mudah diintegrasikan dengan LLM (GPT-4o/Claude) untuk synthetic data generation.
- Nanti bisa dipakai untuk pipeline inference model IndoT5 Anda.

Saya bisa buatkan **template LangChain** lengkap (PromptTemplate + LCEL chain) untuk generate satu pasang data secara otomatis jika Anda ingin.

**Langkah Selanjutnya yang Saya Sarankan Hari Ini**  
1. Buat 50–100 pasang data manual dari kedua file MD di atas (gunakan contoh saya sebagai panduan).  
2. Simpan sebagai `dataset_seed.jsonl`.  
3. Buat script sederhana Python + LangChain untuk augmentasi otomatis.

Apakah Anda ingin saya:
- Membuat **prompt template LangChain lengkap** sekarang?
- Memberikan **script Python lengkap** untuk chunking Markdown + generate dataset JSONL?
- Atau langsung buat **50 pasang data tambahan** dari materi ini?

Silakan pilih, saya siap melanjutkan langsung.