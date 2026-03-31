# Tipe Data

Sebagaimana yang telah dijelaskan, setiap nilai yang digunakan dalam variabel adalah sebuah data. Data memiliki tipe yang berbeda-beda dan dapat kita temui dalam kehidupan sehari-hari. Simak kisah berikut.

> "Seorang pria berumur 30 tahun menjalani kehidupan di ibu kota Jakarta. Pria tersebut bernama Evans dan memiliki berat badan sebesar 75 kg. Suatu hari, Evans harus pergi ke kantor, tetapi hujan deras melanda kota tersebut. Evans pun memutuskan untuk menunggu selama 30 menit sebelum akhirnya berangkat kerja. Jika setelah 30 menit hujan tak kunjung reda, ia akan memakai jas hujan. Namun, jika hujan reda, ia tidak akan memakai jas hujan."

![Ilustrasi kisah Evans](assets/ilustrasi-evans.jpeg)

Beberapa data yang dapat diambil dari kisah tersebut:

- **Umur** — dibentuk dari kumpulan angka. Tipe data ini adalah *numbers* dengan rentang nilai, misalnya 1 sampai 100.
- **Nama** — dibentuk dari serangkaian huruf. Tipe data ini adalah *string* dengan rentang 1 sampai 50 huruf.
- **Berat Badan** — dibentuk dari kumpulan angka, sama seperti data umur.
- **Keputusan Memakai Jas Hujan** — hanya memiliki dua kemungkinan: `True` (memakai jas hujan) atau `False` (tidak memakai). Tipe data ini adalah *boolean*.

Dalam Python, tipe data dikelompokkan menjadi dua: **tipe data primitif** dan **tipe data collection**.

---

## Tipe Data Primitif

Tipe data primitif merupakan jenis paling dasar dalam pemrograman yang menyimpan *single value*.

---

### Numbers

Tipe data `numbers` adalah tipe data angka yang terdiri dari tiga jenis:

| Jenis | Deskripsi | Contoh |
|-------|-----------|--------|
| `int` | Bilangan bulat positif atau negatif, tanpa desimal | `1`, `-20`, `999`, `0` |
| `float` | Bilangan riil, dapat berupa bilangan bulat atau desimal | `3.14`, `1.0`, `4.01E+1` |
| `complex` | Bilangan kompleks (tidak digunakan di kelas ini) | `1+2j` |

Ciri khas tipe data `numbers` adalah dapat dioperasikan dengan operasi matematika seperti `+`, `-`, `*`, dan lainnya.

```python
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""
```

Tipe data `numbers` bersifat **immutable** — nilainya tidak dapat diubah. Perhatikan contoh berikut:

```python
var = 10
print(var)
print(id(var))

var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""
```

Ketika Anda melakukan inisialisasi ulang variabel, Python sebenarnya **membuat objek baru** dengan nilai baru — bukan mengubah nilai yang sudah ada. Hal ini dibuktikan dengan berubahnya alamat memori (`id()`) setiap kali nilai diperbarui.

> Semua tipe data primitif (`numbers`, `boolean`, `string`) bersifat immutable secara natural.

---

### Boolean

Tipe data `boolean` hanya bernilai `True` atau `False` dan merepresentasikan nilai kebenaran (*truth values*).

Nilai yang dianggap `False` dalam Python:

- Nilai yang sudah didefinisikan salah: `None` dan `False`
- Angka nol dari semua tipe numerik: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`
- Urutan dan koleksi kosong: `""`, `()`, `{}`, `set()`, `range(0)`

```python
x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""
```

---

### String

`String` merupakan karakter yang berurutan, diawali dengan single quote (`''`) atau double quote (`""`).

```python
x = 'Dicoding'
print(type(x))

"""
Output:
<class 'str'>
"""
```

Beberapa fakta menarik tentang string Python:

**1. Multi-line string** menggunakan triple quote (`"""` atau `'''`):

```  thon
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""
```

**2. Indexing** — setiap karakter memiliki indeks yang dimulai dari `0`:

```python
x = 'Dicoding'
print(x[0])

"""
Output:
D
"""
```

**3. Immutable** — karakter dalam string tidak dapat diubah:

```python
x = 'Dicoding'
x[0] = 'F'

"""
Output:
TypeError: 'str' object does not support item assignment
"""
```

**4. Slicing** — mengambil beberapa karakter sekaligus:

```python
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""
```

**5. Menampilkan string dengan variabel** — ada beberapa metode:

*Formatted String (f-string):*

```python
name = "Perseus Evans"
print(f"Hello, nama saya {name}")

"""
Output:
Hello, nama saya Perseus Evans
"""
```

*%-formatting:*

```python
name = "Perseus Evans"
print("Nama saya %s" % (name))

"""
Output:
Nama saya Perseus Evans
"""
```

*str.format():*

```python
name = "Perseus Evans"
print("Nama saya {}".format(name))

"""
Output:
Nama saya Perseus Evans
"""
```

Informasi lebih detail tentang string Python tersedia di [dokumentasi resmi Python](https://docs.python.org/3/library/string.html).

---

## Tipe Data Collection

Tipe data collection menyimpan satu atau lebih data primitif sebagai satu kelompok.

---

### List

`List` merupakan kumpulan data terurut (*ordered sequence*) dan salah satu tipe data yang paling sering digunakan. Berbeda dengan array di bahasa lain, list Python tidak mengharuskan semua elemen bertipe data sama.

![Ilustrasi list Python](assets/ilustrasi-list.jpeg)

List diinisialisasi dengan kurung siku `[]` dan setiap elemen dipisahkan dengan koma:

```python
x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output:
<class 'list'>
"""
```

Setiap elemen list memiliki indeks yang dimulai dari `0`:

![Ilustrasi indeks list](assets/ilustrasi-indeks-list.jpeg)

```python
x = [1, 'Dicoding', True, 1.0]
print(x[2])

