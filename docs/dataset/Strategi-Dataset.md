# Strategi Dataset Skala Besar: 5 Section, 25 Lesson Materi Python

Dengan adanya 5 *section* dan masing-masing 5 *lesson* materi Python, total 25 *lesson*, skala persiapan dataset meningkat secara signifikan. Ini memerlukan pendekatan yang lebih terstruktur untuk memastikan konsistensi, efisiensi, dan kualitas dataset yang dihasilkan. Berikut adalah perancangan struktur folder dan skema pemetaan konsep yang diusulkan.

## 1. Perancangan Struktur Folder Materi

Struktur folder yang jelas akan mempermudah pengelolaan materi sumber dan pelacakan progres. Saya mengusulkan struktur hierarkis sebagai berikut:

```
/materi_python/
├── section_01_pengenalan/
│   ├── lesson_01_perkenalan_python.md
│   ├── lesson_02_instalasi_python.md
│   ├── lesson_03_dasar_sintaks.md
│   ├── lesson_04_tipe_data.md
│   └── lesson_05_operator.md
├── section_02_struktur_kontrol/
│   ├── lesson_01_if_else.md
│   ├── lesson_02_elif.md
│   ├── lesson_03_for_loop.md
│   ├── lesson_04_while_loop.md
│   └── lesson_05_break_continue.md
├── ... (untuk section 03, 04, 05)
└── section_05_proyek_akhir/
    ├── lesson_01_pengantar_proyek.md
    ├── lesson_02_desain_aplikasi.md
    ├── lesson_03_implementasi_fitur.md
    ├── lesson_04_debugging_testing.md
    └── lesson_05_deploy_aplikasi.md
```

**Keuntungan Struktur Ini:**
*   **Organisasi Jelas**: Memudahkan navigasi dan identifikasi materi.
*   **Modularitas**: Setiap *lesson* adalah unit independen, mempermudah pemrosesan per *lesson*.
*   **Skalabilitas**: Mudah untuk menambahkan *section* atau *lesson* baru di masa depan.

## 2. Skema Pemetaan Konsep Lintas Lesson

Dengan banyaknya *lesson*, sangat penting untuk memiliki skema pemetaan konsep yang konsisten. Ini akan membantu dalam:
*   Menghindari duplikasi pertanyaan untuk konsep yang sama.
*   Memastikan cakupan konsep yang komprehensif.
*   Memfasilitasi penentuan tingkat kesulitan yang progresif.

Saya mengusulkan pembuatan sebuah **Daftar Konsep Utama (Master Concept List)** yang akan menjadi referensi tunggal untuk semua `metadata.concept` dalam dataset. Daftar ini harus mencakup:

*   **ID Konsep Unik**: Untuk identifikasi internal.
*   **Nama Konsep**: Deskripsi singkat konsep (misalnya, "Variabel", "Fungsi `print()`", "Perulangan `for`").
*   **Definisi Singkat**: Penjelasan singkat tentang konsep.
*   **Level Kesulitan Default**: Tingkat kesulitan awal yang terkait dengan konsep tersebut (misalnya, "mudah" untuk "Variabel", "sedang" untuk "Rekursi").
*   **Lesson Terkait**: Daftar *lesson* di mana konsep ini dibahas.
*   **Potensi Miskonsepsi**: Daftar miskonsepsi umum yang terkait dengan konsep ini (misalnya, "salah_paham_indentasi", "salah_paham_scope_variabel").

**Contoh Tabel Pemetaan Konsep (sebagian):**

| ID Konsep | Nama Konsep          | Definisi Singkat                               | Level Kesulitan Default | Lesson Terkait                               | Potensi Miskonsepsi                               |
| :-------- | :------------------- | :--------------------------------------------- | :---------------------- | :------------------------------------------- | :------------------------------------------------ |
| C001      | Python Definition    | Bahasa pemrograman multifungsi                 | easy                    | section_01/lesson_01                         | -                                               |
| C002      | Guido van Rossum     | Pencipta Python                                | easy                    | section_01/lesson_01                         | tokoh_pemrograman_lain                          |
| C003      | `print()` Function   | Menampilkan output ke konsol                   | easy                    | section_01/lesson_03                         | sintaks_salah_print                             |
| C004      | Python 2.x Features  | Garbage collector, memory management           | medium                  | section_01/lesson_04                         | salah_paham_kompatibilitas_versi                |
| C005      | `if-else` Statement  | Struktur kontrol kondisional                   | medium                  | section_02/lesson_01                         | sintaks_salah_kondisi, logika_salah_cabang      |
| C006      | `for` Loop           | Perulangan iteratif                            | medium                  | section_02/lesson_03                         | sintaks_salah_loop, off_by_one_error            |

**Manfaat Master Concept List:**
*   **Konsistensi Metadata**: Memastikan semua anotator menggunakan nama konsep dan tag miskonsepsi yang sama.
*   **Panduan Generasi Soal**: Memberikan panduan yang jelas untuk membuat soal yang relevan dengan konsep tertentu.
*   **Pelacakan Cakupan**: Memungkinkan Anda untuk melihat konsep mana yang sudah memiliki soal dan mana yang belum.
*   **Dasar untuk Kurikulum Adaptif**: Dapat menjadi dasar untuk sistem pembelajaran adaptif di masa depan.

## 3. Strategi Ekstraksi Konten dari Banyak File

Dengan 25 file Markdown, proses ekstraksi konten harus diotomatisasi sebanyak mungkin.

*   **Skrip Python untuk Pembacaan File**: Buat skrip Python yang dapat mengiterasi semua file `.md` dalam struktur folder yang telah ditentukan. Skrip ini akan membaca konten setiap file.
*   **Segmentasi Otomatis**: Gunakan pustaka Markdown-parsing (misalnya, `markdown` atau `mistune`) untuk membagi konten setiap file menjadi segmen-segmen berdasarkan judul, sub-judul, atau paragraf. Setiap segmen ini akan menjadi `text_chunk` yang potensial.
*   **Ekstraksi Kode**: Identifikasi dan ekstrak blok kode Python (` ```python `) secara terpisah. Soal kuis dapat dibuat khusus untuk pemahaman kode atau *code completion*.
*   **Integrasi dengan Master Concept List**: Saat memproses setiap `text_chunk`, skrip dapat mencoba memetakan `text_chunk` tersebut ke `Nama Konsep` yang ada di Master Concept List. Ini bisa dilakukan dengan pencarian kata kunci atau, di masa depan, dengan model NLP yang lebih canggih.

Dengan perancangan ini, Anda akan memiliki kerangka kerja yang kuat untuk mengelola dan memproses materi Python Anda dalam skala besar, yang akan menjadi dasar untuk pembuatan dataset berkualitas tinggi. Selanjutnya, kita akan membahas strategi otomatisasi ekstraksi dan penanganan konsistensi antar *section* menggunakan LangChain/DSPy.
