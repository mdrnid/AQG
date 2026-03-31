# Implementasi Matriks pada Python

Sebelumnya kita telah belajar cara mengimplementasikan matriks menggunakan nested list. Ingat bahwa setiap elemen matriks bersifat **homogen** — harus memiliki tipe data yang sama.

Sekarang, kita pelajari cara mendeklarasikan matriks dan mengakses setiap elemennya dengan metode *indexing*.

---

## Deklarasi Matriks

Ada dua cara mendeklarasikan matriks menggunakan Python.

---

### 1. Deklarasi Sekaligus Inisialisasi Nilai

Digunakan jika nilai sudah diketahui. Matriks dideklarasikan dengan ukuran N baris dan M kolom (N×M).

![Struktur deklarasi matriks dengan nilai langsung](assets/struktur-deklarasi-matriks-nilai.png)

```python
matriks = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]

print(matriks)

"""
Output:
[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
"""
```

Kode di atas mendeklarasikan **matriks satuan** berukuran 5×5 — jenis matriks dengan elemen bernilai hanya `0` dan `1`.

---

### 2. Deklarasi dengan Nilai Default

Digunakan jika nilai belum diketahui. Nilai default ditentukan berdasarkan kesepakatan — nilainya di luar rentang yang disepakati. Cara ini menggunakan **nested list** dan **nested for** (list comprehension).

![Struktur deklarasi matriks dengan nilai default](assets/struktur-deklarasi-matriks-default.png)

Komponen struktur:

- `<default-val>` — nilai default (di luar range yang disepakati, misalnya `0` jika range adalah 1–10)
- `<n>` — jumlah baris matriks
- `<m>` — jumlah kolom matriks

Perulangan dalam (kedua) menghasilkan **baris**, perulangan luar (pertama) menghasilkan **kolom**.

```python
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)

"""
Output:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
"""
```

Kode di atas membuat matriks berukuran 3×4 dengan nilai default `0`.

---

## Akses Elemen Matriks

Untuk mengakses elemen matriks, gunakan metode *indexing* dengan mengetahui indeks **baris** dan **kolom**.

![Struktur akses elemen matriks](assets/struktur-akses-elemen-matriks.jpeg)

```
<namamatriks>[<nbrs>][<nkol>]
```

- `<namamatriks>` — variabel yang berisi nilai matriks
- `<nbrs>` — nomor indeks baris
- `<nkol>` — nomor indeks kolom

### Ilustrasi Indeks

![Ilustrasi indeks baris dan kolom matriks 5x5](assets/ilustrasi-indeks-matriks.jpeg)

Asumsikan matriks 5×5 berisi angka 1–25. Untuk mengakses nilai `12`:

- Nilai `12` berada pada baris ke-2, kolom ke-1 → `[2][1]`

```python
var_mat = [[1,  2,  3,  4,  5],
           [6,  7,  8,  9,  10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][1])

"""
Output:
12
"""
```
