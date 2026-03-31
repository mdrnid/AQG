# Memformat Kode

Jika proses lint atau linting hanya melakukan pengecekan, kali ini adalah arahan gaya penulisan kode agar bisa sesuai dengan PEP8. Kita akan menggunakan beberapa aplikasi yang perlu diinstal terlebih dahulu.

Proses memformat kode akan sama dengan cara melakukan proses linting, yaitu kita akan mengeksekusi script. Perbedaannya adalah output yang dihasilkan. Jika proses linting menghasilkan pesan dengan menunjukkan baris dan kode yang mengalami kesalahan, proses memformat kode akan memberikan pesan berupa kode yang telah diperbaiki — artinya Anda tidak perlu mengubah kode secara manual.

Berikut adalah tiga jenis aplikasi untuk memformat kode. Tidak harus semuanya diinstal, hanya paket yang menurut Anda sesuai kebutuhan saja yang digunakan.

---

## Aplikasi Formatter

### black

`black` adalah proyek open source yang dikembangkan di repository Python Software Foundation (PSF) dengan lisensi MIT. Untuk mendapatkan gambaran, versi online (tidak resmi) ada di [https://black.now.sh](https://black.now.sh).

```bash
pip install black
```

### YAPF (Yet Another Python Formatter)

YAPF adalah proyek open source yang dikembangkan di repository Google dengan lisensi Apache.

```bash
pip install yapf
```

### autopep8

`autopep8` adalah proyek open source (berlisensi MIT) yang termasuk paling awal untuk memformat kode dengan bantuan lint `pycodestyle`.

```bash
pip install autopep8
```

---

## Cara Kerja Formatter

Kita akan menggunakan kode yang sama seperti sebelumnya. Buka `kalkulator.py` dan salin kode berikut:

```python
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
        return self.i - _i
```

Buka terminal, pastikan berada di direktori tempat file berada, lalu jalankan salah satu perintah berikut.

### Menggunakan black

```bash
black kalkulator.py
```

Ketika Anda menjalankan perintah di atas, kode yang berada di dalam `kalkulator.py` akan langsung mengalami perubahan. Silakan cek kembali kode dalam file Anda.

### Menggunakan yapf

```bash
yapf kalkulator.py
```

Berbeda dengan `black`, `yapf` tidak mengubah kode Anda secara langsung. Sebaliknya, `yapf` akan memberikan saran kode melalui terminal.

![Tampilan terminal menunjukkan saran kode yang telah diperbaiki oleh yapf](assets/dos-cf1f60b0fa519d9814e994ff3e37fbd220230823193800.png)

### Menggunakan autopep8

Cara kerja `autopep8` dapat seperti `yapf` (memberi saran ke terminal) atau seperti `black` (mengubah langsung isi file).

Untuk mendapatkan saran kode:

```bash
autopep8 kalkulator.py
```

![Tampilan terminal menunjukkan saran kode yang telah diperbaiki oleh autopep8](assets/dos-30f97cfbed4e720b5a76ef2b2ff807b920230823193847.png)

Untuk mengubah kode file secara langsung:

```bash
autopep8 --in-place --aggressive --aggressive kalkulator.py
```

---

## Kesimpulan

Setelah mempelajari kedua mekanisme — pengecekan gaya penulisan (style guide) dan proses memformat kode — Anda tinggal fokus dengan penulisan indentasi dalam kode Python. Untuk format sisanya, aplikasi-aplikasi yang telah kita pelajari di atas dapat membantu.

Jika Anda menulis dengan editor kode yang sangat sederhana (seperti Notepad di Windows atau nano di Linux), cukup perhatikan indentasi untuk setiap baris pernyataan (statement). Setelah selesai, simpan kodenya sebagai file `.py`, lalu eksekusi perintah linter atau formatter. Hasilnya, kode Anda sudah dirapikan sesuai arahan gaya penulisan PEP8.

Untuk pengguna PyCharm, secara bawaan sudah menggunakan fitur inspeksi dengan kemampuan yang kurang lebih sama. Namun jika Anda mau, bisa juga menambahkan aplikasi lint yang sudah dijelaskan sebagai tambahan. Fitur format ulang kode juga tersedia secara bawaan di PyCharm.
