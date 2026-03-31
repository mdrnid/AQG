# Percabangan dan Ternary Operators

**Control flow** adalah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir. Control flow memungkinkan program berjalan berdasarkan jalur eksekusi tertentu, meliputi:

- **Percabangan** — menjalankan kode berdasarkan kondisi tertentu
- **Perulangan** — mengulang blok kode secara berulang
- **Error handling** — mengontrol dan merespons kejadian yang tidak diinginkan

---

## Percabangan

Dalam pemrograman, kode program dapat berjalan berdasarkan kondisi tertentu — instruksi "Jika-maka" (*if-else*). Contoh dalam kehidupan sehari-hari:

> "Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Jika daging ayam tidak tersedia, maka Ibu akan membeli tempe sebagai pengganti."

![Ilustrasi percabangan ibu di pasar](assets/ilustrasi-percabangan-pasar.jpeg)

```python
ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
Output:
Ibu membeli dan memasak ayam
"""
```

---

### If

`if` mengecek apakah nilai variabel memenuhi kondisi tertentu. Jika `True`, blok kode di dalamnya dieksekusi.

![Ilustrasi struktur if statement](assets/struktur-if.jpeg)

```python
score = 100

if score == 100:
    print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""
```

Python menganggap nilai berikut sebagai `False`:

- Nilai yang sudah didefinisikan salah: `None` dan `False`
- Angka nol: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`
- Urutan/koleksi kosong: `""`, `()`, `{}`, `set()`, `range(0)`

`if` juga memiliki versi one-liner:

```python
score = 100

if score == 100: print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""
```

---

### Else

`else` dijalankan ketika kondisi `if` bernilai `False` — sebagai jalan keluar terakhir.

![Ilustrasi struktur if-else](assets/struktur-if-else.jpeg)

```python
tinggi_badan = 120

if tinggi_badan >= 160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

"""
Output:
Anda tidak diperbolehkan menaiki roller coaster
"""
```

---

### Elif

`elif` (else if) digunakan untuk menambah kondisi tambahan setelah `if`. Dapat digunakan lebih dari satu kali.

![Ilustrasi struktur if-elif-else](assets/struktur-if-elif-else.jpeg)

```python
nilai = 65

if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

"""
Output:
Hmm.. Anda mendapat nilai C
Ayo semangat!
"""
```

Anda juga dapat menggabungkan operator `and` atau `or` dalam kondisi percabangan:

```python
nilai = 81
perilaku = 'tidak baik'

if nilai >= 80 and perilaku == 'baik':
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != 'baik':
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi ya!")
else:
    print("Yuk belajar lebih giat lagi!")

"""
Output:
Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik
Perbaiki lagi ya!
"""
```

---

## Ternary Operators

Ternary operators adalah versi one-liner dari `if-else` — *conditional expressions* yang mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasilnya.

![Ilustrasi struktur ternary operator](assets/struktur-ternary.jpeg)

```python
lulus = True
print("selamat") if lulus else print("perbaiki")

"""
Output:
selamat
"""
```

Setara dengan bentuk blok:

```python
lulus = True
if lulus:
    print("Selamat")
else:
    print("Perbaiki")
```

### Ternary Tuples

Opsi lain menggunakan tuple — indeks `0` untuk kondisi `False`, indeks `1` untuk kondisi `True`:

![Ilustrasi struktur ternary tuples](assets/struktur-ternary-tuples.jpeg)

```python
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.", "Selamat, Anda lulus!")[lulus]
print(kelulusan)

"""
Output:
Selamat, Anda lulus!
"""
```

> Ternary tuples sebaiknya dihindari untuk kode yang kompleks karena dianggap kurang *pythonic* oleh komunitas Python.
