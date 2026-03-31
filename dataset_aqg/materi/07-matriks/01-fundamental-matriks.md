# Fundamental Matriks

Pada materi sebelumnya, kita telah mempelajari cara menyimpan data menggunakan array (list) dalam Python. Array adalah struktur data **1 dimensi** yang menyimpan data secara linear.

Pada materi ini, kita akan mempelajari jenis array **2 dimensi**, yakni **matriks**.

![Ilustrasi perbedaan array 1D dan matriks 2D](assets/array-vs-matriks.jpeg)

---

## Matriks dalam Matematika

Matriks dalam matematika merupakan sekumpulan bilangan, simbol, atau ekspresi yang disusun berdasarkan **baris** dan **kolom**.

![Struktur matriks dalam matematika](assets/struktur-matriks-matematika.jpeg)

Penamaan baris dan kolom dibuat secara berurutan — baris ke-1 dimulai dari atas ke bawah, kolom ke-1 dimulai dari kiri ke kanan.

Beberapa jenis matriks dalam matematika:

- **Matriks Pengukuran** — indeks `(i, j)` merepresentasikan titik koordinat; setiap elemen adalah bilangan real (`float`)

  ![Contoh matriks pengukuran](assets/matriks-pengukuran.png)

- **Matriks Satuan** — elemen hanya bernilai `0` atau `1`; setiap elemen bertipe `integer`

  ![Contoh matriks satuan](assets/matriks-satuan.png)

---

## Matriks dalam Pemrograman

Dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk **tabel dua dimensi** dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks diimplementasikan menggunakan **array dua dimensi** — dalam Python menggunakan **nested list**.

![Ilustrasi nested list sebagai matriks](assets/nested-list-matriks.jpeg)

Kesimpulan matriks dalam pemrograman:

- Matriks adalah tabel dua dimensi dengan elemen terdefinisi berdasarkan baris dan kolom
- Setiap elemen dapat diakses melalui metode *indexing* jika kedua indeks diketahui
- Elemen matriks bersifat **homogen** — semua elemen harus bertipe data yang sama

```python
matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(matriks)

"""
Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
```

---

## Matriks dengan NumPy

Menggunakan nested list untuk matriks besar sangat memakan memori — setiap elemen disimpan di lokasi memori terpisah. Matriks 100×100 menghasilkan 10.000 elemen dengan 10.000 lokasi penyimpanan.

Untuk matriks besar, programmer Python biasanya menggunakan library **NumPy** yang lebih efisien dalam penggunaan memori.

Cek apakah NumPy sudah terinstal:

```bash
pip show numpy
```

Jika belum, instal dengan:

```bash
pip install numpy
```

Implementasi matriks dengan NumPy:

```python
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
```

### Perbandingan Penggunaan Memori

```python
import numpy
import sys

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Ukuran keseluruhan elemen list dalam bytes =", sys.getsizeof(var_list) * len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes =", var_array.size * var_array.itemsize)

"""
Output:
Ukuran keseluruhan elemen list dalam bytes = 240
Ukuran keseluruhan elemen NumPy dalam bytes = 72
"""
```

Dengan matriks yang sama, NumPy hanya menggunakan **72 bytes** dibanding list Python yang menggunakan **240 bytes** — inilah alasan banyak programmer memilih NumPy untuk memproses matriks.

> **Catatan:** Seluruh materi pada modul ini akan menggunakan list Python untuk mengimplementasikan matriks, agar kita memahami fundamental matriks tanpa melibatkan library apa pun.
