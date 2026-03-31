 # Evaluasi dan Saran Revisi: AQG Dataset Pipeline Requirement & Design

Secara keseluruhan, dokumen *Requirement* dan *Design* yang Anda susun sangat komprehensif, teknis, dan siap diimplementasikan. Penggunaan *Correctness Properties* menunjukkan pendekatan *engineering* yang sangat matang. Namun, mengingat skala proyek kita yang mencakup 25 *lesson*, ada beberapa poin yang perlu dievaluasi dan direvisi untuk memastikan efisiensi dan kualitas dalam skala besar.

## 1. Evaluasi Komponen Utama

### Chunker (src/chunker.py)
*   **Kekuatan**: Strategi pemotongan berdasarkan *heading* dan penanganan *code block* sudah sangat baik. Properti *invariant* jumlah token (Property 1) memastikan data masuk ke IndoT5 tidak terpotong.
*   **Saran Revisi**: Tambahkan fungsionalitas untuk mengekstraksi *Learning Objectives* (jika ada di materi) sebagai metadata tambahan. Ini akan sangat membantu model dalam menghasilkan soal yang lebih relevan secara pedagogis.

### Prompt Constructor (src/prompt_constructor.py)
*   **Kekuatan**: Penggunaan *template* yang konsisten (Property 4) adalah kunci keberhasilan *fine-tuning*.
*   **Saran Revisi**: Mengingat kita memiliki 25 *lesson*, *template* perlu mendukung variasi bahasa yang lebih kaya agar model tidak *overfitting* pada satu struktur kalimat instruksi saja. Saya menyarankan penambahan *Multiple Prompt Templates* yang dipilih secara acak saat konstruksi.

### Synthetic Generator (src/synthetic_generator.py)
*   **Kekuatan**: Dukungan multi-LLM dan *system prompt* yang ketat.
*   **Saran Revisi**: Gunakan **Instructor** atau **DSPy** di sini (seperti yang kita bahas di sesi *brainstorming*). Daripada hanya mengandalkan *plain string* dan berharap model mematuhi format (Property 6), Instructor akan menjamin *output* terstruktur melalui Pydantic sebelum diubah menjadi *plain string* final untuk dataset.

## 2. Tabel Saran Revisi Spesifik

| Komponen | Masalah Potensial | Saran Revisi / Solusi |
| :--- | :--- | :--- |
| **Metadata** | Skala 25 *lesson* bisa membuat pelabelan `concept` manual menjadi sangat lambat. | Gunakan LLM di tahap *Synthetic Generator* untuk secara otomatis menyarankan `concept` dari *Master Concept List* berdasarkan isi *chunk*. |
| **Target Format** | Format "Pertanyaan: ... Jawaban benar: ... Distraktor: ..." mungkin sulit di-*parse* jika ada karakter serupa di dalam konten soal. | Gunakan pemisah yang lebih unik atau tetap gunakan JSON internal sebelum di-*flatten* menjadi string final. |
| **Augmentor** | Risiko duplikasi data yang tinggi saat melakukan augmentasi skala besar. | Implementasikan *Semantic Deduplication* (menggunakan *embeddings*) selain *String-based Deduplication* (Property 11). |
| **Validation** | Validasi saat ini hanya bersifat struktural (panjang teks, keberadaan field). | Tambahkan *Pedagogical Validation* menggunakan LLM untuk memeriksa apakah *distractor* benar-benar *plausible* (masuk akal) dan tidak terlalu mudah. |

## 3. Penyesuaian untuk Skala 25 Lesson

Dengan total 25 *lesson*, kita perlu memastikan *pipeline* ini dapat berjalan secara *batch* dan memiliki mekanisme *checkpointing*.

*   **Batch Processing**: *Pipeline* harus bisa memproses satu *section* (5 *lesson*) sekaligus dan menyimpan hasilnya sebelum lanjut ke *section* berikutnya. Ini mencegah kehilangan data jika terjadi kegagalan API di tengah jalan.
*   **Master Concept List Integration**: Dokumen `design.md` sudah mencantumkan `CONCEPTS`, namun perlu dipastikan bahwa skrip `chunker.py` dapat secara otomatis memetakan file Markdown ke kunci yang tepat di dalam kamus `CONCEPTS` tersebut berdasarkan nama folder/file.
*   **Cost Management**: Menghasilkan 800 pasang data dengan GPT-4o bisa memakan biaya. Pertimbangkan untuk menggunakan model yang lebih murah (seperti GPT-4o-mini) untuk tugas-tugas awal seperti *chunking* dan pelabelan konsep, sementara GPT-4o digunakan khusus untuk generasi soal dan distraktor.

## 4. Kesimpulan

Rancangan Anda sudah sangat solid. Jika saran-saran di atas (terutama integrasi Instructor untuk validasi *output* dan optimasi pelabelan konsep otomatis) diimplementasikan, *pipeline* ini akan sangat *robust* untuk menghasilkan dataset berkualitas tinggi bagi IndoT5.

Apakah Anda ingin saya membantu mendetailkan implementasi salah satu komponen di atas (misalnya skrip `chunker.py` atau `synthetic_generator.py`) berdasarkan saran revisi ini?
