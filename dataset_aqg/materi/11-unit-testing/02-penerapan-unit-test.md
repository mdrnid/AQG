# Penerapan Unit Test dengan Library unittest

Sekarang mari kita pelajari cara implementasinya. Materi kali ini akan menggunakan PyCharm sebagai IDE-nya. Silakan ikuti sembari menggunakan IDE Anda, seperti Visual Studio Code atau PyCharm.

---

## Contoh Pertama: Pengujian String

Tulis kode ini pada IDE Anda dan simpan dalam format `.py`, lalu jalankan pada Command Prompt.

```python
import unittest

class TestStringMethods(unittest.TestCase):
    # Test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')

if __name__ == '__main__':
    # Test Runner
    unittest.main()
```

Jalankan program di atas dengan mengeksekusi file yang telah Anda buat:

```bash
python <nama-file>.py
```

![Tampilan output ketiga test berhasil](assets/dos-dd039517cb4f60e8e57680c5f914b2ac20230823200731.jpeg)

### Penjelasan Kode

- **`TestStringMethods`** adalah kelas turunan (*subclass*) dari `unittest.TestCase` sehingga proses tes dapat dilangsungkan tanpa banyak implementasi lain.
- Ketiga metode diawali dengan kata `test` — ini adalah konvensi wajib untuk menginformasikan ke test runner bahwa metode tersebut merepresentasikan tes yang akan dioperasikan.
- **`test_strip`** — menggunakan `assertEqual` untuk memastikan bahwa `'www.dicoding.com'.strip('c.mow')` sama dengan `'dicoding'`.
- **`test_isalnum`** — menggunakan `assertTrue` untuk memastikan `'c0d1ng'.isalnum()` bernilai benar, dan `assertFalse` untuk memastikan `'c0d!ng'.isalnum()` bernilai salah karena ada karakter `!` yang bukan alfanumerik.
- **`test_index`** — menggunakan `assertEqual` untuk memastikan substring `coding` menempati index `2`, dan `assertRaises(ValueError)` untuk memastikan `ValueError` dibangkitkan ketika pencarian index tidak berhasil ditemukan.
- **`unittest.main()`** di bagian terakhir digunakan untuk mulai menjalankan test.

### Memahami Output

Tampak pada keluaran bahwa ada tiga tanda titik `(...)` yang menyatakan bahwa ketiga fungsi yang dites berhasil melewati tes. Dirangkum juga waktu pemrosesan dari total tiga tes tersebut serta di baris paling akhir adalah rangkuman bahwa semua test berlangsung sukses (`OK`).

---

## Melihat Output Kegagalan

Coba buat salah satu test gagal. Misalnya pada metode `test_isalnum`, ubah keduanya menggunakan `assertTrue`:

```python
def test_isalnum(self):
    self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
    self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal
```

Jalankan kembali program Anda. Keluarannya akan seperti berikut:

![Tampilan output ketika ada test yang gagal](assets/dos-109eabb58cf01556be65cdb084268fbf20230823200731.jpeg)

Penjelasan output:

- Tertulis `.F.` yang menggambarkan bahwa pengujian metode kedua gagal (`FAIL`).
- Dijelaskan bahwa kegagalan ada dalam metode `test_isalnum` dari class `__main__.TestStringMethods`.
- Diinformasikan bahwa `test_isalnum` yang gagal berada pada baris ke-10, yakni pada pengecekan `self.assertTrue('c0d!ng'.isalnum())` yang memang tadi kita ubah dari `assertFalse`. Sistem pengujian melaporkan bahwa `False` tidak bernilai benar seperti yang diharapkan oleh `assertTrue`.
- Rekap totalnya ada tiga tes yang dilakukan, dengan satu buah kegagalan (*failure*).

---

## Contoh Kedua: Pengujian Kelas User

Sekarang kita coba pengujian dengan contoh yang lebih nyata — kita memiliki class `User` dan akan menguji aktif atau tidaknya user dengan melihat apakah dia terkoneksi ke basis data (db) atau tidak.

```python
import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    # Test Case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif)  # tidak aktif secara default
        putus_koneksi_db(db)

    # Test Case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)

if __name__ == "__main__":
    # Test Runner
    unittest.main()
```

Jika Anda perhatikan kembali kode di atas, kita melakukan beberapa tindakan yang berulang — memanggil fungsi koneksi ke basis data dan membuat `User` dicoding setiap kali proses tes. Hal ini karena setiap tes dioperasikan secara terpisah. Tindakan ini dianggap bukan praktik yang baik karena memakan lebih banyak memori, apalagi jika program yang kita uji berukuran besar.

---

## Test Fixture: setUp dan tearDown

Kita bisa memperbaikinya dengan menerapkan konsep **test fixture**. Konsep ini merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (*cleanup*).

Kita akan menggunakan dua metode bawaan dari class `TestCase`:

- **`setUp()`** — dipanggil tiap sebelum metode tes dilaksanakan, bertujuan untuk mempersiapkan pengujian.
- **`tearDown()`** — dipanggil setiap metode tes selesai dilaksanakan, bertindak untuk membersihkan meskipun terjadi kesalahan (*exception*) pada proses tes.

Ubah class `TestUser` dengan implementasi kedua metode tersebut:

```python
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
```

Jalankan kembali program Anda. Keluarannya seperti berikut:

![Tampilan output dengan setUp dan tearDown](assets/dos-4eb329bb43593006cf8ec7d8883f3acd20230823200731.jpeg)

Terlihat bahwa setiap kali melakukan pengujian, metode `setUp()` dipanggil. Begitu juga setelah selesai pengujian, metode `tearDown()` dipanggil.

Dengan kemampuan pengujian ini, aplikasi yang Anda buat jadi lebih teruji atau biasa disebut dengan istilah lebih **tahan banting** (*robust*).
