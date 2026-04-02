# Laporan Evaluasi Dataset AQG Python: `accumulated.jsonl`

Laporan ini menyajikan evaluasi komprehensif terhadap dataset `accumulated.jsonl` yang dihasilkan untuk proyek *Automatic Question Generation* (AQG) Python berbahasa Indonesia. Tujuan evaluasi adalah untuk menilai kepatuhan dataset terhadap spesifikasi desain yang telah disepakati, kualitas konten pedagogis, serta mengidentifikasi area untuk perbaikan lebih lanjut, terutama mengingat skala proyek yang melibatkan 5 *section* dan 25 *lesson* materi.

## 1. Penilaian Keseluruhan

Secara umum, *pipeline* awal berhasil menghasilkan data dalam format JSONL yang benar, dengan struktur `input`, `target`, dan `metadata` yang sesuai. Ini menunjukkan bahwa fondasi teknis untuk proses generasi dataset sudah terbentuk. Namun, evaluasi mendalam mengungkapkan beberapa tantangan signifikan terkait kualitas konten pedagogis, konsistensi metadata, dan ketergantungan konteks yang perlu diatasi untuk mencapai dataset berkualitas tinggi yang siap untuk *fine-tuning* model IndoT5.

## 2. Analisis Struktural dan Validasi Format

File `accumulated.jsonl` berhasil di-*parse* sebagai kumpulan objek JSON yang valid, dengan setiap baris merepresentasikan satu pasangan data. Ini sesuai dengan format JSON Lines yang dibutuhkan untuk *fine-tuning* model *seq2seq*.

### Field `input`
Field `input` adalah string yang menggabungkan `Konteks` dan `Prompt`, sesuai dengan `Prompt Template` yang dirancang. Struktur ini memastikan model menerima semua informasi yang diperlukan untuk menghasilkan *target*. Namun, panjang `input` yang bervariasi dan terkadang sangat panjang (termasuk seluruh *chunk* materi) perlu diperhatikan agar tidak melebihi batasan token model IndoT5.

### Field `target`
Field `target` adalah *plain string* yang berisi pertanyaan, jawaban benar, dan distraktor. Format ini krusial untuk *fine-tuning* model *seq2seq*. Kepatuhan terhadap format ini sangat baik. Namun, format *plain string* ini rentan terhadap masalah *parsing* jika ada karakter khusus atau format yang tidak terduga di dalam pertanyaan atau distraktor itu sendiri. Ini menegaskan kembali rekomendasi untuk mengintegrasikan **Instructor** guna menjamin *output* terstruktur dari LLM sebelum di-*flatten* menjadi *plain string* final.

