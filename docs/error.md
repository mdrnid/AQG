Project root : D:\2-Project\AQG
Python       : 3.12.13

Materi dir  : D:\2-Project\AQG\dataset_aqg\materi
Output dir  : D:\2-Project\AQG\dataset_aqg\output_domain
Formats     : ['span_corruption', 'qa_generic']

Semua modul (11):
  01-Berkenalan-dengan-python
  02-berinteraksi-dengan-data
  03-ekspresi
  04-aksi-sekuensial
  05-control-flow
  06-array
  07-matriks
  08-subprogram
  09-oop
  10-style-guide
  11-unit-testing

Total chunks: 6

────────────────────────────────────────────────────────────

Chunk 1: [# Tipe Data] | tokens=283 | has_code=False
# Tipe Data

Sebagaimana yang telah dijelaskan, setiap nilai yang digunakan dalam variabel adalah sebuah data. Data memiliki tipe yang berbeda-beda dan dapat kita temui dalam kehidupan sehari-hari. Simak kisah berikut. > "Seorang pria berumur 30 tahun menjalani kehidupan di ibu kota Jakarta. Pria te...
────────────────────────────────────────────────────────────

Chunk 2: [### Numbers] | tokens=335 | has_code=True
### Numbers

Tipe data `numbers` adalah tipe data angka yang terdiri dari tiga jenis:

| Jenis | Deskripsi | Contoh |
|-------|-----------|--------|
| `int` | Bilangan bulat positif atau negatif, tanpa desimal | `1`, `-20`, `999`, `0` |
| `float` | Bilangan riil, dapat berupa bilangan bulat atau des...
────────────────────────────────────────────────────────────

Chunk 3: [### String] | tokens=306 | has_code=True
### String

`String` merupakan karakter yang berurutan, diawali dengan single quote (`''`) atau double quote (`""`).
```python
x = 'Dicoding'
print(type(x))

"""
Output:
<class 'str'>
"""
```
Beberapa fakta menarik tentang string Python:

**1. Multi-line string** menggunakan triple quote (`"""` atau...
────────────────────────────────────────────────────────────


============================================================
SPAN CORRUPTION
============================================================
Input  : # <extra_id_0> telah dijelaskan, setiap nilai yang digunakan dalam variabel adalah sebuah data. Data memiliki tipe yang berbeda-beda dan dapat kita temui dalam kehidupan sehari-hari. Simak kisah berik
Target : <extra_id_0> Tipe Data Sebagaimana yang <extra_id_1> yang dapat diambil dari <extra_id_2> - **Umur** — <extra_id_3> *numbers* dengan <extra_id_4> 50 huruf. - <extra_id_5> primitif** dan **tipe <extra_
Format : span_corruption


============================================================
QA GENERIC
============================================================
QA pairs ditemukan: 2

QA 1:
  Input  : Apa itu tipe data primitif dalam Python?
  Target : Dalam Python, tipe data dikelompokkan menjadi dua: **tipe data primitif** dan **tipe data collection**.

QA 2:
  Input  : Apa itu tipe data collection dalam Python?
  Target : Dalam Python, tipe data dikelompokkan menjadi dua: **tipe data primitif** dan **tipe data collection**.

Raw     : 47 data points
  Valid   : 47 | Failed: 0

[MODULE] 02-berinteraksi-dengan-data
  Chunks  : 15 dari 6 file
                                                                          Raw     : 44 data points
  Valid   : 43 | Failed: 1

[WRITE] Menulis final splits...
[DONE] 90 data points → D:\2-Project\AQG\dataset_aqg\output_domain_preview
       Train: 72 | Val: 9 | Test: 9

============================================================
[SUMMARY]
  Raw generated : 91
  Valid         : 90
  Failed        : 1
  span_corruption     : 30
  qa_generic          : 60
============================================================

Summary: {'total_raw': 91, 'total_valid': 90, 'total_failed': 1, 'format_counts': {'span_corruption': 30, 'qa_generic': 60}, 'output_dir': 'D:\\2-Project\\AQG\\dataset_aqg\\output_domain_preview'}
