# Style Guide: Prinsip Penamaan pada Python

Saat membuat variabel, fungsi, hingga kelas, Anda dapat memberikan nama-nama yang beragam. Terkadang, keberagaman tersebut menghasilkan tidak adanya standar dalam kode yang Anda bangun.

Pada materi ini, kita akan belajar beberapa prinsip penamaan saat Anda membangun kode Python. Harapannya, Anda bisa membuat standar nama saat membangun variabel, fungsi, hingga kelas.

> **Catatan:** Pada materi-materi sebelumnya, style guide Python belum diterapkan secara menyeluruh. Sangat disarankan jika Anda mempelajari ulang kode pada materi-materi sebelumnya dengan menerapkan style guide Python.

Perlu diperhatikan juga bahwa Anda dapat memilih mempertahankan styling yang sudah digunakan sebelumnya untuk menjaga konsistensi internal tim atau perusahaan. Konsistensi internal lebih diutamakan.

---

## Prinsip Overriding

Nama yang dilihat oleh user publik sebaiknya merefleksikan penggunaan/fungsinya dan bukan implementasinya. Misalnya nama fungsi berikut lebih mudah dipahami:

```python
cariJalan()   # Lebih deskriptif
jalan()       # Kurang informatif
```

Algoritma yang digunakan hingga informasi lainnya dari fungsi yang dibangun dapat dijelaskan dalam docstring ataupun komentar.

---

## Penamaan Deskriptif

Penamaan deskriptif adalah cara untuk memberikan nama yang informatif, jelas, dan sesuai dengan tujuan dari elemen kode. Penamaan deskriptif ini meliputi variabel, fungsi, kelas, hingga konstanta.

Ada berbagai cara penamaan yang umum digunakan dalam Python. Pemilihan cara penamaan ini penting untuk menjaga konsistensi dan kejelasan kode. Penamaan ini juga merujuk pada PEP8 mengenai *Naming Conventions* dan *Naming Styles*.

Berikut adalah beberapa cara penamaan yang umum:

| Gaya | Contoh |
|------|--------|
| Satu karakter huruf kecil | `b` |
| Satu karakter huruf besar | `B` |
| Huruf kecil | `hurufkecil` |
| Huruf kecil dengan garis bawah | `huruf_kecil_dengan_pemisah` |
| Huruf besar semua | `HURUFBESAR` |
| Huruf besar dengan garis bawah | `HURUF_BESAR_DENGAN_PEMISAH` |
| CapWords / PascalCase | `HurufBesarDiAwalKata` |
| mixedCase / camelCase | `hurufCampuran` |
| CapWords dengan garis bawah | `Huruf_Besar_Di_Awal_Kata` |

Untuk CapWords, pastikan semua singkatan/akronim dituliskan dengan huruf besar. Contoh: `HTTPServerError`, bukan `HttpServerError`.

Python tidak menyarankan penggunaan huruf atau frasa sebagai awalan fungsi, seperti `f` pada `f_mean()` atau `r` pada `r_name()`. Python memiliki prinsip yang berlaku dalam penamaan fungsi atau method:

- Atribut dan method name bersifat *pre-fixed* dengan objek
- Function name selalu diawali dengan module name

### Penamaan Khusus

Berikut adalah beberapa bentuk penamaan khusus yang umum ditemukan. Ini juga bisa diterapkan pada penamaan variabel dan kelas:

| Pola | Keterangan |
|------|------------|
| `_nama` | Penggunaan internal lemah, merujuk pada lingkup tertentu |
| `nama_` | Digunakan untuk mengatasi redundan dengan keyword/reserved words di Python |
| `__nama` | Menegaskan bahwa sebuah objek adalah bagian dari kelas tertentu |
| `__nama__` | Objek atau atribut khusus yang diciptakan Python (dunder). Contoh: `__init__`, `__import__`, `__file__` |

Anda sangat tidak disarankan membuat penamaan menggunakan dunder (`__nama__`) karena bisa menimpa kode yang sudah ada di Python. Terkecuali penamaan tersebut sudah terdokumentasikan oleh Python seperti `__init__`.

---

## Hal-hal yang Harus Dipertimbangkan dalam Penamaan

### Nama yang Dihindari

Hindari karakter `l` (huruf L kecil), `O` (huruf O besar), atau `I` (huruf I besar) sebagai nama variabel satu karakter karena mereka sulit dibedakan dengan angka `1` dan `0`. Daripada menggunakan `l` kecil, gunakan `L` besar.

### ASCII Compatibility

Merujuk pada PEP 3131, suatu *identifiers* yang digunakan dalam Python Standard Library harus kompatibel dengan kode ASCII. *Identifiers* merujuk pada nama-nama yang digunakan untuk menyebut variabel, fungsi, kelas, dan kode lainnya dalam Python. Contoh: nama variabel `x`, nama fungsi `penjumlahan()`, atau nama method `get_nama()`.

