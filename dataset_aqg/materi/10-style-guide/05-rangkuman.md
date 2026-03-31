# Rangkuman: Style Guide pada Python

Kita sudah berada di penghujung materi style guide pada Python. Sampai sejauh ini, Anda diharapkan paham cara membangun kode Python yang lebih baik dan benar sesuai panduan yang telah diberikan oleh Python melalui PEP8. Mari kita rangkum secara saksama.

---

## Pengecekan Style Guide PEP8

Saat membangun program pada Python, seringkali kode yang dibuat cukup berantakan sehingga kita perlu mengeceknya dengan mengacu pada panduan yang telah diberikan oleh Python, yaitu **PEP8**.

**PEP** atau *Python Enhancement Proposals* adalah panduan yang telah menjadi acuan untuk perkembangan Python. Panduan **PEP8** berjudul *"Style Guide for Python Code"* bertujuan agar kode Anda lebih mudah dibaca dan dipahami oleh programmer lain serta menghindari kemungkinan kesalahan yang akan muncul.

---

## Lint

Lint atau linting adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut **linter**.

Berikut adalah tiga jenis aplikasi linter:

### Pycodestyle

Aplikasi open source (berlisensi MIT/Expat) untuk membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8.

```bash
pip install pycodestyle
```

### Pylint

Aplikasi open source (berlisensi GPL v2) untuk melakukan analisis kode Python, mengecek kesalahan (error) pemrograman, memaksakan standar penulisan kode, serta memberikan saran untuk refactoring sederhana.

```bash
pip install pylint
```

### Flake8

Aplikasi open source (berlisensi MIT) yang membungkus sejumlah kemampuan aplikasi lain, seperti `pycodestyle`, `pyflakes`, dan fitur lainnya.

```bash
pip install flake8
```

---

## Memformat Kode

Jika proses linting hanya melakukan pengecekan, proses memformat kode akan memberikan pesan berupa kode yang telah diperbaiki — artinya Anda tidak perlu mengubah kode secara manual.

Berikut adalah tiga jenis aplikasi untuk memformat kode:

### black

Proyek open source yang dikembangkan di repository Python Software Foundation (PSF) dengan lisensi MIT.

```bash
pip install black
black kalkulator.py
```

### YAPF (Yet Another Python Formatter)

Proyek open source yang dikembangkan di repository Google dengan lisensi Apache.

```bash
pip install yapf
yapf kalkulator.py
```

### autopep8

Proyek open source (berlisensi MIT) yang termasuk paling awal untuk memformat kode dengan bantuan lint `pycodestyle`.

```bash
pip install autopep8
autopep8 kalkulator.py
```

---

## Style Guide: Statement Gabungan

### Statement Gabungan

Usahakan untuk tidak menggabungkan lebih dari satu statement pada baris yang sama.

✅ Disarankan:

```python
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

❌ Tidak disarankan:

```python
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

### Penggunaan Trailing Commas

Koma di bagian akhir (*trailing commas*) umumnya bersifat opsional. Wajib digunakan saat membuat tuple dengan satu elemen.

✅ Disarankan:

```python
FILES = ('setup.cfg',)

FILES = [
    'setup.cfg',
    'tox.ini',
    ]
```

❌ Tidak disarankan:

```python
FILES = 'setup.cfg',
FILES = ['setup.cfg', 'tox.ini',]
```

### Anotasi Fungsi

Gunakan spasi setelah titik dua (`:`) dan di sekitar arrow (`->`). Jika menggabungkan anotasi dengan nilai default, gunakan spasi di sekitar `=`. Jika tidak ada anotasi, hindari spasi di sekitar `=`.

✅ Disarankan:

```python
def munge(input: str): pass
def munge() -> str: pass
def LuasPersegiPanjang(panjang: int = 2, lebar=None): pass
```

❌ Tidak disarankan:

```python
def munge(input:str): pass
def munge()->str: pass
def LuasPersegiPanjang(panjang: int=2, lebar = None): pass
```

---

## Style Guide: Prinsip Penamaan

Penamaan pada Python mencakup banyak hal, seperti penamaan fungsi, kelas, dan sebagainya. Konsistensi internal tim atau perusahaan lebih diutamakan.

### Ringkasan Prinsip Penamaan

| Elemen | Konvensi | Contoh |
|--------|----------|--------|
| Variabel & fungsi | `huruf_kecil_garis_bawah` | `hitung_luas()` |
| Konstanta | `HURUF_BESAR_GARIS_BAWAH` | `MAX_SIZE = 100` |
| Kelas | `CapWords` / `PascalCase` | `KalkulatorSederhana` |
| Exception | `CapWords` + `Error` | `DivideByZeroError` |
| Modul | `huruf_kecil` | `math_operations.py` |
| Paket | `hurufkecil` | `mypackage` |
| Instance method | `self` sebagai arg pertama | `def hitung(self):` |
| Class method | `cls` sebagai arg pertama | `def buat(cls):` |

### Penamaan Khusus

| Pola | Keterangan |
|------|------------|
| `_nama` | Penggunaan internal lemah |
| `nama_` | Menghindari konflik dengan reserved words |
| `__nama` | Bagian dari kelas tertentu |
| `__nama__` | Dunder — khusus Python, jangan dibuat sendiri |

### Hal yang Dihindari

- Karakter `l`, `O`, `I` sebagai nama variabel satu karakter (mirip angka `1` dan `0`)
- Awalan huruf/frasa pada nama fungsi seperti `f_mean()` atau `r_name()`
- Penamaan dunder (`__nama__`) kecuali yang sudah terdokumentasikan Python

### Selalu Persiapkan untuk Inheritance

Jika ragu apakah suatu variabel/method harus publik atau non-publik, jadikan non-publik. Lebih mudah mengubah non-publik menjadi publik daripada sebaliknya.

- Atribut publik: tanpa awalan garis bawah
- Atribut non-publik: awalan satu garis bawah (`_nama`)
- Atribut khusus kelas (hindari konflik subkelas): awalan dua garis bawah (`__nama`)
