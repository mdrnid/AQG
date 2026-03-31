# Variable dan Assignment

Sekarang mari kita masuk ke pembahasan lebih mendalam tentang pembuatan kode program pada Python.

Ketika membuat kode program, Anda menuliskan serangkaian instruksi yang nantinya akan dijalankan oleh komputer. Dalam Python, setiap kode adalah instruksi untuk memberi tahu komputer hal yang harus dilakukan selanjutnya. Misalnya pada perintah berikut yang memerintahkan komputer untuk mencetak teks `"Hello World!"`:

```python
print("Hello World!")
```

Teks tersebut sebenarnya adalah data bertipe *string* (Anda akan mempelajari lebih dalam pada materi "Berkenalan dengan Tipe Data"). Umumnya, setiap data yang digunakan akan disimpan dalam variabel — sehingga ketika membutuhkan kembali data tersebut, Anda cukup memanggil variabel yang telah dibuat.

---

## Variable

Variabel merujuk kepada lokasi dalam komputer yang digunakan untuk **menyimpan nilai dengan tipe data tertentu**. Ketika menuliskan variabel, Anda memerintahkan komputer untuk mencari dan memesan ruang kosong yang nantinya akan diisi nilai atau data.

Tujuan dari pembuatan variabel adalah menyimpan nilai yang dapat digunakan secara berulang. Pembuatan variabel sangat erat kaitannya dengan proses *assignment*.

---

## Assignment

Assignment merupakan proses **pemberian atau penetapan nilai pada sebuah variabel**. Dalam Python, proses assignment mengikuti formula berikut:

```
<Ruas Kiri> = <Ruas Kanan>
```

> **Catatan:**
> - **Ruas kiri** adalah variabel.
> - **Ruas kanan** adalah ekspresi, nilai, atau variabel yang sudah jelas nilainya.
>
> Kita akan mempelajari ekspresi lebih detail pada materi ekspresi. Saat ini cukup pahami bahwa ruas kanan dapat berupa ekspresi, nilai, maupun variabel.

### Contoh 1: Assignment Sederhana

```python
greeting = 'Hello World!'   # Ini adalah assignment
print(greeting)

"""
Output: Hello World!
"""
```

Pada kode di atas, teks `'Hello World!'` disimpan pada variabel `greeting`. Setelah proses assignment tersebut, variabel `greeting` memiliki nilai `'Hello World!'`.

### Contoh 2: Assignment dengan Ekspresi dan Variabel Lain

```python
"""
addition adalah variabel yang bernilai ekspresi 2+2,
result adalah hasil pengurangan dari variabel addition dikurangi 1
"""

addition = 2 + 2
result = addition - 1
print(result)

"""
Output: 3
"""
```

Pada kode di atas:
- `addition` menyimpan hasil dari ekspresi `2 + 2`, yaitu `4`.
- `result` menyimpan hasil dari `addition - 1`, yaitu `3`.
- `print(result)` menampilkan nilai `3` ke layar.
