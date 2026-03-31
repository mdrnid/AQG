# Penanganan Kesalahan (Error Handling)

Saat membuat program, Anda akan menemui setidaknya dua jenis kesalahan:

1. **Kesalahan sintaks** (*syntax errors* / *parsing errors*)
2. **Pengecualian** (*exceptions* / *runtime errors*)

---

## Kesalahan Sintaks (Syntax Errors)

Kesalahan sintaks terjadi ketika Python tidak mengerti perintah Anda — pesan kesalahan muncul **sebelum** program berjalan.

**Contoh IndentationError:**

```python
if 9 > 10:
print("Hello World!")

"""
Output:
File "/home/glot/main.py", line 2
    print("Hello World!")
    ^
IndentationError: expected an indented block
"""
```

**Contoh SyntaxError:**

```python
i = 1
while i < 3
    print("Dicoding")
    i += 1

"""
Output:
File "/home/glot/main.py", line 2
    while i<3
             ^
SyntaxError: invalid syntax
"""
```

Kesalahan di atas terjadi karena tidak ada tanda titik dua `:` setelah `while`.

### Struktur Pesan Kesalahan Sintaks

![Struktur pesan kesalahan sintaks](assets/struktur-syntax-error.jpeg)

- `<nama file>` — file Python yang dieksekusi
- `<nomor baris>` — nomor baris kode yang mengalami kesalahan
- `<baris kode>` — kode yang mengalami kesalahan
- `<tipe kesalahan>` — contoh: `SyntaxError`, `IndentationError`
- `<pesan kesalahan>` — detail kesalahan, contoh: `invalid syntax`, `expected an indented block`

---

## Pengecualian (Exceptions)

Pengecualian terjadi ketika Python mengerti perintah Anda, tetapi mendapat masalah saat mengeksekusinya — terjadi **saat program berjalan**.

**Contoh NameError:**

```python
print(angka)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 1, in <module>
    print(angka)
NameError: name 'angka' is not defined
"""
```

**Contoh TypeError:**

```python
bukan_angka = '1'
bukan_angka + 2

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
"""
```

### Struktur Pesan Pengecualian

![Struktur pesan pengecualian](assets/struktur-exception.jpeg)

Perbedaan utama dari syntax error: pengecualian menampilkan pesan `Traceback (most recent call last)` yang menyediakan "jejak" jalur eksekusi program sebelum mencapai titik error.

---

## Penanganan Pengecualian (try-except)

Gunakan pernyataan `try-except` untuk menangani pengecualian:

```python
z = 0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

"""
Output:
Anda tidak bisa membagi angka dengan nilai nol.
"""
```

### Struktur Lengkap try-except

![Struktur lengkap try-except-else-finally](assets/struktur-try-except.jpeg)

```python
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""
```

Penjelasan setiap blok:

- `try` — blok kode yang mungkin menghasilkan pengecualian
- `except` — dieksekusi jika pengecualian terjadi
- `else` — dieksekusi jika **tidak ada** pengecualian
- `finally` — selalu dieksekusi, baik ada pengecualian maupun tidak

---

## Raise Exception

Digunakan untuk membangkitkan pengecualian secara **disengaja** — biasanya untuk membatasi program dengan kondisi tertentu. `raise` umumnya digunakan bersama `if-else`.

```python
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i + 1)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 3, in <module>
    raise ValueError("Bilangan negatif tidak diperbolehkan")
ValueError: Bilangan negatif tidak diperbolehkan
"""
```
