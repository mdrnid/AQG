# Fungsi

## Fungsi dalam Matematika

Fungsi dalam pemrograman didasari oleh konsep pemetaan dan fungsi dalam matematika. Fungsi pada matematika merupakan pemetaan antara dua himpunan nilai — **domain** (input) dan **range** (output).

![Ilustrasi fungsi sebagai mesin input-output](assets/fungsi-mesin.jpeg)

Notasi fungsi yang umum dijumpai:

![Notasi fungsi matematika f(x) = 2x](assets/notasi-fungsi.jpeg)

- `f` = nama fungsi
- `x` = input
- `2x` = output yang dihasilkan

Contoh: fungsi `f(x) = 2x` mengalikan setiap elemen domain dengan 2:

![Ilustrasi pemetaan domain ke range](assets/pemetaan-domain-range.jpeg)

---

## Fungsi dalam Pemrograman

Fungsi dalam pemrograman dapat diumpamakan seperti **black box**:

![Ilustrasi fungsi sebagai black box](assets/fungsi-black-box.jpeg)

Kita tidak perlu tahu proses di dalam kotak — cukup fokus pada input (domain) dan output (range). Contohnya fungsi `print()` yang sudah kita kenal:

![Ilustrasi print() sebagai black box](assets/print-black-box.jpeg)

**Fungsi dalam pemrograman** adalah blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil. Dalam Python, fungsi terbagi menjadi dua jenis:

- **Built-in Functions** — fungsi bawaan yang sudah terintegrasi dengan Python, tidak perlu mengimpor modul tambahan. Contoh: `print()`, `len()`, `type()`, `range()`
- **User-defined Functions** — fungsi yang kita definisikan sendiri untuk tugas spesifik tertentu. Contoh: `mencari_luas_persegi_panjang()`

---

## Library, Modul, dan Package

Jika ingin menggunakan fungsi di luar built-in functions, Anda bisa mengimpor sebuah library. Berikut ringkasannya:

| Nama | Definisi | Contoh |
|------|----------|--------|
| **Fungsi** | Blok kode yang dapat digunakan kembali | `print()`, `len()`, `mencari_luas_persegi_panjang()` |
| **Built-in functions** | Fungsi bawaan Python | `print()`, `len()`, `range()` |
| **User-defined functions** | Fungsi yang didefinisikan sendiri | `mencari_luas_persegi_panjang()` |
| **Modul** | File berisi kode Python (fungsi, kelas, dll.) | `math`, `main.py`, `var.py` |
| **Package** | Direktori berisi satu atau lebih modul terkait | NumPy, Pandas |
| **Library** | Koleksi modul dan paket yang saling terkait | Matplotlib, TensorFlow, Beautiful Soup |

Library Python terbagi dua:

- **Python Standard Library** — terpasang otomatis saat instalasi Python. Contoh: `os`, `datetime`, `re`
- **External Library** — dikembangkan pihak luar, perlu diimpor. Contoh: TensorFlow

---

## Kegunaan Fungsi

Beberapa kegunaan fungsi dalam pemrograman:

**1. Program dapat dipecah menjadi bagian yang lebih kecil**

![Ilustrasi pemecahan program menjadi fungsi-fungsi kecil](assets/fungsi-pecah-program.png)

**2. Penggunaan ulang kode alih-alih menulis ulang**

![Ilustrasi reuse kode dengan fungsi](assets/fungsi-reuse.png)

**3. Setiap fungsi bersifat independen dan dapat diuji secara terpisah**

![Ilustrasi fungsi independen](assets/fungsi-independen.png)

---

## Mendefinisikan Fungsi dalam Python

Secara umum, fungsi terdiri dari **header**, **body**, dan **return**:

![Struktur fungsi Python](assets/struktur-fungsi.jpeg)

- **Function header** — memberi tahu Python bahwa kita mulai mendefinisikan fungsi
- **Function body** — blok kode yang diindentasi, menentukan apa yang dilakukan fungsi
- **Function return** — mengembalikan nilai atau hasil eksekusi fungsi

### Membuat Fungsi

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang
```

![Penjelasan elemen fungsi](assets/elemen-fungsi.jpeg)

Elemen fungsi:

- `def` — keyword untuk membuat fungsi
- `mencari_luas_persegi_panjang` — nama fungsi
- `panjang, lebar` — parameter untuk menyimpan nilai input
- `:` — menandakan awal blok kode fungsi
- Body fungsi — kode yang dieksekusi
- `return` — mengembalikan nilai hasil eksekusi

### Memanggil Fungsi

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

"""
Output:
50
"""
```

![Struktur pemanggil fungsi](assets/struktur-pemanggil-fungsi.jpeg)

