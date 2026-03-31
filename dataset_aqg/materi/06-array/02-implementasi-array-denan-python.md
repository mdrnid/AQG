# Implementasi Array dengan Python

Dalam materi ini, Anda akan mempelajari cara mendeklarasikan array dan mengakses elemennya menggunakan Python.

---

## Mendeklarasikan Array

Dalam Python, ada dua cara mendeklarasikan array menggunakan list.

Setiap elemen dalam list disimpan pada lokasi memori yang berbeda. Anda bisa membuktikannya dengan kode berikut:

```python
var_list = [1, 2, 3]
for elemen in var_list:
    print(id(elemen))
```

Setiap elemen memiliki ID lokasi penyimpanan yang berbeda.

---

### Mendefinisikan Isi Array

Cara pertama — mendeklarasikan variabel array sekaligus mendefinisikan isinya. Digunakan jika nilai sudah diketahui.

![Struktur deklarasi array dengan isi langsung](assets/struktur-deklarasi-array-isi.jpeg)

`<nama-var>` adalah nama variabel array dengan elemen `<val0>`, `<val1>`, ..., `<valn-1>` yang terurut berdasarkan indeks dari `0` hingga `n-1`.

```python
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
```

---

### Mendefinisikan Nilai Default

Cara kedua — mendeklarasikan array dengan nilai default. Digunakan jika nilai belum diketahui, sebagai nilai awal yang dapat diperbarui kemudian.

Nilai default ditentukan berdasarkan kesepakatan — nilainya di luar rentang yang disepakati. Misalnya jika rentang nilai yang disepakati adalah 1–10, nilai default bisa `0`.

![Struktur deklarasi array dengan nilai default](assets/struktur-deklarasi-array-default.jpeg)

Struktur ini menggunakan **list comprehension**:

- `<nama-var>` — variabel yang dideklarasikan
- `<default-val>` — nilai default (di luar range yang disepakati)
- `<n>` — ukuran panjang array

```python
var_arr = [0 for i in range(10)]
print(var_arr)

"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
```

Nilai default kemudian dapat diperbarui:

```python
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
```

---

## Mengakses Elemen Array

Mengakses elemen array menggunakan metode **indexing** — sama seperti mengakses elemen list.

![Struktur akses elemen array](assets/struktur-akses-elemen-array.jpeg)

```python
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])

"""
Output:
9
"""
```

`var_arr[0]` mengambil elemen pada indeks ke-0, yaitu `9`.
