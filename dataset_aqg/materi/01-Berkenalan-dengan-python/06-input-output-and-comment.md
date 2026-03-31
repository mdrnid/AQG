# Input/Output dan Komentar

Pada bagian ini, Anda akan belajar tentang variabel yang nilainya tidak ditentukan oleh programmer, tetapi ditentukan oleh pengguna.

---

## Input

Untuk memungkinkan pengguna memberikan masukan, Anda dapat menggunakan fungsi `input()`. Berikut implementasinya:

```python
name = input('Masukan nama Anda: ')

"""
Output:
Masukan nama Anda: Perseus Evans
"""
```

Ketika kode tersebut dijalankan, program akan meminta pengguna untuk memasukkan nilai. Dalam contoh di atas, nilai yang dimasukkan adalah `'Perseus Evans'`.

---

## Output

Anda telah mengenal output dari materi sebelumnya — fungsi `print()` adalah perintah untuk menampilkan output ke layar komputer. Mari gabungkan `input()` dan `print()` berdasarkan contoh sebelumnya:

```python
name = input('Masukan nama Anda: ')
print(name)

"""
Output:
Masukan nama Anda: Perseus Evans
Perseus Evans
"""
```

Program akan meminta pengguna memasukkan nilai `'Perseus Evans'`, lalu menampilkan nilai tersebut ke layar menggunakan `print()`.

---

## Komentar

Sebagai programmer, Anda perlu memastikan kode yang dibuat dapat terbaca dan dipahami oleh programmer lain. Salah satu caranya adalah menggunakan **komentar** — barisan teks yang akan **diabaikan oleh Python** ketika program dijalankan.

Ada dua jenis komentar dalam Python:

---

### Inline Comment

Inline comment diletakkan pada baris yang sama dengan kode, atau satu baris sebelum kode. Digunakan untuk menjelaskan baris kode secara spesifik. Inline comment diawali dengan tanda `#`.

```python
# Variabel ini menyimpan nama 'Perseus Evans'
name = 'Perseus Evans'
```

Teks yang diawali dengan `#` akan dianggap sebagai komentar dan diabaikan oleh Python saat program dijalankan.

---

### Block Comment

Block comment digunakan untuk menjelaskan kode yang lebih kompleks atau membuat dokumentasi dari sebuah fungsi maupun modul. Block comment diapit oleh tiga tanda kutip — bisa menggunakan **triple double quote** (`"""`) atau **triple single quote** (`'''`).

**Menggunakan triple double quote (`"""`):**

```python
"""
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
"""
print("Hello World!")
```

**Menggunakan triple single quote (`'''`):**

```on
'''
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
'''
print("Hello World!")
```

Kedua cara tersebut sama-sama mengarahkan Python untuk menganggap teks di dalamnya sebagai komentar, sehingga tidak akan memunculkan error ketika dijalankan.


```