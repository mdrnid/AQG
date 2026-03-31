# Rangkuman: Subprogram

Kita sudah berada di penghujung materi Subprogram. Sampai sejauh ini, Anda diharapkan paham untuk mengimplementasikan subprogram dalam setiap program yang Anda bangun. Mari kita rangkum secara saksama.

---

## Definisi Subprogram

**Subprogram** adalah serangkaian instruksi yang dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Ada dua jenis:

- **Fungsi** — blok kode yang menerima input, melakukan pemrosesan, dan mengembalikan output dengan tipe data eksplisit
- **Prosedur** — deretan instruksi dengan keadaan awal dan akhir yang jelas, cakupan kecil dan terbatas

---

## Fungsi

Fungsi dalam pemrograman didasari oleh konsep pemetaan dalam matematika — memiliki input (domain) dan output (range).

![Notasi fungsi matematika](assets/notasi-fungsi-rangkuman.jpeg)

Dalam pemrograman, fungsi dapat diumpamakan seperti **black box**:

![Ilustrasi fungsi sebagai black box](assets/black-box-rangkuman.jpeg)

### Jenis Fungsi

- **Built-in Functions** — fungsi bawaan Python (`print()`, `len()`, `range()`, dll.)
- **User-defined Functions** — fungsi yang didefinisikan sendiri

### Library

| Nama | Definisi | Contoh |
|------|----------|--------|
| **Fungsi** | Blok kode yang dapat digunakan kembali | `print()`, `len()`, `mencari_luas_persegi_panjang()` |
| **Built-in functions** | Fungsi bawaan Python | `print()`, `len()`, `range()` |
| **User-defined functions** | Fungsi yang didefinisikan sendiri | `mencari_luas_persegi_panjang()` |
| **Modul** | File berisi kode Python | `math`, `main.py`, `var.py` |
| **Package** | Direktori berisi modul terkait | NumPy, Pandas |
| **Library** | Koleksi modul dan paket | Matplotlib, TensorFlow, Beautiful Soup |

Library Python terbagi dua: **Python Standard Library** (terpasang otomatis) dan **External Library** (perlu diimpor).

### Struktur Fungsi

![Struktur fungsi Python](assets/struktur-fungsi-rangkuman.jpeg)

Elemen fungsi:

1. `def` — keyword untuk membuat fungsi
2. Nama fungsi
3. Parameter fungsi
4. `:` — menandakan awal blok kode
5. Body fungsi — kode yang dieksekusi
6. `return` — mengembalikan nilai hasil eksekusi

### Docstring

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

### Jenis Argumen dan Parameter

**Argumen:**

- **Keyword Argument** — menyebutkan nama parameter secara eksplisit: `mencari_luas_persegi_panjang(panjang=5, lebar=10)`
- **Positional Argument** — tidak menyebutkan nama, mengikuti urutan: `mencari_luas_persegi_panjang(5, 10)`

**Parameter:**

```python
# Positional-or-Keyword (default)
def greeting(nama, pesan): ...

# Positional-Only (sintaks /)
def penjumlahan(a, b, /): ...

# Keyword-Only (sintaks *)
def greeting(*, nama, pesan): ...

# Var-Positional (*args)
def hitung_total(*args): ...

# Var-Keyword (**kwargs)
def cetak_info(**kwargs): ...
```

### Fungsi Anonim (Lambda)

![Animasi perbandingan def dan lambda](assets/animasi-def-vs-lambda-rangkuman.gif)

```python
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
```

### Impor Modul

```python
# Impor seluruh modul
import hello

# Impor spesifik
from hello import mencari_luas_persegi_panjang, nama
```

---

## Prosedur

Prosedur adalah fungsi Python yang **tidak mengembalikan nilai**. Didefinisikan tanpa `return` atau dengan `return` tanpa nilai.

![Kerangka dasar prosedur](assets/kerangka-prosedur-rangkuman.jpeg)

```python
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")
```

Prosedur juga bisa dibuat tanpa parameter:

```python
def greeting():
    print("Halo Selamat Datang!")

greeting()
```
