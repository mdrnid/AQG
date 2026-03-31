# Transformasi Angka, Karakter, dan String

Pada materi ini, Anda akan mempelajari berbagai cara mentransformasi tipe data string menggunakan method bawaan Python.

---

## Mengubah Huruf Besar/Kecil

Metode berikut mengubah string menjadi huruf kapital atau huruf kecil. Karakter bukan huruf (simbol, angka) tidak akan terpengaruh.

### `upper()`

Mengubah semua huruf dalam string menjadi uppercase:

```python
kata = 'dicoding'
kata = kata.upper()
print(kata)

"""
Output:
DICODING
"""
```

### `lower()`

Mengubah semua huruf dalam string menjadi lowercase:

```python
kata = 'DICODING'
kata = kata.lower()
print(kata)

"""
Output:
dicoding
"""
```

---

## Awalan dan Akhiran

Metode berikut digunakan untuk menghapus karakter *whitespace* atau karakter tertentu dari awal/akhir string.

### `rstrip()`

Menghapus whitespace di sebelah kanan (akhir) string:

```python
print("Dicoding          ".rstrip() + " Indonesia")

"""
Output:
Dicoding Indonesia
"""
```

### `lstrip()`

Menghapus whitespace di sebelah kiri (awal) string:

```python
print("           Dicoding".lstrip())

"""
Output:
Dicoding
"""
```

### `strip()`

Menghapus whitespace di kedua sisi string:

```python
print("         Dicoding          ".strip())

"""
Output:
Dicoding
"""
```

Anda juga bisa menghapus karakter selain whitespace dengan memberikan nilai pada `strip()`:

```python
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

"""
Output:
Dicoding
"""
```

### `startswith()`

Mengembalikan `True` jika string diawali dengan kata yang dicari:

```python
print('Dicoding Indonesia'.startswith('Dicoding'))

"""
Output:
True
"""
```

### `endswith()`

Mengembalikan `True` jika string diakhiri dengan kata yang dicari, `False` jika tidak:

```python
print('Dicoding Indonesia'.endswith('Dicoding'))

"""
Output:
False
"""
```

---

## Memisah dan Menggabung String

### `join()`

Menggabungkan elemen-elemen list menjadi satu string dengan delimiter tertentu:

```python
print(' '.join(['Dicoding', 'Indonesia', '!']))

"""
Output:
Dicoding Indonesia !
"""
```

Anda bisa menggunakan delimiter selain spasi:

```python
print('123'.join(['Dicoding', 'Indonesia']))

"""
Output:
Dicoding123Indonesia
"""
```

### `split()`

Kebalikan dari `join()` — memisahkan string menjadi list berdasarkan delimiter:

```python
print('Dicoding Indonesia !'.split())

"""
Output:
['Dicoding', 'Indonesia', '!']
"""
```

Anda juga bisa menggunakan delimiter newline (`\n`) untuk memisahkan string multi-baris:

```python
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""
```

---

## Mengganti Elemen String

### `replace()`

Mengganti substring tertentu dengan substring lain. Perlu diingat bahwa `replace()` bersifat *case-sensitive*:

```python
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

"""
Output:
Ayo belajar Pemrograman di Dicoding
"""
```

Perhatikan bahwa kata `coding` pada `Dicoding` tidak ikut berubah karena huruf awalnya berbeda (`c` kecil vs `C` besar).

---

## Pengecekan String

Metode berikut mengembalikan nilai boolean `True` atau `False`.

### `isupper()`

Mengembalikan `True` jika semua huruf dalam string adalah uppercase:

```python
kata = 'DICODING'
print(kata.isupper())

"""
Output:
True
"""
```

### `islower()`

Mengembalikan `True` jika semua huruf dalam string adalah lowercase:

```python
kata = 'dicoding'
print(kata.islower())

"""
Output:
True
"""
```

### `isalpha()`

Mengembalikan `True` jika semua karakter adalah huruf alfabet:

```python
kata = 'dicoding'
print(kata.isalpha())

"""
Output:
True
"""
```

### `isalnum()`

Mengembalikan `True` jika karakter dalam string adalah alfanumerik (huruf, angka, atau keduanya):

```python
kata = 'dicoding123'
print(kata.isalnum())

"""
Output:
True
"""
```

### `isdecimal()`

Mengembalikan `True` jika semua karakter adalah angka/numerik:

```python
print('123'.isdecimal())

"""
Output:
True
"""
```

### `isspace()`

Mengembalikan `True` jika string hanya berisi whitespace (spasi, tab, newline, dll.):

```python
print('         '.isspace())

"""
Output:
True
"""
```

### `istitle()`

Mengembalikan `True` jika setiap kata dalam string diawali huruf kapital:

```python
print('Dicoding Indonesia'.istitle())

"""
Output:
True
"""
```

---

## Formatting pada String

### `zfill()`

Menambahkan angka `0` di depan string hingga mencapai panjang yang ditentukan. Berguna untuk format nomor nota atau nomor antrian:

```python
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

"""
Output:
0Code
"""
```

Kata `'Code'` memiliki 4 karakter. Dengan `zfill(5)`, program menambahkan `0` di depan agar panjangnya menjadi 5.

### `rjust()`

Membuat teks rata kanan dengan menambahkan karakter pengisi di sebelah kiri:

```python
print('Dicoding'.rjust(20))

"""
Output:
            Dicoding
"""
```

Anda bisa mengganti whitespace dengan karakter lain:

```python
print('Dicoding'.rjust(20, '!'))

"""
Output:
!!!!!!!!!!!!Dicoding
"""
```

### `ljust()`

Kebalikan dari `rjust()` — membuat teks rata kiri:

```python
print('Dicoding'.ljust(20))

"""
Output:
Dicoding            
"""
```

### `center()`

Membuat teks rata tengah dengan menambahkan karakter pengisi di kiri dan kanan:

```python
print('Dicoding'.center(10, '-'))

"""
Output:
-Dicoding-
"""
```

> `zfill()`, `rjust()`, `ljust()`, dan `center()` bekerja dengan prinsip yang sama: memastikan panjang teks sesuai dengan nilai yang diminta.

---

## String Literals

Umumnya string ditulis dengan tanda petik tunggal. Namun, jika string mengandung petik tunggal di dalamnya (seperti `Jum'at`), Python akan salah mengira string berakhir lebih awal:

```python
st1 = 'Jum'at'   # SyntaxError
```

Solusi pertama — gunakan petik dua:

```python
st1 = "Jum'at"
```

Solusi kedua — gunakan *escape character* `\'`:

```python
st1 = 'Jum\'at'
```

### Escape Character

Escape character diawali dengan backslash (`\`) dan memungkinkan Anda memasukkan karakter khusus ke dalam string:

| Escape Character | Deskripsi |
|-----------------|-----------|
| `\'` | Single quote |
| `\"` | Double quote |
| `\t` | Tab |
| `\n` | Newline (line break) |
| `\\` | Backslash |

Contoh penggunaan:

```python
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""
```

---

## Raw String

Raw string mencetak string persis seperti yang ditulis, tanpa memproses escape character. Digunakan terutama untuk *regex*. Tambahkan huruf `r` sebelum string:

```python
print(r'Dicoding\tIndonesia')

"""
Output:
Dicoding\tIndonesia
"""
```

Perhatikan bahwa `\t` tidak dikonversi menjadi tab, melainkan dicetak apa adanya.
