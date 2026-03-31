# Rangkuman: Unit Testing

Kita sudah berada di penghujung materi Unit Testing. Sampai sejauh ini, Anda diharapkan telah paham terkait tes unit menggunakan library `unittest` pada Python. Sekarang, mari kita rangkum secara saksama.

---

## Pengantar Unit Testing

Saat membangun aplikasi atau program yang lebih kompleks, aplikasi tersebut akan memunculkan **dependensi** — satu atau lebih fungsi digunakan oleh fungsi lain. Dependensi tersebut tentu perlu dipastikan bahwa fungsionalitasnya dapat berjalan dengan baik dan tidak terganggu dengan adanya perubahan atau fungsi baru yang dibuat.

Di sinilah kita butuh **pengujian (test)** untuk fungsi-fungsi tersebut.

### Jenis Pengujian

| Jenis | Deskripsi |
|-------|-----------|
| **Manual testing** | Proses pengujian yang dilakukan oleh seseorang yang ditunjuk sebagai tester (penguji) |
| **Testing otomatis** | Pengujian yang dilakukan secara otomatis terhadap kode-kode yang kita bangun berdasarkan rencana pengujian (*test plan*) |
| **Integration testing** | Pengujian yang bertujuan untuk menguji suatu sistem sebagai satu kesatuan |
| **Unit testing** | Pengujian yang lebih spesifik dan fokus terhadap bagian-bagian kecil (fungsi, kelas, dll.) |

### Konsep Penting dalam unittest

Library `unittest` mendukung sejumlah konsep penting yang berorientasi objek:

| Konsep | Deskripsi |
|--------|-----------|
| **Test fixture** | Merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (*cleanup*) |
| **Test case** | Sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. `unittest` menyediakan basis class `TestCase` untuk membuat kasus pengujian baru |
| **Test suite** | Sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya |
| **Test runner** | Komponen yang mengatur eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna |

---

## Penerapan Unit Test dengan Library unittest

Untuk melakukan unit testing, gunakan library bawaan Python:

```python
import unittest
```

### Contoh Implementasi

```python
import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    # Test Fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")

    def tearDown(self):
        putus_koneksi_db(self.db)

    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif)  # tidak aktif secara default

    # Test Case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(self.dicoding.aktif)

if __name__ == "__main__":
    # Test Runner
    unittest.main()
```

### Poin Penting

- Kelas test harus merupakan turunan dari `unittest.TestCase`
- Semua metode test harus diawali dengan kata `test`
- Gunakan `setUp()` untuk mempersiapkan kondisi sebelum setiap test dijalankan
- Gunakan `tearDown()` untuk membersihkan kondisi setelah setiap test selesai
- Gunakan `unittest.main()` sebagai test runner di bagian akhir kode

### Assert Methods yang Umum Digunakan

| Method | Kegunaan |
|--------|----------|
| `assertEqual(a, b)` | Memastikan `a == b` |
| `assertTrue(x)` | Memastikan `x` bernilai `True` |
| `assertFalse(x)` | Memastikan `x` bernilai `False` |
| `assertRaises(Error)` | Memastikan exception tertentu dibangkitkan |
