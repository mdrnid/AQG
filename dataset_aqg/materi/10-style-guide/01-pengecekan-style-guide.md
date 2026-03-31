# Pengecekan Style Guide PEP8

Sampai dengan saat ini, Anda tentu sudah menuliskan kode pemrograman Python cukup banyak, termasuk di antaranya kode yang Anda tulis mengalami kesalahan sintaksis atau indentasi. Lalu, bagaimana agar ke depannya bisa mencegah hal tersebut terjadi?

Semua itu bergantung pada kode editor yang Anda gunakan untuk menulis kode Python. Terkadang ada beberapa kode editor yang sudah dilengkapi dengan fitur pengecekan kemungkinan kesalahan dan memformat kode sesuai arahan gaya penulisan (style guide) PEP8, seperti PyCharm. Ada juga kode editor seperti Visual Studio Code yang menyediakan plugin tambahan untuk membantu pengecekan kemungkinan kesalahan dan memformat kode.

**PEP** atau *Python Enhancement Proposals* merupakan panduan yang telah menjadi acuan untuk perkembangan Python. Salah satu panduan tersebut membahas mengenai arahan gaya penulisan (style guide) yang baik dan benar ketika Anda ingin membangun kode menggunakan Python. Panduan tersebut adalah **PEP8** yang berjudul *"Style Guide for Python Code"*.

Tujuan dari panduan ini agar kode Anda lebih mudah dibaca dan dipahami oleh programmer lain serta menghindari kemungkinan kesalahan yang akan muncul.

Pada materi kali ini, kita akan mempelajari beberapa aplikasi yang dapat Anda gunakan dengan memanggil perintah atau sebaiknya diintegrasikan ke editor kode yang Anda pakai. Tujuannya untuk membantu Anda mengecek kemungkinan kesalahan dan kesesuaian dengan PEP8.

---

## Lint

Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk dalam proses ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut **linter**.

Integrasi linter dengan editor kode Anda akan membuat efisien dalam menulis kode Python. Pertimbangan ini karena keluaran atau output dari aplikasi linter hanya berupa teks singkat berupa keterangan dan kode Error atau Warning atau Kesalahan Konvensi Penamaan (Naming Conventions).

Lint atau linting akan meminimalkan kode Anda mengalami error, salah satu contohnya karena kesalahan indentasi di Python. Sebelum kode Anda diproses oleh interpreter Python dengan `IndentationError`, lint akan memberitahukannya lebih dahulu ke Anda.

Berikut akan dibahas tiga jenis aplikasi linter. Tidak harus semuanya diinstal — hanya paket yang menurut Anda sesuai kebutuhan saja yang digunakan.

> **Catatan:** Output ketiga aplikasi ini kemungkinan mirip, tetapi pada kondisi tertentu akan ada output atau fitur yang mungkin sesuai dengan kebutuhan Anda menulis kode.

### Pycodestyle

Pycodestyle (sebelumnya bernama `pep8`) adalah aplikasi open source (berlisensi MIT/Expat) untuk membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8.

```bash
pip install pycodestyle
```

### Pylint

Pylint adalah aplikasi open source (berlisensi GPL v2) untuk melakukan analisis kode Python, mengecek kesalahan (error) pemrograman, memaksakan standar penulisan kode, serta memberikan saran untuk refactoring sederhana.

```bash
pip install pylint
```

### Flake8

Flake8 adalah aplikasi open source (berlisensi MIT) yang membungkus sejumlah kemampuan aplikasi lain, seperti `pycodestyle`, `pyflakes`, dan fitur lainnya.

```bash
pip install flake8
```

---

## Cara Kerja Linter

Pastikan Anda sudah menginstal aplikasi yang disebutkan sebelumnya.

**Langkah 1** — Buat file `kalkulator.py` dan masukkan kode berikut:

```python
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
    return self.i - _i
```

Berdasarkan PEP8, kode tersebut masih perlu diperbaiki dan ada blok kode yang akan menghasilkan error.

**Langkah 2** — Buka terminal, pastikan berada di direktori tempat file berada, lalu jalankan salah satu perintah berikut.

**Pycodestyle:**

```bash
pycodestyle kalkulator.py
```

![Tampilan terminal ketika menjalankan script menggunakan pycodestyle](assets/dos-138a11d39cda96e183b2a5b32b3c5e3f20230823192816.png)

**Pylint:**

```bash
pylint kalkulator.py
```

![Tampilan terminal ketika menjalankan script menggunakan pylint](assets/dos-248507f072ac6c74341b8903ced0d07820230823192952.png)

**Flake8:**

```bash
flake8 kalkulator.py
```

![Tampilan terminal ketika menjalankan script menggunakan flake8](assets/dos-91b4268978cf80b7d39ef3c8aad4c7c020230823193054.png)

Pesan dari ketiga aplikasi tersebut beragam, tetapi ada satu kesamaan — ketiganya menunjukkan pola yang sama di awal pesan berupa nama file diikuti dengan baris dan kolom.

![Format pesan error: nama file, baris, dan kolom](assets/dos-229d7b4243edfb42235e72c531c1c2c120230823192255.jpeg)

![Ilustrasi baris dan kolom pada kode](assets/dos-d7e37b7d7642eee485b9d7d4226a0aa720230823192255.jpeg)

Contoh: pesan pylint `"kalkulator.py 7:5 Parsing failed: 'expected an indented block after function definition on line 6'"` berarti pada baris 7 kolom ke-5 seharusnya memiliki indentasi setelah mendefinisikan fungsi di baris ke-6.

---

## Memperbaiki Kode

Ganti isi `kalkulator.py` dengan kode yang sudah diperbaiki berikut:

```python
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i): return self.i + _i

    def kurang(self, _i):
        return self.i - _i
```

Perbaikan yang dilakukan:
- Menambahkan baris kosong (*new line*) setelah setiap blok fungsi
- Menambahkan indentasi pada method `kurang`

Jalankan kembali file tersebut menggunakan ketiga aplikasi. Jika diproses menggunakan `pycodestyle` dan `flake8`, tidak akan memunculkan pesan error.

![Tampilan terminal tanpa pesan error](assets/dos-bf00db5ba34d695e76db376948c4865420230823192254.jpeg)

Namun, ketika dijalankan menggunakan `pylint`, beberapa pesan peringatan muncul karena kita perlu menambahkan dokumentasi pada setiap fungsi dan kelas yang dibangun.

![Tampilan peringatan pylint](assets/dos-e67c91e8a3997ebe3ffd5de5c75c2b1420230823192255.jpeg)
