# Rangkuman: Object-Oriented Programming (OOP)

Kita sudah berada di penghujung materi Object-Oriented Programming (OOP). Sampai sejauh ini, Anda diharapkan paham untuk mengimplementasikan konsep OOP ke dalam setiap program yang Anda bangun. Mari kita rangkum secara saksama.

---

## Duck Typing

Duck typing adalah konsep yang menjelaskan bahwa tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya. Konsep ini berbunyi:

> "If it walks like a duck and it quacks like a duck, then it must be a duck."

Python memberikan keleluasaan kepada developer untuk tidak perlu mencemaskan tipe atau kelas dari sebuah objek — yang lebih penting adalah kemampuan melakukan operasinya (method).

---

## Class, Object, dan Method

Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atribut dan perilaku (method).

| Nama | Deskripsi | Contoh |
|------|-----------|--------|
| **Class (Kelas)** | Cetakan (blueprint) untuk membuat objek-objek dengan karakteristik dan perilaku yang serupa | Mobil; Manusia |
| **Object (Objek)** | Turunan atau perwujudan dari kelas | Mobil Dicoding; Budi, Herman, Asep |
| **Method** | Perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas | Maju, mundur, berbelok, berhenti |
| **Atribut** | Variabel yang menjadi identitas dari objek atau kelas | Warna, kecepatan, merek |

---

## Class

Keyword untuk membuat kelas dalam Python adalah `class`:

```python
class Mobil:
    pass
```

---

## Object (Objek)

Kelas adalah bentuk abstrak dari objek — layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut **instansiasi**. Itulah sebabnya objek disebut juga sebagai *instance* atau *instance of the class*.

```python
class Mobil:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil()
```

---

## Atribut

Ada dua jenis atribut dalam Python:

### Atribut Kelas

Atribut yang melekat pada kelas dan menjadi bawaan ketika membuat sebuah instance:

```python
class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)  # Merah
```

### Atribut Instance

Atribut yang terkait dengan instance atau objek itu sendiri, bukan kelas. Dibuat melalui class constructor:

```python
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'

mobil_1 = Mobil()
print(mobil_1.warna)  # Merah
```

---

## Class Constructor

Class constructor adalah fungsi khusus `__init__` yang digunakan untuk menentukan nilai atau kondisi awal dari suatu kelas. Saat instansiasi, constructor dipanggil pertama kali.

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)      # Merah
print(mobil_1.merek)      # DicodingCar
print(mobil_1.kecepatan)  # 160
```

---

## Method

Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Dibuat menggunakan keyword `def` di dalam kelas. Ada tiga jenis method:

### Object Method

Method yang melekat pada objek, ditandai dengan parameter `self`:

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10
```

### Static Method

Method yang bersifat independen dan tidak terikat pada instance kelas. Gunakan dekorator `@staticmethod`:

```tic mn
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()
```

### Class Method

Method yang memerlukan parameter yang merujuk pada kelas. Gunakan dekorator `@classmethod` dengan parameter `cls`:

```python
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()
```

---

## Inheritance (Pewarisan)

### Mekanisme Pewarisan

![Ilustrasi mekanisme pewarisan](assets/dos-474361acb56f38d3f5de58bdadf63efd20230822112439.jpeg)

Kelas turunan mewarisi semua atribut dan method dari kelas induk. Jika kelas turunan memiliki method dengan nama yang sama, method tersebut akan menimpa method dari kelas induk.

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
```

### Override

Membuat method baru di kelas turunan dengan nama yang sama akan menimpa (override) method dari kelas induk:

```python
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):  # Override
        self.kecepatan += 20
```

### Super

`super()` digunakan untuk memanggil method dari kelas induk tanpa menulis ulang semua kode:

```python
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()  # Panggil method kelas induk
        print("Kecepatan Anda meningkat! Hati-Hati!")
```

    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()     # Super
        print("Kecepatan Anda meningkat! Hati-Hati!")