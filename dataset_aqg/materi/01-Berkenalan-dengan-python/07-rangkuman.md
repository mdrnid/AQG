# Rangkuman: Berkenalan dengan Python

Kita sudah berada di penghujung materi pertama. Sampai sini Anda sudah memiliki pengetahuan mendasar mengenai Python. Mari kita rangkum secara saksama.

---

## Pengenalan Python

Python adalah bahasa pemrograman multifungsi yang dirilis pada tahun **1991** oleh **Guido van Rossum (GvR)**. Beliau membuat Python sebagai bahasa pemrograman yang mudah dibaca dan dimengerti (*readable*) serta memiliki kemampuan penanganan kesalahan (*exception handling*).

Salah satu ciri khas Python yang paling dikenal adalah Python tidak mewajibkan penggunaan titik koma atau semi colon (`;`) pada setiap akhir kode programnya.

---

## Bersiap Membuat Kode Program di Lokal

Untuk menjalankan program Python di lokal komputer, Anda perlu mempersiapkan dua hal:

1. **Menginstal Python** — Anda dapat mengunduhnya di [python.org/downloads](https://www.python.org/downloads/).
2. **Menyiapkan IDE** — aplikasi yang menyediakan fasilitas komprehensif untuk pengembangan aplikasi, termasuk kode editor.

Beberapa IDE populer untuk Python:

- **Visual Studio Code** — IDE populer yang menyediakan ribuan plugin untuk membantu programmer membuat program dengan berbagai bahasa pemrograman.
- **PyCharm** — IDE yang dibuat khusus untuk pengembangan aplikasi Python, dilengkapi fitur-fitur khusus untuk mempermudah proses pengembangan.
- **Jupyter Notebook** — IDE berbasis web yang memungkinkan Anda membuat dan berbagi kode program. Terdiri dari sel-sel yang dapat dijalankan satu per satu.
- **Google Colaboratory** — IDE berbasis web online dengan fungsi serupa Jupyter Notebook, tanpa perlu instalasi.

---

## Menjalankan Kode Program di Lokal

Ada tiga mode untuk menjalankan kode Python di lokal komputer:

- **Kode Interaktif** — menjalankan kode Python langsung dari terminal atau command prompt, cocok untuk eksplorasi dua hingga tiga baris kode.
- **Script** — membuat file berekstensi `.py` lalu mengeksekusinya. Mode ini paling sering digunakan oleh programmer.
- **Notebook** — lingkungan pengembangan interaktif seperti Jupyter Notebook atau Google Colaboratory.

---

## Variable dan Assignment

**Variabel** adalah lokasi dalam komputer yang digunakan untuk menyimpan nilai dengan tipe data tertentu. **Assignment** adalah proses pemberian atau penetapan nilai pada sebuah variabel, dengan format:

```
<Ruas Kiri> = <Ruas Kanan>
```

- **Ruas kiri** adalah variabel.
- **Ruas kanan** dapat berupa ekspresi, nilai, atau variabel yang sudah jelas nilainya.

---

## Input/Output dan Komentar

Dalam membuat kode program, Anda dapat menetapkan nilai secara langsung atau mengizinkan pengguna menentukannya melalui **input**. Gunakan fungsi `input()` untuk menerima masukan dari pengguna, dan `print()` untuk menampilkan output ke layar.

Selain itu, Anda dapat memberikan **komentar** pada kode untuk memberikan konteks bagi programmer lain. Komentar diabaikan oleh Python saat program dijalankan. Ada dua tipe komentar:

### Inline Comment

Diawali dengan tanda `#`, diletakkan pada baris yang sama dengan kode atau satu baris sebelumnya:

```python
# Variabel ini menyimpan nama 'Dicoding Indonesia'
name = 'Dicoding Indonesia'
```

### Block Comment

Mengapit blok teks dengan tiga tanda kutip — `"""` atau `'''`:

```python
"""
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
"""
print("Hello World!")
```

```python
'''
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
'''
print("Hello World!")
```

Kedua cara tersebut mengarahkan Python untuk mengabaikan teks di dalamnya sehingga tidak memunculkan error.
