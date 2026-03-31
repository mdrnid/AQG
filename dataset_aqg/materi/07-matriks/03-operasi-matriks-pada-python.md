# Operasi Matriks pada Python

Dalam matematika maupun pemrograman, operasi matriks dapat melibatkan satu atau dua matriks sekaligus.

**Operasi 1 matriks:**
- Menghitung total semua elemen matriks
- Mengalikan elemen matriks dengan konstanta
- Transpose matriks
- Inverse matriks
- Menentukan determinan, dll.

**Operasi 2 matriks:**
- Menambahkan dua matriks
- Mengalikan dua matriks
- Pembagian dua matriks, dll.

---

## Mengalikan Elemen Matriks dengan Konstanta

Mari pelajari salah satu operasi — **mengalikan elemen matriks dengan konstanta**.

Dalam matematika, operasi ini dapat diilustrasikan sebagai berikut (matriks 2×2):

![Ilustrasi perkalian matriks dengan konstanta](assets/ilustrasi-perkalian-konstanta.jpeg)

Matriks `[[5, 0], [1, -2]]` dikalikan dengan konstanta `2`:

1. `2 × 5 = 10`
2. `2 × 0 = 0`
3. `2 × 1 = 2`
4. `2 × (-2) = -4`

Hasil: `[[10, 0], [2, -4]]`

---

### Implementasi dengan List Python

```python
# Membuat matriks 2x2
var_mat = [[5, 0],
           [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)

"""
Output:
[[10, 0], [2, -4]]
"""
```

Penjelasan kode:

1. Deklarasi `var_mat` dengan matriks 2×2 yang diinginkan
2. Deklarasi `def_mat` sebagai matriks default berukuran sama (nilai awal `0`)
3. Perulangan pertama (`i`) — mengiterasi baris (2 list di dalam `var_mat`)
4. Perulangan kedua (`j`) — mengiterasi kolom (2 elemen per list)
5. Setiap iterasi: `def_mat[i][j] = var_mat[i][j] * 2` — perbarui elemen dengan hasil perkalian
6. Proses berulang hingga semua elemen `def_mat` diperbarui

---

### Implementasi dengan NumPy

Cara yang lebih efektif menggunakan library NumPy:

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

Dengan NumPy, tidak perlu nested for — cukup kalikan matriks langsung dengan konstanta:

```python
result = var_mat * 2
```

Anda masih bisa bereksplorasi dengan operasi matriks lainnya seperti transpose, inverse, dan sebagainya menggunakan NumPy.
