# Style Guide: Statement Gabungan

Setelah mengetahui aplikasi untuk pengecekan dan memformat kode, kali ini kita akan belajar cara membuat kode yang baik dan benar. Perhatikan bahwa materi ini akan menunjukkan sintaks yang disarankan dan tidak disarankan.

---

## Statement Gabungan

Saat Anda membuat program dengan banyak statement, usahakan untuk tidak menggabungkan lebih dari satu statement pada baris yang sama.

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

Anda diperbolehkan membuat konten dari `if`/`for`/`while` yang cukup pendek dalam satu baris (program tetap berjalan). Namun, pastikan tidak melakukannya jika `if`/`for`/`while` Anda bertingkat atau bersifat multi clause, misalnya `if-else`, `try-finally`, dan sebagainya.

❌ Tidak disarankan:

```python
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()
```

⛔ Sangat tidak disarankan:

```python
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()
```

---

## Penggunaan Trailing Commas

Koma di bagian akhir (*trailing commas*) umumnya bersifat opsional. Satu kondisi yang bersifat wajib adalah saat kita membuat variabel menggunakan tipe tuple dengan satu elemen. Hal ini umumnya diperjelas dengan kurung untuk menghindari penghapusan atau pembersihan.

✅ Disarankan:

```python
FILES = ('setup.cfg',)
```

❌ Tidak disarankan:

```python
FILES = 'setup.cfg',
```

Saat trailing comma bersifat redundan, Anda akan merasakan kemudahannya saat menggunakan VCS (Version Control System), atau pada kode yang mungkin ditambahkan dalam beberapa waktu ke depan. Pola yang disarankan adalah meletakkan nilai atau string pada baris baru, mengikuti indentasi, menambahkan trailing comma, dan menutup kurung/kurawal/siku pada baris selanjutnya.

✅ Disarankan:

```python
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

❌ Tidak disarankan:

```python
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
```

---

## Anotasi Fungsi

Anotasi fungsi adalah fitur yang memungkinkan kita untuk menambahkan informasi tambahan tentang parameter dan return value dari sebuah fungsi. Jika sebelumnya kita belajar menambahkan informasi terkait fungsi dengan docstring, anotasi fungsi lebih spesifik untuk menjelaskan parameter dan return value.

Penggunaan anotasi fungsi sebaiknya menggunakan aturan baku untuk titik dua (`:`) dan menggunakan spasi untuk penggunaan arah panah atau arrow (`->`). Hal ini disebut sebagai *type hints* yang merujuk pada PEP 484.

✅ Disarankan:

```python
def munge(input: str):    # Menambahkan informasi parameter bertipe string
    pass

def munge() -> str:       # Menambahkan informasi return value bertipe string
    pass
```

❌ Tidak disarankan:

```python
def munge(input:str):     # Menambahkan informasi parameter bertipe string
    pass

def munge()->str:         # Menambahkan informasi return value bertipe string
    pass
```

Selanjutnya, saat membuat fungsi dan Anda menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi baik sebelum dan sesudah tanda sama dengan (`=`).

```python
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    pass
```

Pada contoh di atas, sintaks berikut menjelaskan bahwa parameter `panjang` harus bertipe data integer:

```python
panjang: int
```

Sementara itu, menambahkan nilai setelah `=` akan memberikan nilai default. Contohnya sintaks berikut memberikan nilai default `2` untuk parameter `panjang`:

```python
panjang: int = 2
```

Contoh lengkap penggunaan anotasi fungsi:

```python
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang * lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)

"""
Output:
4
"""
```

Perlu diingat bahwa karena *type hints* bersifat opsional dan hanya memberikan petunjuk, jika pada fungsi `LuasPersegiPanjang` kita memberikan tipe data `float`, program akan tetap berjalan sebagaimana mestinya.

---

### Fungsi Tanpa Anotasi

Jika pada saat membuat fungsi tanpa adanya anotasi yang menandakan keyword argumen atau nilai default, hindari penggunaan spasi di sekitar tanda sama dengan (`=`).

✅ Disarankan:

```python
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang * lebar
    return luas
```

❌ Tidak disarankan:

```python
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang * lebar
    return luas
```

### Menggabungkan Anotasi dan Nilai Default

Jika kita membuat fungsi yang menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi sebelum dan sesudah `=`. Namun, ketika membuat fungsi biasa tanpa anotasi, sebaiknya tidak menggunakan spasi sebelum dan sesudah `=`.

✅ Disarankan:

```python
def LuasPersegiPanjang(panjang: int = 2, lebar=None):
    pass
```

❌ Tidak disarankan:

```python
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass
```

Pada contoh di atas, parameter `panjang` menggabungkan anotasi fungsi dan nilai default, sedangkan parameter `lebar` hanya mendefinisikan nilai default tanpa anotasi fungsi. Perhatikan penempatan spasi pada setiap parameternya.
