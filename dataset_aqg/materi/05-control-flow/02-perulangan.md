# Perulangan

Dalam kehidupan sehari-hari, sering kali kita menemui situasi yang harus dilakukan berulang kali. Dalam pemrograman pun sama — daripada menulis kode berulang seperti ini:

```python
print(1)
print(2)
print(3)
# ... hingga 10
```

Python menyediakan sintaks perulangan untuk membuat kode yang lebih efektif dan mudah dibaca.

---

## For

`for` adalah sintaks perulangan yang bersifat **definite iteration** — jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

![Format perulangan for](assets/format-for.jpeg)

- `<iterable>` — objek Python yang dapat diiterasi seperti list, tuple, atau string
- `<var>` — variabel yang mengambil elemen berikutnya dari `<iterable>` setiap iterasi

```python
var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in var_list:
    print(i)

"""
Output:
1
2
3
4
5
6
7
8
9
10
"""
```

### Fungsi `range()`

Anda dapat melakukan perulangan berdasarkan panjang tertentu menggunakan `range()`:

```python
for i in range(10):
    print(i)

"""
Output:
0
1
2
3
4
5
6
7
8
9
"""
```

![Sintaks fungsi range()](assets/sintaks-range.jpeg)

Parameter `range()`:

- `start` — nilai awal (opsional, default `0`)
- `stop` — nilai batas, bersifat **eksklusif** (wajib)
- `step` — nilai penambahan antar bilangan (opsional, default `1`)

```python
for i in range(1, 10, 2):
    print(i)

"""
Output:
1
3
5
7
9
"""
```

---

## While

`while` adalah sintaks perulangan yang bersifat **indefinite iteration** — berhenti ketika kondisi tertentu terpenuhi.

![Format perulangan while](assets/format-while.jpeg)

```python
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

"""
Output:
1
2
3
4
5
"""
```

> Hati-hati dengan **infinite loop** — kondisi ketika perulangan tidak pernah berhenti karena tidak ada increment atau kondisi tidak pernah terpenuhi:

```python
counter = 1
while counter <= 5:
    print(counter)
    # Tidak ada increment — program akan berjalan selamanya!
```

---

## For Bersarang (Nested Loop)

Perulangan dalam perulangan disebut **nested loop**.

![Format nested loop](assets/format-nested-loop.jpeg)

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

"""
Output:
1 1
1 2
2 1
2 2
"""
```

![Ilustrasi alur nested loop](assets/ilustrasi-nested-loop.jpeg)

Perulangan luar (`i`) akan dilanjutkan setelah perulangan dalam (`j`) selesai sepenuhnya.

---

## Kontrol Perulangan

### `break`

Menghentikan perulangan sepenuhnya dan keluar dari blok perulangan tersebut:

```python
for i in range(2):
    print("Perulangan luar:", i)
    for j in range(10):
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""
```

```python
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
"""
```

### `continue`

Menghentikan iterasi saat ini dan melanjutkan ke iterasi berikutnya:

```python
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""
```

### `else` setelah `for`

Digunakan untuk perulangan pencarian. Blok `else` dieksekusi jika `break` tidak pernah terjadi:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

"""
Output:
Angka tidak ditemukan.
"""
```

### `else` setelah `while`

Blok `else` dieksekusi ketika kondisi `while` menjadi `False`:

```python
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""
```

> Jika `while` keluar karena `break`, blok `else` tidak akan dieksekusi.

### `pass`

Digunakan sebagai placeholder ketika Python memerlukan pernyataan tetapi tidak ada tindakan yang perlu dilakukan:

```python
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
Output:
(tidak ada output)
"""
```

---

## List Comprehension

Cara ringkas untuk menghasilkan list baru berdasarkan list atau iterable yang sudah ada.

**Cara konvensional:**

```python
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

"""
Output:
[1, 4, 9, 16]
"""
```

**Dengan list comprehension:**

```python
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

"""
Output:
[1, 4, 9, 16]
"""
```

![Sintaks list comprehension](assets/sintaks-list-comprehension.jpeg)

Komponen list comprehension:

- `new_list` — variabel yang dideklarasikan
- `expression` — ekspresi yang dijalankan setiap iterasi
- `for_loop_one_or_more_conditions` — perulangan `for` yang didefinisikan
