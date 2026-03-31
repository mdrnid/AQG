# Jenis-Jenis Operator

Selain ekspresi dengan beragam jenis, operator pun memiliki berbagai jenis yang dikelompokkan menjadi operator aritmetika, operator relasional, operator logika, dan operator assignment.

---

## Operator Aritmetika

Operator untuk melakukan operasi aritmetika. Asumsikan `x = 11` dan `y = 5`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `+` (Penjumlahan) | Menambahkan nilai dari kedua operan | `x + y = 16` |
| `-` (Pengurangan) | Mengurangi nilai dari kedua operan | `x - y = 6` |
| `*` (Perkalian) | Mengalikan nilai dari kedua operan | `x * y = 55` |
| `//` (Pembagian Bulat) | Membagi dan membulatkan ke bawah | `x // y = 2` |
| `/` (Pembagian Riil) | Membagi dengan hasil bilangan riil | `x / y = 2.2` |
| `%` (Modulo) | Sisa hasil pembagian | `x % y = 1` |
| `**` (Pangkat) | Memangkatkan nilai dari dua operan | `x ** y = 161051` |

```python
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

"""
Output:
16
6
55
2
2.2
1
161051
"""
```

---

## Operator Relasional

Operator perbandingan antara dua operan yang menghasilkan nilai boolean. Asumsikan `x = 5` dan `y = 10`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `==` | `True` jika kedua operan bernilai sama | `x == y` → `False` |
| `!=` | `True` jika kedua operan tidak sama | `x != y` → `True` |
| `>` | `True` jika operan kiri lebih besar | `x > y` → `False` |
| `<` | `True` jika operan kiri lebih kecil | `x < y` → `True` |
| `>=` | `True` jika operan kiri lebih besar atau sama | `x >= y` → `False` |
| `<=` | `True` jika operan kiri lebih kecil atau sama | `x <= y` → `True` |

```python
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:
False
True
False
True
False
True
"""
```

Operator relasional juga dapat digunakan pada operan bertipe string. Asumsikan `x = "Dicoding"` dan `y = "Indonesia"`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `==` | `True` jika kedua string identik | `x == y` → `False` |
| `!=` | `True` jika kedua string tidak sama | `x != y` → `True` |
| `>` | `True` jika nilai unicode huruf pertama `x` lebih tinggi dari `y` | `x > y` → `False` |
| `<` | `True` jika nilai unicode huruf pertama `x` lebih rendah dari `y` | `x < y` → `True` |
| `>=` | `True` jika nilai unicode huruf pertama `x` lebih tinggi atau sama | `x >= y` → `False` |
| `<=` | `True` jika nilai unicode huruf pertama `x` lebih rendah atau sama | `x <= y` → `True` |

> **Catatan:** Nilai unicode adalah standar internasional yang menetapkan kode numerik untuk setiap karakter dari hampir semua sistem tulisan dan simbol yang digunakan manusia.

```python
x = "Dicoding"
y = "Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:
False
True
False
True
False
True
"""
```

String `"Dicoding"` dan `"Indonesia"` tidak sama, sehingga `==` menghasilkan `False` dan `!=` menghasilkan `True`. Operator sisanya membandingkan huruf pertama: `D` pada `"Dicoding"` vs `I` pada `"Indonesia"` berdasarkan nilai unicode-nya.

---

## Operator Logika

Operator untuk melakukan operasi logika dengan operan bertipe boolean. Asumsikan `p = True` dan `q = False`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `and` / `&` | `True` hanya jika **kedua** operan bernilai `True` | `p and q` → `False` |
| `or` / `\|` | `True` jika **salah satu** operan bernilai `True` | `p or q` → `True` |
| `not` | Membalikkan nilai boolean operan (negasi) | `not q` → `True` |

![Ilustrasi tabel kebenaran operator logika](assets/operator-logika-truth-table.jpeg)

---

### Operator AND

`AND` hanya menghasilkan `True` jika **kedua** operan bernilai `True`:

![Tabel kebenaran AND](assets/operator-and-truth-table.jpeg)

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)

"""
Output:
True
False
False
False
"""
```

---

### Operator OR

`OR` menghasilkan `True` jika **salah satu atau kedua** operan bernilai `True`:

![Tabel kebenaran OR](assets/operator-or-truth-table.jpeg)

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)

"""
Output:
True
True
True
False
"""
```

---

### Operator NOT

`NOT` membalikkan nilai boolean operan (negasi):

![Tabel kebenaran NOT](assets/operator-not-truth-table.jpeg)

```python
print(not True)
print(not False)

"""
Output:
False
True
"""
```

---

## Operator Assignment

Operator assignment menyederhanakan penulisan operasi `x = x <operator> y`. Asumsikan `x = 11` dan `y = 5`:

| Operator | Setara dengan | Contoh |
|----------|---------------|--------|
| `+=` | `x = x + y` | `x += y` → `16` |
| `-=` | `x = x - y` | `x -= y` → `6` |
| `*=` | `x = x * y` | `x *= y` → `55` |
| `/=` | `x = x / y` | `x /= y` → `2.2` |
| `%=` | `x = x % y` | `x %= y` → `1` |

```python
x = 11
x += 5
print(x)   # 16

x = 11
x -= 5
print(x)   # 6

x = 11
x *= 5
print(x)   # 55

x = 11
x /= 5
print(x)   # 2.2

x = 11
x %= 5
print(x)   # 1

"""
Output:
16
6
55
2.2
1
"""
```

Untuk memahami lebih jelas, perhatikan bahwa `x += 5` sepenuhnya setara dengan `x = x + 5`:

```python
x = 11
x += 5
print(x)   # 16

x = 11
x = x + 5
print(x)   # 16

"""
Output:
16
16
"""
```

Operator assignment sering dijumpai pada perulangan (*loop*) — Anda akan mempelajarinya pada materi berikutnya.
