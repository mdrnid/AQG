# Pengenalan Aksi Sekuensial

Selama mempelajari beberapa materi pertama kelas ini, Anda telah membuat banyak program sederhana. Ke depannya, Anda akan membuat kode program yang tidak hanya terdiri dari satu baris, tetapi bisa banyak baris dan lebih kompleks.

Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara **sekuensial**. Artinya, kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. **Aksi sekuensial** adalah sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya.

Program yang Anda bangun haruslah memiliki awal dan akhir — sehingga ketika dijalankan, bisa diketahui waktu berakhirnya. Simak contoh implementasinya:

```python
print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)

print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")

"""
Output:
Selamat datang dalam program Python!

Silakan masukkan data diri Anda:
Masukkan nama Anda: Evans
Masukkan tahun lahir Anda: 2005
Selamat datang Evans dalam program Python, per 2023 umur Anda adalah 18 tahun.

Terima kasih telah menggunakan program Python!
"""
```

Mari bedah kode tersebut:

1. Komputer menjalankan baris pertama — menampilkan teks `"Selamat datang dalam Program Python"`.
2. Baris kedua dijalankan — menampilkan teks `"Silakan masukkan data diri Anda."`.
3. Baris ketiga dijalankan — program meminta input nama dan menyimpannya ke variabel `nama`.
4. Baris keempat dijalankan — program meminta input tahun lahir dan menyimpannya ke variabel `tahun_lahir`.
5. Variabel `tahun_lahir` dikalkulasikan untuk mengetahui umur per 2023, hasilnya disimpan ke variabel `umur`.
6. Program menampilkan pesan sambutan dengan nilai dari variabel `nama` dan `umur`.
7. Program ditutup dengan menampilkan teks penutup.

---

## Urutan Instruksi dan Pengaruhnya

Perlu diperhatikan bahwa ada program yang **akan berubah** hasilnya jika urutan baris instruksinya diubah, dan ada yang **tidak akan berubah**.

### Contoh: Urutan tidak mempengaruhi hasil

```python
a = 6
b = 9

result = a + b
print(result)

"""
Output:
15
"""
```

Jika urutan inisialisasi variabel `a` dan `b` diubah:

![Ilustrasi perubahan urutan variabel a dan b](assets/urutan-variabel-ab.jpeg)

```python
a = 9
b = 6

result = a + b
print(result)

"""
Output:
15
"""
```

Hasil tetap `15` karena operasi penjumlahan bersifat komutatif.

---

### Contoh: Urutan mempengaruhi hasil

```python
a = 6
b = 9

print(a**2)
print(b//3)

"""
Output:
36
3
"""
```

Jika urutan `print()` diubah:

![Ilustrasi perubahan urutan print](assets/urutan-print.jpeg)

```python
a = 6
b = 9

print(b//3)
print(a**2)

"""
Output:
3
36
"""
```

Hasil berbeda karena urutan perintah `print()` menentukan urutan output yang ditampilkan.

Memahami hal ini penting untuk membantu menemukan kesalahan sintaks ketika membuat program yang kompleks.
