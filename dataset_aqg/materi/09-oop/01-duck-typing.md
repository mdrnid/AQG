# Duck Typing

> **Catatan:** Modul OOP ini bersifat opsional. Kita akan belajar Object-Oriented Programming (OOP) tidak secara mendalam, tetapi mendasar.

Python sering dikaitkan dengan konsep duck typing, yang berbunyi:

![Ilustrasi duck typing: "If it walks like a duck and it quacks like a duck, then it must be a duck"](assets/6736db1173b534e08da0308392a979ab20230822104414.jpeg)

Jika diterjemahkan ke dalam bahasa Indonesia: "Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek, kemungkinan besar ia adalah bebek."

Duck typing tidak berkaitan langsung dengan dynamic typing atau loosely typed. Konsep ini lebih erat dengan pemrograman berorientasi objek (OOP). Duck typing menjelaskan bahwa tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya.

Python memberikan keleluasaan kepada developer untuk tidak perlu mencemaskan tipe atau kelas dari sebuah objek — yang lebih penting adalah kemampuan melakukan operasinya (method).

Mari kita ambil contoh dengan fungsi `len()`. Fungsi ini menghitung panjang atau banyaknya elemen dari list, set, dan string. Bagaimana jika digunakan pada tipe data numerik seperti integer?

```python
i = 123
print(len(i))

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    print(len(i))
TypeError: object of type 'int' has no len()
"""
```

Python menghasilkan error yang menyatakan bahwa objek integer tidak memiliki `len()`.

![Pesan error: object of type 'int' has no len()](assets/e1402b022c797d734d6208d2440508b520230822104414.jpeg)

Pesan error tersebut menyatakan bahwa objek dengan tipe data `int` tidak memiliki method `len()` yang diharapkan. Python secara alami memeriksa apakah object yang Anda buat memiliki method yang diharapkan atau tidak.

Inilah inti dari duck typing — Python tidak peduli tipe datanya, yang penting apakah method yang dibutuhkan tersedia atau tidak.

Baiklah, mari kita mulai perjalanan untuk mempelajari class, object, dan method.
