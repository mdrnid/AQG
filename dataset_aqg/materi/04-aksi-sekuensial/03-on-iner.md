# One-liner

Selain membangun kode berdasarkan bloknya, Anda juga dapat membuat sebuah kode hanya dalam satu baris — konsep ini dikenal sebagai **one-liner**.

One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda membuat kode hanya dalam satu baris. Ini adalah salah satu keunggulan Python yang sulit diimplementasikan di beberapa bahasa pemrograman lain.

Tujuan dari one-liner adalah membuat kode yang **singkat dan jelas**. Perlu diingat bahwa tidak semua kode blok dapat dijadikan one-liner — seperti deklarasi fungsi, modul, dan kelas.

---

## Contoh: Menukar Dua Variabel

### Cara Konvensional

```python
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

"""
Output:
Setelah pertukaran:
x = 2
y = 1
"""
```

Penjelasan langkah per langkah:

1. Inisialisasi `x = 1` dan `y = 2`.
2. Simpan nilai `x` ke variabel bantuan `temp` → `temp = 1`.
3. Isi `x` dengan nilai `y` → `x = 2`.
4. Isi `y` dengan nilai `temp` → `y = 1`.
5. Tampilkan hasil pertukaran.

Analogi dengan gelas dan kelereng:

![Ilustrasi tiga gelas kosong untuk analogi pertukaran variabel](assets/analogi-gelas-kosong.jpeg)

![Animasi proses pertukaran kelereng antar gelas](assets/analogi-pertukaran-kelereng.gif)

Langkah-langkahnya:

1. Gelas `x` diisi 1 kelereng, gelas `y` diisi 2 kelereng, gelas `temp` kosong.
2. Kelereng dari gelas `x` dipindahkan ke gelas `temp` → `temp = 1`, `x` kosong.
3. Kelereng dari gelas `y` dipindahkan ke gelas `x` → `x = 2`, `y` kosong.
4. Kelereng dari gelas `temp` dipindahkan ke gelas `y` → `y = 1`.

---

### Cara One-liner

```python
x = 1
y = 2

x, y = y, x    # One-liner

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)

"""
Output:
Setelah pertukaran:
x = 2
y = 1
"""
```

![Ilustrasi one-liner pertukaran variabel](assets/analogi-one-liner.jpeg)

Dengan satu baris `x, y = y, x`, Python secara bersamaan menginisialisasi ulang `x` dengan nilai `y` dan `y` dengan nilai `x` — tanpa memerlukan variabel bantuan `temp`.

---

Ini hanyalah salah satu contoh penerapan one-liner. Ke depannya, banyak materi Python yang memiliki versi one-liner-nya masing-masing.
