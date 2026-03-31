# Python Interpreter

Python termasuk bahasa pemrograman yang mudah dimengerti oleh manusia karena sintaksnya yang mudah dipahami. Namun, proses komputer menjalankan kode yang Anda bangun tidak sesederhana itu.

Kode dari program Python akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan program **compiler** atau **interpreter**.

- **Compiler** — menerjemahkan seluruh program menjadi bahasa mesin *sebelum* dijalankan, lalu menghasilkan output.
- **Interpreter** — menerjemahkan kode Python *satu per satu* dan menghasilkan output secara langsung, memungkinkan Anda melihat hasil segera setelah setiap baris dieksekusi.

![Ilustrasi perbedaan compiler dan interpreter](assets/compiler-vs-interpreter.jpeg)

Implementasi interpreter ada pada mode interaktif Python. Anda dapat menjalankan satu atau beberapa baris kode secara langsung dan melihat hasilnya.

---

## Block Code

Sebuah program Python dapat berupa pernyataan (*statement*) tunggal atau terdiri atas **blok kode**. Sebuah blok merujuk pada potongan kode program Python yang dijalankan sebagai satu unit — dapat berupa modul, fungsi, kelas, control flow, dan sebagainya.

Contoh blok kode perulangan (akan dipelajari lebih detail pada materi Control Flow):

```python
for i in range(10):
    print(i)

"""
Output:
0
1
2
3
4
5
6
7
8
9
"""
```

Kode di atas merupakan satu unit blok perulangan yang mencetak angka 0 hingga 9. Perhatikan bahwa blok ini juga menerapkan aksi sekuensial — setiap iterasi dijalankan berurutan hingga kondisi akhir terpenuhi.

### Indentasi

Python sangat memperhatikan **indentasi**. Indentasi tidak hanya merapikan kode, tetapi juga menjelaskan batas awal dan akhir sebuah blok kode. Tanpa indentasi yang benar, program akan menghasilkan error:

```python
for i in range(10):
print(i)

"""
Output:
IndentationError: expected an indented block
"""
```

Error terjadi karena interpreter menganggap `print(i)` bukan bagian dari blok `for`. Indentasi yang benar (biasanya 4 spasi) diperlukan untuk menyatakan kode blok secara utuh.

---

## Case-sensitive

Python adalah bahasa pemrograman yang **case-sensitive** — huruf besar dan kecil diperlakukan sebagai karakter yang berbeda dalam penamaan variabel, fungsi, atau penulisan kode secara umum.

```python
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)

"""
Output:
Dicoding
Indonesia
"""
```

Variabel `teks` dan `Teks` dianggap sebagai dua variabel yang berbeda oleh Python. Jika Anda mencoba mengakses variabel dengan kapitalisasi yang tidak terdefinisi, Python akan menghasilkan error:

```python
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)
print(TEks)

"""
Output:
Dicoding
Indonesia
NameError: name 'TEks' is not defined
"""
```

Variabel `teks`, `Teks`, dan `TEks` dianggap sebagai tiga variabel yang berbeda.
