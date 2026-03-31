# Inheritance (Pewarisan)

Sebagaimana ilustrasi awal, kita dapat membuat sebuah kelas baru dengan menggunakan kelas induk yang sudah ada. Konsep ini disebut **inheritance** atau dalam bahasa Indonesia artinya pewarisan.

---

## Mekanisme Pewarisan

![Ilustrasi mekanisme pewarisan kelas](assets/dos-d33e86529030af3a78283af384ce923a20230822111858.jpeg)

Untuk melakukan pewarisan, anggap kita memiliki **kelas A** sebagai induk atau kelas dasar. Dari kelas A tersebut kita membuat kelas baru bernama **kelas B** sebagai kelas turunan. Ketika kelas B mewarisi kelas A, secara otomatis kelas ini memiliki semua atribut dan method yang dimiliki kelas A.

Hal yang perlu diperhatikan: jika kelas B memiliki nama method yang sama dengan kelas A, method tersebut akan **menimpa** method yang diwariskan oleh kelas A.

Mari lihat contohnya. Kita membuat kelas `Mobil` sebagai kelas dasar, lalu membuat kelas `MobilSport` yang mewarisinya dengan tambahan method `turbo`:

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50


# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)  # 160

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)  # 160

mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)  # 210
```

Perhatikan bagian kode berikut:

```python
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
```

Kelas `MobilSport` didefinisikan dengan menambahkan `Mobil` sebagai parameter. Dengan demikian, `MobilSport` mewarisi seluruh fitur dari kelas `Mobil` — atribut warna, merek, kecepatan, dan method `tambah_kecepatan`. Dalam kelas turunan, kita tidak perlu mendefinisikan ulang atribut tersebut.

---

## Override

Ketika kita membuat method baru di kelas turunan dengan nama yang **sama** seperti method di kelas induk, method baru tersebut akan menimpa (override) method dari kelas induk:

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10  # Tambah 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        self.kecepatan += 20  # Override: tambah 20


mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)   # 160
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)   # 180
```

> Penting: menimpa bukan berarti mengubah method dari kelas induk. Method kelas induk tetap berjalan seperti semula ketika dipanggil dari objek kelas induk.

Saat program dijalankan, Python akan mencari nama method di kelas turunan terlebih dahulu. Jika tidak ada, baru dicari di kelas induk.

---

## Super

Bagaimana jika kita ingin menggunakan method dari kelas induk sekaligus menambahkan perilaku baru, tanpa menulis ulang semua kode? Gunakan `super()`.

`super()` merujuk pada kelas induk (super class). Konsep ini membantu menghindari kode berulang dan memanfaatkan fungsi yang sudah ada:

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()  # Panggil method dari kelas induk
        print("Kecepatan Anda meningkat! Hati-Hati!")


mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)   # 160
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)   # 170
```

Pada method `tambah_kecepatan` di kelas `MobilSport`, kita menggunakan `super().tambah_kecepatan()` untuk menjalankan method dari kelas induk, lalu menambahkan perilaku baru berupa pesan peringatan.
