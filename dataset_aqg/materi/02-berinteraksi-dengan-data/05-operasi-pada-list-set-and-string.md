# Operasi pada List, Set, dan String

Dalam modul ini, Anda akan belajar mengenai berbagai operasi pada list, set, dan string menggunakan fungsi bawaan Python.

---

## `len()`

Fungsi `len()` menghitung panjang atau banyaknya elemen dari list, set, dan string. Khusus pada string, program akan menghitung jumlah karakternya.

**List:**

```python
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""
```

**Set:**

```python
contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_set)
print(len(contoh_set))

"""
Output:
{1, 3, 5, 7, 9}
5
"""
```

Setelah dikonversi ke set, duplikat dihapus sehingga jumlah anggota berkurang dari 9 menjadi 5.

**String:**

```python
contoh_string = "Belajar Python"

print(contoh_string)
print(len(contoh_string))

"""
Output:
Belajar Python
14
"""
```

> Karakter spasi dihitung sebagai bagian dari string.

---

## `min()` dan `max()`

Fungsi `min()` dan `max()` mengembalikan nilai terkecil dan terbesar dari suatu list:

```python
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

"""
Output:
5
96
"""
```

---

## `count()`

Fungsi `count()` menghitung berapa kali suatu objek muncul dalam list atau string.

**Pada list:**

```python
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

"""
Output:
3
"""
```

**Pada string:**

```python
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

"""
Output:
6
"""
```

---

## Operator `in` dan `not in`

Operator `in` dan `not in` digunakan untuk mengecek apakah suatu nilai ada dalam list atau string. Keduanya mengembalikan nilai boolean `True` atau `False`:

```python
kalimat = "Belajar Python di Dicoding sangat menyenangkan"

print('Dicoding' in kalimat)      # True  — ada dalam kalimat
print('tidak' in kalimat)         # False — tidak ada dalam kalimat
print('Dicoding' not in kalimat)  # False — kebalikan dari baris pertama
print('tidak' not in kalimat)     # True  — kebalikan dari baris kedua

"""
Output:
True
False
False
True
"""
```

---

## Memberikan Nilai untuk Multiple Variable

Secara konvensional, Anda mengakses elemen list satu per satu:

```python
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
```

Python memungkinkan Anda melakukan hal yang sama dalam satu baris (*unpacking*):

```python
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

"""
Output:
['shirt', 'white', 'L']
shirt
white
L
"""
```

> Jumlah variabel di sebelah kiri harus sama dengan jumlah elemen dalam list atau tuple. Jika tidak, Python akan menghasilkan error.

---

## `sort()`

Fungsi `sort()` mengurutkan elemen dalam list secara *ascending* (menaik) secara default:

```python
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['helikopter', 'mobil', 'motor', 'pesawat']
"""
```

Beberapa hal penting tentang `sort()`:

**1. Membalik urutan dengan `reverse=True`:**

```python
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
['pesawat', 'motor', 'mobil', 'helikopter']
"""
```

**2. Tidak dapat mengurutkan list yang berisi campuran angka dan string:**

```python
urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()

"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""
```

**3. Menggunakan urutan ASCII — huruf kapital diurutkan sebelum huruf kecil:**

```python
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""
```

[ASCII Table](https://www.asciitable.com/) memetakan karakter ke nilai angka. Metode `sort()` mengurutkan berdasarkan nilai angka ASCII tersebut.

Untuk mengatasi perbedaan kapital, gunakan parameter `key=str.lower` agar semua elemen dianggap lowercase saat diurutkan (tanpa mengubah nilai aslinya):

```python
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)

print(kendaraan)

"""
Output:
['helikopter', 'mobil', 'motor', 'Pesawat']
"""
```
