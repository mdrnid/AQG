# Rangkuman: Array dan Pemrosesannya

Kita sudah berada di penghujung materi Array dan Pemrosesannya. Sampai sini, Anda telah mempelajari salah satu struktur data, yakni array. Mari kita rangkum secara saksama.

---

## Fundamental Array

**Array** adalah salah satu jenis struktur data linear — terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan.

![Struktur array](assets/struktur-array-rangkuman.jpeg)

Komponen array:

- **Indeks** — posisi untuk mengidentifikasi elemen, selalu dimulai dari `0`
- **Elemen** — nilai yang berada dalam suatu indeks
- **Array length** — panjang atau jumlah elemen dalam array

Dalam Python, ada dua cara menggunakan array:

**Menggunakan List:**

```python
x = [1, 2, 3, 4, 5]
print(x)

"""
Output:
[1, 2, 3, 4, 5]
"""
```

**Menggunakan Library `array`:**

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

---

## Implementasi Array dengan Python

Ada dua cara mendeklarasikan array menggunakan list:

### Mendefinisikan Isi Array

Digunakan jika nilai sudah diketahui:

![Struktur deklarasi array dengan isi langsung](assets/struktur-deklarasi-isi-rangkuman.jpeg)

- `<nama-var>` — nama variabel array
- `<val0>`, `<val1>`, ..., `<valn-1>` — elemen-elemen array terurut dari indeks `0` hingga `n-1`

### Mendefinisikan Nilai Default

Digunakan jika nilai belum diketahui — menggunakan list comprehension:

![Struktur deklarasi array dengan nilai default](assets/struktur-deklarasi-default-rangkuman.jpeg)

- `<nama-var>` — variabel yang dideklarasikan
- `<default-val>` — nilai default (di luar range yang disepakati)
- `<n>` — ukuran panjang array

---

## Pemrosesan Sekuensial pada Array

**Pemrosesan sekuensial** adalah pemrosesan setiap elemen array dari indeks terkecil hingga terbesar, umumnya menggunakan perulangan.

Hal-hal yang perlu diperhatikan:

1. Setiap elemen diakses langsung melalui indeksnya (*indexing*)
2. Elemen pertama selalu dimulai dari indeks `0`
3. Elemen selanjutnya dicapai melalui suksesor indeks
4. Kondisi berhenti saat indeks terbesar tercapai
5. Array tidak boleh kosong — minimal satu elemen

Contoh penerapan pemrosesan sekuensial:

- Mengisi array secara sekuensial
- Menghitung nilai rata-rata elemen array
- Mengalikan elemen array dengan suatu nilai
- Mencari nilai terbesar atau terkecil pada array
- Mencari indeks letak suatu nilai ditemukan pertama kali
