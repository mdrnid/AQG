# Rangkuman: Ekspresi

Kita sudah berada di penghujung materi Ekspresi. Sampai sini, Anda memiliki pemahaman mendasar mengenai ekspresi yang akan sering dijumpai ketika membuat program Python. Mari kita rangkum secara saksama.

---

## Pengertian Ekspresi

**Ekspresi** pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam tipe tertentu.

---

## Jenis-Jenis Ekspresi

### Menurut Arity dari Operator

- **Biner** — ekspresi dengan dua operan. Contoh: `x + y`, `x - y`, `x * y`, dll.
- **Uner** — ekspresi dengan satu operan. Contoh: increment (`x += 1`), decrement (`x -= 1`), negasi (`not x`)

### Menurut Tipe Data yang Dihasilkan

| Jenis | Pola | Contoh |
|-------|------|--------|
| **Ekspresi aritmetika** | `<numerik> <operator> <numerik>` → `<numerik>` | `2 + 2 = 4`, `2 - 2 = 0` |
| **Ekspresi relasional** | `<numerik> <operator> <numerik>` → `<boolean>` | `3 < 10 = True`, `1 > 10 = False` |
| **Ekspresi logika** | `<boolean> <operator> <boolean>` → `<boolean>` | `True or False = True` |

---

## Jenis-Jenis Operator

### Operator Aritmetika

Asumsikan `x = 11` dan `y = 5`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `+` | Menambahkan nilai dari kedua operan | `x + y = 16` |
| `-` | Mengurangi nilai dari kedua operan | `x - y = 6` |
| `*` | Mengalikan nilai dari kedua operan | `x * y = 55` |
| `//` | Pembagian bulat (hasil bilangan bulat) | `x // y = 2` |
| `/` | Pembagian riil (hasil bilangan riil) | `x / y = 2.2` |
| `%` | Sisa hasil pembagian (modulo) | `x % y = 1` |
| `**` | Memangkatkan nilai dari dua operan | `x ** y = 161051` |

---

### Operator Relasional

Menghasilkan nilai boolean. Asumsikan `x = 5` dan `y = 10` (integer/float):

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `==` | `True` jika kedua operan bernilai sama | `x == y` → `False` |
| `!=` | `True` jika kedua operan tidak sama | `x != y` → `True` |
| `>` | `True` jika operan kiri lebih besar | `x > y` → `False` |
| `<` | `True` jika operan kiri lebih kecil | `x < y` → `True` |
| `>=` | `True` jika operan kiri lebih besar atau sama | `x >= y` → `False` |
| `<=` | `True` jika operan kiri lebih kecil atau sama | `x <= y` → `True` |

Untuk operan bertipe string, asumsikan `x = "Dicoding"` dan `y = "Indonesia"`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `==` | `True` jika kedua string identik | `x == y` → `False` |
| `!=` | `True` jika kedua string tidak sama | `x != y` → `True` |
| `>` | `True` jika huruf pertama `x` lebih besar secara unicode | `x > y` → `False` |
| `<` | `True` jika huruf pertama `x` lebih kecil secara unicode | `x < y` → `True` |
| `>=` | `True` jika huruf pertama `x` lebih besar atau sama secara unicode | `x >= y` → `False` |
| `<=` | `True` jika huruf pertama `x` lebih kecil atau sama secara unicode | `x <= y` → `True` |

---

### Operator Logika

Operan bertipe boolean, hasil bertipe boolean. Asumsikan `p = True` dan `q = False`:

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `and` / `&` | `True` hanya jika **kedua** operan `True` | `p and q` → `False` |
| `or` / `\|` | `True` jika **salah satu** operan `True` | `p or q` → `True` |
| `not` | Membalikkan nilai boolean (negasi) | `not q` → `True` |

---

### Operator Assignment

Menyederhanakan penulisan `x = x <operator> y`. Asumsikan `x = 11` dan `y = 5`:

| Operator | Setara dengan | Contoh |
|----------|---------------|--------|
| `+=` | `x = x + y` | `x += y` → `16` |
| `-=` | `x = x - y` | `x -= y` → `6` |
| `*=` | `x = x * y` | `x *= y` → `55` |
| `/=` | `x = x / y` | `x /= y` → `2.2` |
| `%=` | `x = x % y` | `x %= y` → `1` |
