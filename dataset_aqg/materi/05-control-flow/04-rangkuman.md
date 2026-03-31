# Rangkuman: Control Flow

Kita sudah berada di penghujung materi Control Flow. Sampai sejauh ini, Anda telah memiliki pemahaman mengenai berbagai jenis kontrol dalam pemrograman. Mari kita rangkum secara saksama.

---

## Percabangan dan Ternary Operators

### Percabangan

Kode program dapat berjalan berdasarkan kondisi tertentu menggunakan instruksi "Jika-maka":

- **`if`** — mengecek kondisi; jika `True`, blok kode di dalamnya dieksekusi

  ![Struktur if statement](assets/struktur-if.jpeg)

- **`else`** — jalan keluar terakhir ketika kondisi `if` bernilai `False`

  ![Struktur if-else](assets/struktur-if-else.jpeg)

- **`elif`** — kondisi tambahan setelah `if`, dapat digunakan lebih dari satu kali

  ![Struktur if-elif-else](assets/struktur-if-elif-else.jpeg)

> Anda juga dapat menggabungkan operator `and` atau `or` dalam kondisi percabangan.

### Ternary Operators

Versi one-liner dari `if-else`:

- **Ternary biasa** — `<nilai_jika_true> if <kondisi> else <nilai_jika_false>`

  ![Struktur ternary operator](assets/struktur-ternary.jpeg)

- **Ternary tuples** — menggunakan indeks tuple; indeks `0` untuk `False`, indeks `1` untuk `True`

  ![Struktur ternary tuples](assets/struktur-ternary-tuples.jpeg)

---

## Perulangan

### For

Perulangan **definite iteration** — jumlah pengulangan ditentukan secara eksplisit.

![Format perulangan for](assets/format-for.jpeg)

### While

Perulangan **indefinite iteration** — berhenti ketika kondisi tertentu terpenuhi.

![Format perulangan while](assets/format-while.jpeg)

> Hindari **infinite loop** — pastikan selalu ada increment atau kondisi yang akan terpenuhi:

```python
counter = 1
while counter <= 5:
    print(counter)
    # Tanpa increment → infinite loop!
```

### For Bersarang (Nested Loop)

Perulangan dalam perulangan.

![Format nested loop](assets/format-nested-loop.jpeg)

### Kontrol Perulangan

- **`break`** — menghentikan perulangan sepenuhnya
- **`continue`** — melewati iterasi saat ini dan lanjut ke iterasi berikutnya
- **`else` setelah `for`** — dieksekusi jika `break` tidak pernah terjadi (berguna untuk pencarian)
- **`else` setelah `while`** — dieksekusi ketika kondisi `while` menjadi `False`
- **`pass`** — placeholder ketika tidak ada tindakan yang perlu dilakukan

### List Comprehension

Cara ringkas menghasilkan list baru dari list atau iterable yang sudah ada:

![Sintaks list comprehension](assets/sintaks-list-comprehension.jpeg)

- `new_list` — variabel yang dideklarasikan
- `expression` — ekspresi yang dijalankan setiap iterasi
- `for_loop_one_or_more_conditions` — perulangan `for` yang didefinisikan

---

## Penanganan Kesalahan (Error Handling)

Dua jenis kesalahan dalam Python:

- **Kesalahan sintaks** (*syntax errors*) — terjadi sebelum program berjalan; Python tidak mengerti perintah Anda

  ![Struktur pesan syntax error](assets/struktur-syntax-error.jpeg)

- **Pengecualian** (*exceptions*) — terjadi saat program berjalan; Python mengerti perintah tetapi gagal mengeksekusinya

  ![Struktur pesan exception](assets/struktur-exception.jpeg)

### Penanganan Pengecualian (try-except)

Gunakan `try-except` untuk menangani pengecualian:

![Struktur lengkap try-except-else-finally](assets/struktur-try-except.jpeg)

- `try` — blok kode yang mungkin menghasilkan pengecualian
- `except` — dieksekusi jika pengecualian terjadi
- `else` — dieksekusi jika tidak ada pengecualian
- `finally` — selalu dieksekusi

### Raise Exception

Membangkitkan pengecualian secara disengaja untuk membatasi program dengan kondisi tertentu:

```python
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i + 1)

"""
Output:
ValueError: Bilangan negatif tidak diperbolehkan
"""
```
