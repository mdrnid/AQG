# Pengertian Ekspresi

Setelah melewati pembahasan tipe data yang sangat komprehensif, Anda memiliki bekal cukup untuk membuat program dan belajar pada modul-modul berikutnya.

Salah satunya adalah materi ekspresi. Data yang Anda simpan pada suatu variabel umumnya akan dioperasikan untuk menghasilkan suatu nilai sesuai keinginan. Masih ingat ekspresi pada matematika? Ekspresi pada matematika adalah kombinasi dari simbol-simbol matematika seperti angka, variabel, dan operasi matematika.

![Contoh ekspresi matematika 4x - 7](assets/ekspresi-matematika.jpeg)

Pada gambar di atas, `4x-7` merupakan ekspresi, sedangkan `4x`, `7`, dan `5` merupakan suku bilangan.

**Ekspresi pada pemrograman** merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.

---

## Struktur Ekspresi

Struktur umum ekspresi yang sering dijumpai adalah:

```
<operan1> <operator> <operan2>
```

Ini merupakan struktur **ekspresi biner** — ekspresi yang menggunakan dua operan. Penjelasan komponennya:

- **Operan** — dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
- **Operator** — fungsi standar dalam bahasa pemrograman untuk melakukan perhitungan dasar seperti aritmetika, logika, dan relasional. Contoh: `+`, `-`, `*`, `%`, dan sebagainya.

---

## Contoh Ekspresi dalam Python

```python
x = 10
y = 2
result = x - y

print(result)

"""
Output:
8
"""
```

Ekspresi juga dapat digunakan untuk operasi pada list, seperti **penggabungan** dan **replikasi**.

**Penggabungan list** menggunakan operator `+`:

```python
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

"""
Output:
[2, 4, 6, 8, 'P', 'Y', 'T', 'H', 'O', 'N']
"""
```

**Replikasi list** menggunakan operator `*`:

```python
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)

"""
Output:
['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']
"""
```

Memahami ekspresi adalah dasar dalam pemrograman untuk melakukan semua perhitungan dan manipulasi data. Sekarang, mari kita pelajari lebih dalam mengenai berbagai jenis ekspresi.
