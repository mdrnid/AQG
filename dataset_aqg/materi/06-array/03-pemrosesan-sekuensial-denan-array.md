# Pemrosesan Sekuensial pada Array

**Pemrosesan array** merujuk pada operasi-operasi yang dilakukan pada elemen-elemen suatu array — mulai dari manipulasi hingga pengolahan elemen.

**Pemrosesan sekuensial** adalah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. Pemrosesan ini lebih sering menggunakan perulangan (*loop*) dalam setiap prosesnya.

---

## Aturan Pemrosesan Sekuensial

Karena melibatkan semua elemen, ada beberapa hal yang perlu diperhatikan:

1. Setiap elemen array diakses secara langsung melalui indeksnya (metode *indexing*)
2. Elemen pertama (*first element*) adalah elemen dengan indeks terkecil, selalu dimulai dari `0`
3. Elemen selanjutnya (*next element*) dicapai melalui suksesor indeks
4. Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi
5. Suatu array tidak boleh kosong — minimal memiliki satu elemen

---

## Contoh Implementasi

```python
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")

"""
Output:
Current element: 1, next elements: 2
Current element: 2, next elements: 3
Current element: 3, next elements: 4
Current element: 4, next elements: 5
Current element: 5, next elements: None
"""
```

![Ilustrasi pemrosesan sekuensial array](assets/ilustrasi-pemrosesan-sekuensial.jpeg)

Penjelasan kode:

1. Inisialisasi `var_arr = [1, 2, 3, 4, 5]`
2. Perulangan `for` mengiterasi setiap elemen menggunakan indeks `i`
3. `current_element = var_arr[i]` — menyimpan elemen saat ini
4. `next_index = i + 1` — menghitung indeks berikutnya (*suksesor indeks*)
5. Jika `next_index` valid (dalam rentang array), ambil `var_arr[next_index]` sebagai `next_element`
6. Jika tidak valid (melebihi rentang), tetapkan `next_element = None`
7. Cetak `current_element` dan `next_element`

---

## Contoh Penerapan Pemrosesan Sekuensial

Beberapa operasi yang umum dilakukan pada array secara sekuensial:

- Mengisi array secara sekuensial
- Menghitung nilai rata-rata elemen array
- Mengalikan elemen array dengan suatu nilai
- Mencari nilai terbesar atau terkecil pada array
- Mencari indeks letak suatu nilai ditemukan pertama kali dalam array

Pada materi berikutnya, kita akan mempelajari cara mencari nilai terbesar pada array.