### Nama Paket dan Nama Modul

Penamaan modul sebaiknya pendek atau singkat, menggunakan huruf kecil, dan opsional garis bawah (`_`) untuk meningkatkan keterbacaan. Contoh: `math_operations.py`.

Nama paket juga sebaiknya singkat, menggunakan huruf kecil, dan hindari garis bawah. Contoh: paket `math` yang di dalamnya ada modul `math_operations.py`.

### Nama Kelas

Saat menamai kelas, gunakan **CamelCase** atau **CapWords**. Pastikan semua akronim (misal HTTP) ditulis keseluruhan dengan huruf besar.

### Penulisan Tipe Variabel

Untuk penamaan variabel, umumnya menggunakan CamelCase atau CapWords, lebih pendek lebih baik. Contoh: `T`, `AnyStr`, `Num`.

Jika terdapat *covariant* atau *contravariant* dari sebuah variabel, tambahkan di akhir variabel untuk mempermudah pembacaan:

```python
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

### Nama Exception

Untuk pengecualian (exception), terapkan konvensi penamaan kelas karena exception seharusnya bertipe kelas. Tambahkan `"Error"` atau nama deskriptif lain pada nama exception:

```python
class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)

def divide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
except DivideByZeroError as e:
    print(f"Error: {e}")

"""
Output:
Error: Cannot divide by zero
"""
```

### Nama Variabel Global

Dalam variabel global, penamaannya bisa mengikuti fungsi/modul yang bersifat publik. Anda bisa menggunakan garis bawah untuk menghindari variabel tersebut diimpor jika ia termasuk modul non-publik.

### Nama Fungsi, Parameter, dan Variabel

Nama fungsi, parameter, dan variabel sebaiknya menggunakan huruf kecil dengan pemisahan menggunakan garis bawah untuk meningkatkan keterbacaan. `mixedCase` dapat digunakan jika ada dependensi dengan pustaka menggunakan style tertentu.

### Argumen Fungsi dan Method

Dalam pembuatan fungsi dan method pada suatu kelas, ada beberapa hal yang perlu dipertimbangkan:

- Gunakan `self` sebagai argumen pertama jika Anda membuat instance method
- Gunakan `cls` sebagai argumen pertama ketika Anda membuat class method
- Jika nama argumen fungsi adalah reserved keyword, tambahkan garis bawah di akhir nama argumen. Contoh: gunakan `class_` atau `kelas`, bukan `clss`

### Nama Method dan Variabel Instance

Saat membuat method dan variabel dalam suatu kelas, gunakan standar penamaan fungsi — huruf kecil dengan pemisah kata garis bawah. Tambahkan garis bawah sebagai awalan untuk method non-publik dan variabel internal pada fungsi.

Untuk menghindari kesamaan dengan subkelas, gunakan `__nama_method` (dua garis bawah di awal). Python menggabungkan nama modul dengan nama kelas. Misal ada kelas `Foo` dengan atribut `__a`, kita tidak dapat mengaksesnya melalui `Foo.__a`, tetapi `Foo._Foo__a`.

### Konstanta

Dalam memberikan nama variabel bertipe konstanta, umumnya didefinisikan pada bagian atas modul dengan huruf besar semua:

```python
PI = 3.14
TOTAL = 4.14213
```

---

## Selalu Persiapkan untuk Inheritance

Saat membangun method dan variabel dalam sebuah kelas, sebaiknya Anda dapat langsung mengetahui atribut pada method dan variabel tersebut — publik atau non-publik. Jika Anda ragu, jadikan atributnya non-publik. Sebab, lebih mudah menjadikan sebuah variabel/method bersifat non-publik menjadi publik, dibandingkan sebaliknya.

```python
class MyClass:
    def __init__(self):
        self._private_var = 42          # Variabel non-publik
        self._secret_list = [1, 2, 3]  # Variabel non-publik lainnya

    def _private_method(self):
        print("Ini adalah method non-publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non-publik
```

Method/variabel publik dipersiapkan untuk pihak eksternal menggunakan kelas Anda. Sebaliknya, method/variabel non-publik hanya digunakan oleh Anda sebagai developer dan tidak memberikan garansi bahwa Anda takkan mengubah atau menghapusnya.

Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut:

- Atribut publik tidak menggunakan awalan garis bawah
- Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf
- Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang — cukup dengan nama atribut sependek mungkin
- Jika Anda berniat mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, tambahkan awalan dua garis bawah

Semua materi style guide ini mengacu pada PEP8 yang dapat Anda baca lebih lanjut.
