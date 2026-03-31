# Fundamental Array

Python tidak memiliki tipe data array seperti yang umum digunakan dalam bahasa pemrograman lain. Sebaliknya, Python memiliki tipe data **list** yang mirip, tetapi tidak sama dengan array.

Perbedaan utamanya:

- **Array** — semua elemen harus bertipe data yang sama
- **List** — elemen dapat bertipe data berbeda-beda

![Perbandingan array dan list](assets/perbandingan-array-list.jpeg)

---

## Struktur Data

**Struktur data** adalah cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien. Dengan adanya struktur data, setiap data yang disimpan memiliki hubungan satu sama lain.

Tipe data yang telah Anda pelajari sebelumnya — baik primitif maupun collection — semuanya termasuk jenis struktur data Python.

![Jenis-jenis struktur data Python](assets/jenis-struktur-data.jpeg)

Array dan list merupakan hal yang berbeda dalam Python. Namun, **Anda bisa menggunakan list sebagai array** dalam Python:

```python
x = [1, 2, 3, 4, 5]
print(x)

"""
Output:
[1, 2, 3, 4, 5]
"""
```

Jika ingin menggunakan array secara eksplisit, gunakan modul `array` bawaan Python:

```python
import array

x = array.array("i", [1, 2, 3, 4, 5])
print(x)
print(type(x))

"""
Output:
array('i', [1, 2, 3, 4, 5])
<class 'array.array'>
"""
```

> **Catatan:** Kelas ini akan menggunakan `list` sebagai `array`. Ke depannya, kata "list" dalam kelas ini juga dapat diartikan sebagai "array".

---

## Array sebagai Struktur Data Linear

List dapat dibagi menjadi struktur data **linear** dan **non-linear**:

![Pembagian struktur data linear dan non-linear](assets/struktur-data-linear-nonlinear.jpeg)

- **Linear** — elemen disusun secara berurutan
- **Non-linear** — elemen tidak disusun secara linear

Array adalah salah satu jenis struktur data linear — terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan.

![Ilustrasi struktur array](assets/ilustrasi-struktur-array.jpeg)

Komponen array:

- **Indeks** — posisi untuk mengidentifikasi elemen, selalu dimulai dari `0`
- **Elemen** — nilai yang berada dalam suatu indeks
- **Array length** — panjang atau jumlah elemen dalam array

---

## Mengapa Array Berguna?

Tanpa array, menyimpan banyak nilai memerlukan banyak variabel:

```python
nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
# ... hingga 10 variabel
```

Dengan array (list), semua nilai dapat disimpan dalam satu variabel:

```python
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])

"""
Output:
[90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
90
"""
```

![Ilustrasi penyimpanan array nilai siswa](assets/ilustrasi-array-nilai-siswa.jpeg)