"""
Output:
True
"""
```

List bersifat **mutable** — nilainya dapat diubah:

```python
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""
```

#### Indexing

```
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])    # indeks ke-0
print(x[2])    # indeks ke-2
print(x[-1])   # indeks terakhir
print(x[-3])   # indeks ke-3 dari terakhir

"""
Output:
laptop
mouse
microphone
keyboard
"""
```

#### Slicing

Slicing mengambil data berdasarkan rentang indeks tertentu dengan pola:

```
sequence[start:stop:step]
```

- `start` — indeks awal (inklusif)
- `stop` — indeks akhir (eksklusif)
- `step` — jumlah elemen yang dilewati (default: `1`)

![Ilustrasi inklusif pada interval](assets/ilustrasi-inklusif.jpeg)

![Ilustrasi eksklusif pada interval](assets/ilustrasi-eksklusif.jpeg)

```python
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])   # indeks 0-4, setiap 2 elemen
print(x[1:])      # indeks 1 hingga terakhir
print(x[:3])      # indeks 0 hingga 2 (eksklusif)

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']
"""
```

---

### Tuple

![Ilustrasi tuple](assets/ilustrasi-tuple.jpeg)

`Tuple` adalah jenis list yang **tidak dapat diubah** elemennya (*immutable*). Umumnya digunakan untuk data yang bersifat tetap dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung `()`:

```put: 
Nam (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""
```

Indexing dan slicing pada tuple bekerja sama seperti list:

```python
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

"""
Output:
program
(5, 'program', (1+3j))
"""
```

Tuple bersifat immutable — tidak dapat diubah:

```python
x = (5, 'program', 1+3j)
x[1] = 'Dicoding'

"""
Output:
TypeError: 'tuple' object does not support item assignment
"""
```

---

### Set

`Set` adalah kumpulan item yang bersifat **unik** dan **tanpa urutan** (*unordered*). Set diinisialisasi dengan kurawal `{}`:

```hon
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""
```

Karena tidak memiliki urutan, set **tidak mendukung indexing**:

```python
x = {1, 2, 7, 2, 3, 13, 3}
print(x[0])

"""
Output:
TypeError: 'set' object is not subscriptable
"""
```

![Ilustrasi set unik](assets/ilustrasi-set.jpeg)

Set mendukung operasi himpunan matematika menggunakan method `.union()` dan `.intersection()`:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
"""
```

---

### Dictionary

`Dictionary` merupakan kumpulan pasangan *key-value* yang tidak berurutan. Dictionary didefinisikan dengan kurawal `{}` dengan aturan:

- Setiap pasangan key-value dipisahkan dengan koma (`,`)
- Key dan value dipisahkan dengan titik dua (`:`)
- Key dan value dapat berupa tipe variabel atau objek apa pun

![Ilustrasi dictionary](assets/ilustrasi-dictionary.jpeg)

```python
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
print(type(x))

"""
Output:
<class 'dict'>
"""
```

Akses nilai dictionary menggunakan **key**, bukan indeks:

```
# Menggunakan indeks → error
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
print(x[0])

"""
Output:
KeyError: 0
"""
```

```python
# Menggunakan key → benar
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
print(x['name'])

"""
Output:
Perseus Evans
"""
```

**Menambah data:**

```python
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
x['Job'] = "Web Developer"
print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""
```

**Menghapus data** menggunakan `del`:

```python
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
del x['isMarried']
print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20}
"""
```

**Mengubah data:**

```python
x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
x['name'] = "Dicoding"
print(x)

"""
Output:
{'name': 'Dicoding', 'age': 20, 'isMarried': False}
"""
```

---

## Konversi antara Tipe Data

Python menyediakan fungsi bawaan untuk mengonversi antar tipe data.

### Integer ke Float

```python
print(float(5))

"""
Output:
5.0
"""
```

### Float ke Integer

```python
print(int(5.6))
print(int(-5.6))

"""
Output:
5
-5
"""
```

### Dari dan ke String

```python
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""
```

> Konversi dari dan ke string akan divalidasi terlebih dahulu. Jika tidak valid, Python akan menghasilkan error:

```python
print(int("1p"))

"""
Output:
ValueError: invalid literal for int() with base 10: '1p'
"""
```

### Konversi Kumpulan Data

```python
print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list('hello'))

"""
Output:
{1, 2, 3}
(5, 6, 7)
['h', 'e', 'l', 'l', 'o']
"""
```

### Konversi ke Dictionary

Data harus memenuhi persyaratan key-value. Gunakan fungsi `dict()`:

```python
# Dari list berisi list pasangan nilai
print(dict([[1, 2], [3, 4]]))

"""
Output:
{1: 2, 3: 4}
"""
```

```python
# Dari list berisi tuple pasangan nilai
print(dict([(3, 26), (4, 44)]))

"""
Output:
{3: 26, 4: 44}
"""
```