### Field `metadata`
Field `metadata` adalah objek JSON yang berisi informasi tambahan tentang soal, mencakup `difficulty`, `question_type`, `concept`, `misconception_tags`, `source_file`, `section`, `source`, dan `validated`. Observasi menunjukkan:
*   **`difficulty`**: Semua entri saat ini dilabeli `"easy"`. Ini mengindikasikan kurangnya variasi tingkat kesulitan yang dihasilkan atau diminta oleh *prompt*.
*   **`question_type`**: Konsisten sebagai `"MCQ"`.
*   **`concept`**: Pemetaan konsep seringkali dipaksakan oleh *prompt* daripada secara akurat merefleksikan isi *chunk*. Misalnya, *chunk* tentang PEP (Python Enhancement Proposals) diprompt untuk `concept: "Sejarah Python"` atau `"Ciri Khas Python"`, yang menyebabkan soal yang dihasilkan tidak sepenuhnya relevan dengan konteks langsung.
*   **`misconception_tags`**: Semua entri memiliki array kosong `[]`. Ini adalah kelemahan signifikan karena salah satu tujuan proyek adalah menghasilkan distraktor pedagogis berdasarkan miskonsepsi.
*   **`source_file` dan `section`**: Informasi ini terekam dengan baik, meskipun format *path* `dataset_aqg\materi\01-Berkenalan-dengan-python\01-perkenalan-pythn.md` menggunakan *backslash* (`\`) yang lebih umum di Windows, sementara lingkungan Linux menggunakan *forward slash* (`/`). Ini perlu distandardisasi.
*   **`source`**: Konsisten sebagai `"synthetic"`.
*   **`validated`**: Semua entri bernilai `false`, menunjukkan bahwa tahap validasi belum dilakukan.

## 3. Evaluasi Kualitas Konten Pedagogis

### Kualitas Pertanyaan dan Jawaban
Pertanyaan yang dihasilkan umumnya relevan dengan konteks yang diberikan dan jawaban benarnya akurat, terutama untuk informasi faktual. Namun, terdapat sedikit variasi dalam formulasi pertanyaan, dengan beberapa pertanyaan yang secara semantik identik muncul dari *chunk* yang sama. Keterbatasan pada tingkat kesulitan "easy" juga menjadi perhatian, karena proyek ini membutuhkan soal dengan berbagai tingkat kesulitan.

### Kualitas Distraktor (Plausibilitas)
Distraktor yang dihasilkan bervariasi dalam kualitas. Sebagian besar cukup *plausible* (misalnya, nama tokoh teknologi lain sebagai distraktor untuk pencipta Python). Namun, ada kasus di mana distraktor terlalu mudah ditebak atau, yang lebih kritis, model berhalusinasi atau menggunakan pengetahuan internal yang tidak ada dalam konteks yang diberikan. Contoh paling jelas adalah soal tentang ciri khas Python (indentasi) yang dihasilkan dari konteks tentang PEP, di mana informasi indentasi tidak ada dalam teks sumber. Ini melanggar prinsip *context grounding* yang esensial untuk dataset ini.

### Metadata Pedagogis
Kekosongan `misconception_tags` adalah area perbaikan utama. Tanpa tag ini, sulit untuk menilai kualitas pedagogis distraktor secara otomatis atau memastikan bahwa distraktor secara efektif menargetkan miskonsepsi umum siswa. Pemetaan `concept` yang tidak selalu akurat dengan konteks juga menunjukkan bahwa *prompting* saat ini belum cukup dinamis atau cerdas dalam mengidentifikasi konsep utama dari *chunk*.

## 4. Area Kritis untuk Perbaikan dan Rekomendasi

Berdasarkan evaluasi di atas, berikut adalah area kritis untuk perbaikan dan rekomendasi konkret:

| Area Perbaikan | Rekomendasi Konkret | Justifikasi |
| :--- | :--- | :--- |
| **Context Grounding** | **Perbaiki `Prompt Constructor`**: Pastikan `concept` yang diminta dalam *prompt* benar-benar diekstraksi atau divalidasi relevansinya dengan `text_chunk` yang diberikan. Gunakan LLM untuk membantu identifikasi konsep dari *chunk* sebelum membuat *prompt*. | Mencegah model berhalusinasi atau menghasilkan soal yang tidak relevan dengan konteks yang diberikan, memastikan integritas pedagogis. |
| **Generasi `misconception_tags`** | **Revisi `GENERATION_SYSTEM_PROMPT`**: Tambahkan instruksi eksplisit agar LLM mengidentifikasi dan menghasilkan `misconception_tags` yang relevan dengan distraktor yang dibuat. | Memungkinkan dataset untuk secara efektif menargetkan miskonsepsi siswa, meningkatkan nilai pedagogis soal. |
| **Variasi Tingkat Kesulitan** | **Diversifikasi `TaskParams`**: Secara aktif masukkan `difficulty` (`medium`, `hard`) ke dalam `Prompt Constructor` dan pantau kualitas *output*. Lakukan *human annotation* untuk soal dengan kesulitan lebih tinggi. | Membangun dataset yang lebih kaya dan menantang, melatih model untuk menghasilkan soal dengan kompleksitas yang bervariasi. |
| **Deduplikasi Semantik** | **Implementasikan `Augmentor.deduplicate`**: Selain deduplikasi berbasis string, pertimbangkan deduplikasi berbasis *embedding* untuk mengidentifikasi dan menghapus soal yang secara semantik identik. | Mengurangi redundansi dalam dataset, memastikan setiap entri memberikan informasi unik untuk *fine-tuning*. |
| **Robustness `target` Parsing** | **Integrasikan `Instructor`**: Gunakan pustaka Instructor untuk memvalidasi *output* LLM sebagai objek JSON terstruktur terlebih dahulu, sebelum mengonversinya menjadi *plain string* `target`. | Menjamin format *output* yang konsisten dan valid, mengurangi *error* *parsing* di kemudian hari. |
| **Standardisasi Path** | **Normalisasi `source_file`**: Pastikan *path* `source_file` menggunakan *forward slash* (`/`) yang konsisten di semua sistem operasi. | Meningkatkan portabilitas dan konsistensi data. |
| **Validasi Pedagogis** | **Tambahkan Tahap Validasi LLM**: Kembangkan komponen *Validator* untuk menggunakan LLM lain (atau LLM yang sama dengan *prompt* berbeda) untuk menilai *plausibility* distraktor dan relevansi soal dengan konteks. | Menambahkan lapisan kualitas otomatis untuk memastikan distraktor benar-benar pedagogis dan soal terikat konteks. |

## 5. Kesimpulan

Dataset `accumulated.jsonl` adalah langkah awal yang menjanjikan, menunjukkan kemampuan *pipeline* untuk menghasilkan data terstruktur. Namun, untuk mencapai kualitas yang dibutuhkan untuk *fine-tuning* model AQG yang efektif, perbaikan pada *context grounding*, generasi `misconception_tags`, variasi tingkat kesulitan, dan robustnes *output* sangat diperlukan. Dengan mengimplementasikan rekomendasi di atas, dataset akan menjadi aset yang jauh lebih berharga untuk proyek Anda. Saya siap membantu Anda dalam setiap langkah implementasi perbaikan ini.
