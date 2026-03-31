# Class, Object, dan Method

Sebelum mengenal secara teknis class, object, dan method, mari kita berandai-andai sejenak untuk memahami konsep object-oriented programming (OOP).

Bayangkan Anda adalah seorang penggiat mobil, suatu waktu teman Anda yang berasal dari antah-berantah datang menghampiri. Kalian pun mulai berbincang dan dimulai dengan dia yang bertanya satu hal, "Apa itu mobil?".

![Ilustrasi pertanyaan tentang mobil](assets/dos-6e97620883795bc09cec63e7edb58afa20230822104950.jpeg)

Anda bisa menjawab, "Mobil adalah jenis kendaraan dengan empat roda yang memiliki kemampuan untuk bergerak maju, mundur, berbelok, dan berhenti. Mobil dapat melaju dengan kecepatan dari 0 hingga 160 km/jam. Mobil juga memiliki variasi warna yang beragam, termasuk merah, hitam, dan warna lainnya."

![Ilustrasi deskripsi mobil sebagai class](assets/dos-aa607e96f06ad021eca26737057ff53b20230822104951.jpeg)

Berdasarkan ilustrasi tersebut, mobil dapat dikatakan sebagai sebuah kelas (class). Perilaku (method) mobil tersebut adalah melaju, mundur, berbelok, dan berhenti. Mobil memiliki atribut warna yang bisa beragam (merah, hitam, dll.) serta kecepatan berkisar antara 0 hingga 160 km/jam.

Class dapat diibaratkan sebagai blueprint atau cetakan. Ketika class telah dibuat, Anda dapat membuat sebuah objek baru berdasarkan class tersebut. Objek baru ini memiliki karakteristik, atribut, dan perilaku sama dengan class yang menjadi cetakannya.

![Ilustrasi class Mobil dan objek turunannya](assets/dos-56ba7cc237efe8e9732873b59b4cb20020230822104950.jpeg)

Pada gambar di atas, kita memiliki sebuah kelas bernama Mobil dengan method bergerak maju, mundur, berbelok, dan berhenti. Dari kelas ini, kita bisa membuat objek baru, misalnya mobil Dicoding dengan warna biru.

Tidak hanya objek, Anda juga dapat membuat kelas baru untuk mewarisi kelas yang sudah ada.

![Ilustrasi pewarisan kelas MobilSport dari Mobil](assets/dos-80289924c5bab4c18d13fdbeaa95354220230822104951.jpeg)

Kelas MobilSport mewarisi atribut dan method dari kelas Mobil (induk), lalu menambahkan method baru yaitu turbo.

Secara umum, OOP adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atribut dan perilaku (method).

| Nama | Deskripsi | Contoh |
|------|-----------|--------|
| **Class (Kelas)** | Cetakan (blueprint) untuk membuat objek-objek yang memiliki karakteristik dan perilaku serupa | Mobil; Manusia |
| **Object (Objek)** | Perwujudan dari kelas | Mobil Dicoding; Budi, Herman, Asep |
| **Method** | Perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas | Maju, mundur, berbelok, berhenti |
| **Atribut** | Variabel yang menjadi identitas dari objek atau kelas | Warna, kecepatan, merek |

---

## Class

Keyword untuk membuat kelas dalam Python adalah `class`:

```python
class Mobil:
    pass
```

Pernyataan `pass` digunakan agar tidak menghasilkan error saat atribut dan method belum didefinisikan. Ingat bahwa class merupakan blok kode sehingga perlu memperhatikan indentasi.

Selanjutnya, tambahkan atribut pada kelas:

```python
class Mobil:
    # Atribut
    warna = "Merah"
```

---

## Object (Objek)

Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Kelas adalah bentuk abstrak dari objek — layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut **instansiasi**. Itulah sebabnya objek disebut juga sebagai *instance* atau *instance of the class*.

```python
class Mobil:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil()
print(mobil_1.warna)

"""
Output:
Merah
"""
```

Untuk memanggil atribut, sebutkan objek diikuti nama atributnya (`mobil_1.warna`).

![Ilustrasi akses atribut dari objek](assets/dos-5ffe37160dd30253772892c93802dcb520230822104950.jpeg)

Anda juga dapat mengubah nilai atribut dari objek:

```python
class Mobil:
    # Atribut
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)

"""
Output:
Biru
"""
```

---

## Atribut

Dalam Python, ada dua jenis atribut:

### Atribut Kelas

Atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat. Kelemahannya: ketika nilai atribut kelas diubah, perubahan tersebut memengaruhi **semua** objek yang dibuat dari kelas tersebut.

```python
class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
mobil2 = Mobil()

print(mobil1.warna)  # Merah
print(mobil2.warna)  # Merah

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)  # Hitam
print(mobil2.warna)  # Hitam
```

### Atribut Instance

Atribut yang terkait dengan instance atau objek itu sendiri, bukan kelas. Memungkinkan setiap objek memiliki atribut yang berbeda-beda. Untuk membuatnya, kita perlu menggunakan **class constructor**.

---

## Class Constructor

Class constructor adalah fungsi khusus `__init__` yang digunakan untuk menentukan nilai awal dari suatu kelas. Saat instansiasi, constructor dipanggil pertama kali.

```python
class Mobil:
    def __init__(self):
        self.warna = 'Merah'
```

Parameter `self` merujuk pada objek yang sedang diproses saat ini. Ini memungkinkan setiap objek memiliki atribut masing-masing tanpa saling memengaruhi:

```python
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)  # Merah
print(mobil_2.warna)  # Merah

# Mengubah atribut instance mobil_1 saja
mobil_1.warna = "Hitam"

print(mobil_1.warna)  # Hitam
print(mobil_2.warna)  # Merah (tidak berubah)
```

Parameter tambahan juga dapat ditambahkan dalam constructor:

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

> Jika parameter tidak memiliki nilai default, argumen wajib diberikan saat instansiasi. Jika tidak, program akan menghasilkan error.

---

## Method

Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Dalam pembuatan method, kita membuat fungsi di dalam kelas menggunakan keyword `def`. Python membagi method menjadi tiga jenis.

### Dekorator

Sebelum membahas jenis method, perlu dikenal konsep **dekorator** — fungsi dalam Python yang mengembalikan fungsi lain, diawali sintaks `@`:

```python
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""
```

Dekorator berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi tanpa mengubah kode aslinya.

### Object Method

Method yang melekat pada objek. Cirinya adalah adanya parameter `self` yang merujuk pada objek saat ini:

```python
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)  # 160

mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)  # 170
```

Perbedaan memanggil atribut vs method:
- Atribut: `mobil_1.kecepatan` (tanpa tanda kurung)
- Method: `mobil_1.tambah_kecepatan()` (dengan tanda kurung)

> Object method tidak bisa dipanggil langsung melalui kelasnya tanpa membuat objek terlebih dahulu.

### Static Method

Method yang bersifat independen dan tidak terikat pada instance kelas. Gunakan dekorator `@staticmethod`:

```python
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()       # Bisa dipanggil dari kelas
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()     # Bisa dipanggil dari objek

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""
```

### Class Method

Method yang memerlukan parameter yang merujuk pada kelas (bukan objek). Gunakan dekorator `@classmethod` dengan parameter `cls`:

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

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""
```

> Penamaan `cls` adalah konvensi programmer Python untuk memudahkan pembacaan kode. Anda dapat menggantinya dengan nama lain.

Ketika menggunakan class method, Python secara otomatis menambahkan kelas tersebut sebagai argumen pertama.
