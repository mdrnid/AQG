# Rangkuman: Berinteraksi dengan Data

Kita sudah berada di penghujung materi Berinteraksi dengan Data. Sampai sini, Anda telah memiliki pemahaman mendasar mengenai data dalam Python. Mari kita rangkum secara saksama.

---

## Abstraksi Data

**Abstraksi data** merupakan kemampuan untuk mengerti konteks dan merepresentasikannya menjadi bentuk lain sesuai dengan konteks masalahnya.

Ketika menuliskan data dalam pemrograman, komputer tidak akan mengetahui data yang dimaksud hingga Anda mendeklarasikan **tipe datanya**.

---

## Data Typing

### Deklarasi dan Inisialisasi

**Deklarasi** merujuk pada pembuatan variabel dengan menentukan tipe data dan nama variabelnya (contoh dalam C/C++):

```c
int age;
float salary;
```

**Inisialisasi** merujuk pada pemberian nilai awal pada variabel yang telah dideklarasikan (contoh dalam C/C++):

```c
int age = 17;
float salary = 5000000;
```

Dalam Python, Anda tidak perlu mendeklarasikan tipe data — langsung inisialisasi saja:

```on
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

"""
Output:
<class 'int'>
<class 'float'>
"""
```

---

## Tipe Data

### Tipe Data Primitif

Tipe data primitif menyimpan *single value*. Berikut jenisnya:

**Numbers:**

| Jenis | Deskripsi | Contoh |
|-------|-----------|--------|
| `int` | Bilangan bulat positif atau negatif, tanpa desimal | `1`, `-20`, `999`, `0` |
| `float` | Bilangan riil, dapat berupa bilangan bulat atau desimal | `3.14`, `1`, `4.01E+1` |
| `complex` | Bilangan kompleks (tidak digunakan di kelas ini) | `1+2j` |

**Boolean** — hanya bernilai `True` atau `False`. Nilai yang dianggap `False`:

- `None` dan `False`
- Angka nol: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`
- Urutan/koleksi kosong: `""`, `()`, `{}`, `set()`, `range(0)`

**String** — karakter yang berurutan, diapit single quote (`''`) atau double quote (`""`):

```python
"Dicoding Indonesia"
```

---

### Tipe Data Collection

Tipe data collection menyimpan satu atau lebih data primitif sebagai satu kelompok:

- **List** — kumpulan data terurut, menggunakan `[]`:
  ```python
  x = [1, 2.2, "Dicoding"]
  ```

- **Tuple** — seperti list tapi immutable, menggunakan `()`:
  ```python
  x = (1, "Dicoding", 1+3j)
  ```

- **Set** — kumpulan item unik tanpa urutan, menggunakan `{}`:
  ```python
  x = {1, 2, 3, 7, 13}
  ```

- **Dictionary** — pasangan key-value, menggunakan `{}` dengan pemisah `:`:
  ```python
  x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
  ```

### Konversi antara Tipe Data

| Konversi | Fungsi |
|----------|--------|
| Integer ke float | `float()` |
| Float ke integer | `int()` |
| Dari/ke string | `str()`, `float()`, `int()` |

---

## Transformasi Angka, Karakter, dan String

### Mengubah Huruf Besar/Kecil
- `upper()` — mengubah ke UPPERCASE
- `lower()` — mengubah ke lowercase

### Awalan dan Akhiran
- `rstrip()` — hapus whitespace di kanan
- `lstrip()` — hapus whitespace di kiri
- `strip()` — hapus whitespace di kedua sisi
- `startswith()` — cek awalan string
- `endswith()` — cek akhiran string

### Memisah dan Menggabung String
- `join()` — menggabungkan elemen list menjadi string
- `split()` — memisahkan string menjadi list

### Mengganti Elemen String
- `replace()` — mengganti substring dengan substring lain (case-sensitive)

### Pengecekan String
- `isupper()`, `islower()`, `isalpha()`, `isalnum()`, `isdecimal()`, `isspace()`, `istitle()`

### Formatting pada String
- `zfill()` — tambah `0` di depan hingga panjang tertentu
- `rjust()` — rata kanan
- `ljust()` — rata kiri
- `center()` — rata tengah

### String Literals dan Escape Character

Gunakan escape character untuk memasukkan karakter khusus ke dalam string:

| Escape Character | Deskripsi |
|-----------------|-----------|
| `\'` | Single quote |
| `\"` | Double quote |
| `\t` | Tab |
| `\n` | Newline |
| `\\` | Backslash |

### Raw String

Mencetak string apa adanya tanpa memproses escape character. Tambahkan `r` sebelum string:

```python
print(r'Dicoding\tIndonesia')

"""
Output:
Dicoding\tIndonesia
"""
```

---

## Operasi pada List, Set, dan String

### `len()`

```python
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(len(contoh_list))

"""
Output:
9
"""
```

### `min()` dan `max()`

```python
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

"""
Output:
5
96
"""
```

### `count()`

```python
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

"""
Output:
3
"""
```

### Operator `in` dan `not in`

```python
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

"""
Output:
True
False
False
True
"""
```

### Multiple Variable Assignment

```python
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)

"""
Output:
['shirt', 'white', 'L']
"""
```

### `sort()`

```python
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['helikopter', 'mobil', 'motor', 'pesawat']
"""
```


```