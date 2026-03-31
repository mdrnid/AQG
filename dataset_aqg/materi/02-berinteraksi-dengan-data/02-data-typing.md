# Data Typing

Sekarang Anda memahami bahwa komputer perlu mengetahui data yang diinginkan dengan cara melakukan deklarasi. Sebelum memahami berbagai tipe data yang umum digunakan dalam Python, Anda harus mengenal terlebih dahulu cara menuliskan data dalam pemrograman.

---

## Deklarasi dan Inisialisasi

**Deklarasi** merujuk pada pembuatan variabel dengan menentukan tipe data dan nama variabelnya. Umumnya, ini dilakukan oleh bahasa pemrograman lain seperti C/C++:

```c
int age;
float salary;
```

**Inisialisasi** merujuk kepada pemberian nilai awal pada variabel yang sebelumnya telah dideklarasikan:

```c
int age = 17;
float salary = 5000000;
```

Kedua proses tersebut wajib dilakukan dalam bahasa pemrograman seperti C. Beruntungnya, Python tidak mengharuskan Anda melakukan deklarasi tipe data variabel secara eksplisit. Hal ini disebabkan Python menerapkan ***loosely typed*** — artinya tipe data variabel tidak perlu dideklarasikan secara eksplisit.

---

## Loosely Typed

Kode C sebelumnya jika diubah ke dalam Python akan menjadi seperti berikut:

```python
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

"""
Output:
<class 'int'>
<class 'float'>
"""
```

---

## Dynamic Typing

Python juga menerapkan ***dynamic typing*** — artinya Python hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment. Hal ini memungkinkan tipe data dari suatu variabel berubah seiring berjalannya program:

```python
x = 6
print(type(x))

x = "6"
print(type(x))

"""
Output:
<class 'int'>
<class 'str'>
"""
```

Pada kode di atas, variabel `x` digunakan dua kali — pertama bertipe `int` dengan nilai `6`, lalu berubah menjadi bertipe `str` dengan nilai `"6"`.

---

Sekarang Anda paham cara mendeklarasikan variabel dan cara Python bekerja dengan tipe data. Selanjutnya, mari kita pelajari berbagai tipe data pada Python.


```