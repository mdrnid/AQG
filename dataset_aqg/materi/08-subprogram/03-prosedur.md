# Prosedur

## Fundamental Prosedur

Dalam KBBI, kata **prosedur** memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. Dalam pemrograman, prosedur adalah pengelompokan instruksi-instruksi yang sering dipakai dalam program.

Berbeda dengan fungsi, prosedur:

- Tidak mengharuskan adanya parameter input atau output
- Dapat dipandang sebagai **fungsi yang tidak menghasilkan nilai**
- Dalam Python, didefinisikan dengan `return` tanpa ekspresi atau nilai di akhir fungsi

![Kerangka dasar prosedur pada Python](assets/kerangka-prosedur.jpeg)

---

## Mendefinisikan dan Memanggil Prosedur

Contoh prosedur sederhana:

```python
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
```

Perhatikan bahwa tidak ada `return` dan tidak ada return value. Kita juga bisa menambahkan `return` tanpa nilai:

```python
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return
```

Untuk memanggil prosedur, caranya sama seperti memanggil fungsi:

```python
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")

"""
Output:
Halo Dicoding Indonesia, Selamat Datang!
"""
```

Walaupun tidak ada `return` atau return value, program tetap menampilkan output karena kita langsung menggunakan `print()` di dalam prosedur.

---

## Prosedur Tanpa Parameter

Prosedur juga bisa dibuat tanpa parameter input:

```python
def greeting():
    print("Halo Selamat Datang!")

greeting()

"""
Output:
Halo Selamat Datang!
"""
```

Ketika dipanggil, program langsung menjalankan body prosedur dan menampilkan teks ke layar.
