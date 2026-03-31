# Rangkuman: Matriks

Kita sudah berada di penghujung materi Matriks. Sampai sejauh ini, Anda telah memahami matriks dalam matematika hingga penerapannya dalam pemrograman Python. Mari kita rangkum secara saksama.

---

## Fundamental Matriks

Matriks dalam matematika merupakan himpunan bilangan atau elemen yang disusun berdasarkan **baris** dan **kolom**.

![Struktur matriks dalam matematika](assets/struktur-matriks-rangkuman.jpeg)

Jenis-jenis matriks:

- **Matriks Pengukuran** — indeks `(i, j)` merepresentasikan titik koordinat; elemen bertipe `float`
- **Matriks Satuan** — elemen hanya bernilai `0` atau `1`; elemen bertipe `integer`

Dalam pemrograman, matriks diimplementasikan menggunakan **nested list**:

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

Atau menggunakan library **NumPy** untuk efisiensi memori:

```python
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)
```

Kesimpulan matriks dalam pemrograman:

- Matriks adalah tabel dua dimensi dengan elemen terdefinisi berdasarkan baris dan kolom
- Setiap elemen dapat diakses melalui metode *indexing* jika kedua indeks diketahui
- Elemen matriks bersifat **homogen** — semua elemen harus bertipe data yang sama

> Menggunakan nested list untuk matriks besar sangat memakan memori. NumPy jauh lebih efisien untuk kasus tersebut.

---

## Implementasi Matriks pada Python

Ada dua cara mendeklarasikan matriks:

### Deklarasi Sekaligus Inisialisasi Nilai

Digunakan jika nilai sudah diketahui:

![Struktur deklarasi matriks dengan nilai langsung](assets/struktur-deklarasi-nilai-rangkuman.png)

### Deklarasi dengan Nilai Default

Digunakan jika nilai belum diketahui — menggunakan nested list comprehension:

![Struktur deklarasi matriks dengan nilai default](assets/struktur-deklarasi-default-rangkuman.png)

Untuk mengakses elemen matriks, gunakan metode *indexing* dengan indeks baris dan kolom:

![Ilustrasi akses elemen matriks](assets/ilustrasi-akses-elemen-rangkuman.jpeg)

---

## Operasi Matriks pada Python

Operasi matriks dapat melibatkan satu atau dua matriks:

**Operasi 1 matriks:**
- Menghitung total semua elemen
- Mengalikan elemen dengan konstanta
- Transpose, inverse, determinan, dll.

**Operasi 2 matriks:**
- Menambahkan dua matriks
- Mengalikan dua matriks
- Pembagian dua matriks, dll.

Contoh perkalian matriks dengan konstanta menggunakan NumPy:

```python
import numpy as np

var_mat = np.array([[5, 0],
                    [1, -2]])

result = var_mat * 2
print(result)

"""
Output:
[[10  0]
 [ 2 -4]]
"""
```
