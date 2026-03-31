# Jenis-Jenis Ekspresi

Pada dasarnya, jenis-jenis ekspresi dibagi menjadi dua:

1. Menurut jumlah operan (*arity*) dari operator
2. Menurut tipe data yang dihasilkan

---

## Ekspresi Menurut Arity dari Operator

| Jenis | Contoh |
|-------|--------|
| **Biner** | `x + y`, `x - y`, `x * y`, `x / y`, `x ** y`, `x < y`, `x <= y`, `x > y`, `x >= y`, `x % y`, `x == y`, `x != y` |
| **Uner** | `x += 1`, `x -= 1`, `not x` |

**Ekspresi biner** memiliki dua operan. Operatornya meliputi:

- Aritmetika: `+`, `-`, `*`, `/`, `**`, `%`
- Perbandingan: `<`, `<=`, `>`, `>=`, `==`, `!=`

**Ekspresi uner** memiliki satu operan. Contohnya:

- *Increment*: `x += 1`
- *Decrement*: `x -= 1`
- *Negasi*: `not x`

Berikut penerapan ekspresi uner dalam Python:

```python
a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10
"""
```

Penjelasan kode di atas:

- `not a` — karena `a = True`, maka `not True` menghasilkan `False`
- `b -= 1` (*decrement*) — setara dengan `b = b - 1`, sehingga `6 - 1 = 5`
- `c += 1` (*increment*) — setara dengan `c = c + 1`, sehingga `6 + 1 = 7`
- `-d` — negasi nilai `d`, sehingga `10` menjadi `-10`

---

## Ekspresi Menurut Tipe Data yang Dihasilkan

| Jenis | Pola | Contoh |
|-------|------|--------|
| **Ekspresi aritmetika** | `<numerik> <operator> <numerik>` → `<numerik>` | `2 + 2 = 4`, `2 - 2 = 0` |
| **Ekspresi relasional** | `<numerik> <operator> <numerik>` → `<boolean>` | `3 < 10 = True`, `1 > 10 = False` |
| **Ekspresi logika** | `<boolean> <operator> <boolean>` → `<boolean>` | `True or False = True` |

Penjelasan masing-masing jenis:

- **Ekspresi aritmetika** — operan bertipe numerik, menghasilkan nilai numerik
- **Ekspresi relasional** — operan bertipe numerik, menghasilkan nilai boolean
- **Ekspresi logika** — operan bertipe boolean, menghasilkan nilai boolean

```python
print(2 + 2)
print(3 < 10)
print(True or False)

"""
Output:
4
True
True
"""
```

- `2 + 2` menghasilkan `4` (ekspresi aritmetika)
- `3 < 10` menghasilkan `True` karena 3 memang kurang dari 10 (ekspresi relasional)
- `True or False` menghasilkan `True` — ini merupakan gerbang logika yang akan dipelajari lebih detail pada materi operator logika (ekspresi logika)
