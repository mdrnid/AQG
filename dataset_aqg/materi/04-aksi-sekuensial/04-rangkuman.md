# Rangkuman: Aksi Sekuensial

Kita sudah berada di penghujung materi Aksi Sekuensial. Sampai sejauh ini, Anda telah memiliki pemahaman mengenai aksi sekuensial Python yang menjadi ilmu mendasar dalam pemrograman. Mari kita rangkum secara saksama.

---

## Pengenalan Aksi Sekuensial

**Aksi sekuensial** adalah sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya. Dalam Python, kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya.

Perlu diperhatikan:
- Ada program yang **akan berubah** hasilnya jika urutan baris instruksinya diubah.
- Ada program yang **tidak akan berubah** hasilnya jika urutan baris instruksinya diubah.

---

## Python Interpreter

Kode program Python akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan **compiler** atau **interpreter**:

- **Compiler** — menerjemahkan seluruh program menjadi bahasa mesin *sebelum* dijalankan.
- **Interpreter** — menerjemahkan kode Python *satu per satu* secara langsung, memungkinkan Anda melihat hasil segera setelah setiap baris dieksekusi.

---

## Block Code

Sebuah program Python dibangun berdasarkan **blok-blok kode** — potongan kode yang dijalankan sebagai satu unit. Blok kode dapat berupa modul, fungsi, dan kelas. Contoh blok kode perulangan `for`:

```python
for i in range(10):
    print(i)
```

Python sangat memperhatikan **indentasi** untuk menentukan batas awal dan akhir sebuah blok kode.

---

## Case-sensitive

Python adalah bahasa pemrograman **case-sensitive** — huruf besar dan kecil diperlakukan sebagai karakter yang berbeda:

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

Variabel `teks` dan `Teks` dianggap sebagai dua variabel yang berbeda oleh Python.

---

## One-liner

**One-liner** adalah gaya penulisan Python yang memungkinkan Anda membuat kode hanya dalam satu baris — singkat dan jelas. Salah satu contohnya adalah program penukaran dua variabel:

```python
x = 1
y = 2

x, y = y, x    # One-liner: menukar nilai x dan y
```

Tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas.