Elemen pemanggil fungsi:

- **Nama fungsi** — nama fungsi yang ingin digunakan, diikuti `()`
- **Argumen** — nilai yang diberikan kepada fungsi, disimpan dalam parameter

### Docstring

Untuk membuat fungsi lebih mudah dipahami, tambahkan **docstring** — dokumentasi fungsi menggunakan triple double quote `"""` tepat di bawah `def`:

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)
```

Elemen docstring:

- **Deskripsi** — tujuan fungsi
- **Args** — argumen yang diterima beserta tipe datanya
- **Returns** — nilai yang dikembalikan beserta tipe datanya

---

## Argumen dan Parameter

**Parameter** adalah variabel dalam definisi fungsi. **Argumen** adalah nilai yang diberikan saat memanggil fungsi.

![Ilustrasi parameter vs argumen](assets/parameter-vs-argumen.jpeg)

![Animasi keterkaitan argumen dan parameter](assets/animasi-argumen-parameter.gif)

### Jenis Argumen

**Keyword Argument** — menyebutkan nama parameter secara eksplisit:

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

# Urutan tidak perlu dipikirkan
persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)
print(persegi_panjang_pertama)

"""
Output:
50
"""
```

**Positional Argument** — tidak menyebutkan nama parameter, harus mengikuti urutan:

```python
persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

"""
Output:
50
"""
```

### Jenis Parameter

**1. Positional-or-Keyword** (default) — dapat dipanggil dengan positional maupun keyword:

```python
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

"""
Output:
Halo, Dicoding! Selamat pagi!
Halo, Dicoding! Selamat sore!
"""
```

**2. Positional-Only** — hanya bisa dipanggil dengan positional argument, ditandai `/`:

```python
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))

"""
Output:
58
"""
```

**3. Keyword-Only** — hanya bisa dipanggil dengan keyword argument, ditandai `*`:

```python
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!", nama="Dicoding"))

"""
Output:
Halo, Dicoding! Selamat sore!
"""
```

**4. Var-Positional (`*args`)** — menampung jumlah argumen posisi yang bervariasi:

```python
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

"""
Output:
<class 'tuple'>
6
"""
```

**5. Var-Keyword (`**kwargs`)** — menampung jumlah keyword argument yang bervariasi:

```python
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

"""
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""
```

---

## Fungsi Anonim (Lambda Expression)

Fungsi anonim adalah versi one-liner dari fungsi — dibuat tanpa keyword `def`.

![Struktur lambda expression](assets/struktur-lambda.jpeg)

![Animasi perbandingan def dan lambda](assets/animasi-def-vs-lambda.gif)

```python
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
print(mencari_luas_persegi_panjang(5, 10))

"""
Output:
50
"""
```

Lambda dapat menerima argumen dalam jumlah berapa pun, tetapi hanya mengembalikan **satu nilai ekspresi**.

---

## Variabel Global dan Lokal

### Variabel Global

Didefinisikan di luar fungsi dan dapat diakses dari seluruh bagian program:

```python
a = 10

def add(b):
    result = a + b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

"""
Output:
30
"""
```

### Variabel Lokal

Didefinisikan dalam fungsi dan hanya dapat diakses dari dalam fungsi tersebut:

```python
def add(a, b):
    lokal_var = 5
    result = a + b - lokal_var
    return result

bilanganPertama = add(10, 20)
print(bilanganPertama)

"""
Output:
25
"""
```

> Mencoba mengakses `lokal_var` di luar fungsi akan menghasilkan `NameError: name 'lokal_var' is not defined`.

---

## Menulis Modul pada Python

Setiap file berekstensi `.py` dapat direferensikan sebagai **modul**. Anda bisa mengimpor fungsi dari satu file ke file lain.

**Langkah 1** — Buat file `hello.py` berisi fungsi:

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang
```

**Langkah 2** — Buat file `main.py` di folder yang sama:

![Ilustrasi dua file dalam satu folder](assets/dua-file-satu-folder.png)

```python
import hello

persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)
```

**Langkah 3** — Jalankan `main.py` dari terminal:

```bash
python main.py
```

![Tampilan output di terminal](assets/output-terminal.png)

**Langkah 4** — Tambahkan variabel di `hello.py`:

```python
nama = "Dicoding Indonesia"
```

**Langkah 5** — Akses variabel dari `main.py`:

```python
print(hello.nama)
```

### Impor Spesifik

Anda juga bisa mengimpor fungsi atau variabel secara spesifik:

```python
from hello import mencari_luas_persegi_panjang, nama

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

print(nama)
```

Dengan cara ini, tidak perlu menyebutkan nama modul (`hello.`) setiap kali menggunakan fungsi atau variabel yang diimpor.
