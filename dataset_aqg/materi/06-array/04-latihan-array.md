# Latihan Array

Pada materi sebelumnya, kita telah memahami bahwa array adalah salah satu jenis struktur data linear. Pemrosesan sekuensial memproses setiap elemen array dari indeks terkecil hingga terbesar.

Kali ini, kita akan mempelajari salah satu contoh pemrosesan sekuensial — **mencari nilai terbesar dalam array**.

---

## Studi Kasus: Mencari Nilai Terbesar

Asumsikan kita memiliki array berikut:

![Ilustrasi array [1, 7, 2, 89, 3]](assets/ilustrasi-array-latihan.jpeg)

Array berisi: indeks ke-0 = `1`, indeks ke-1 = `7`, indeks ke-2 = `2`, indeks ke-3 = `89`, indeks ke-4 = `3`.

---

## Algoritma Two Pointers

Kita akan menggunakan **algoritma two pointers** — pendekatan yang memproses urutan data menggunakan dua penanda (*pointer*) secara bersamaan: `left` dan `right`.

![Ilustrasi dua pointer pada array](assets/ilustrasi-two-pointers.jpeg)

Aturan algoritma:

- Pointer `left` berada pada indeks pertama dan selalu menunjukkan **nilai terbesar** yang ditemukan sejauh ini
- Pointer `right` selalu berada pada elemen selanjutnya dan membandingkannya dengan elemen pointer `left`

---

## Langkah-langkah Algoritma

![Animasi proses two pointers mencari nilai terbesar](assets/animasi-two-pointers.gif)

1. `left` pada elemen `1`, `right` pada elemen `7`. Karena `7 > 1`, pindahkan `left` ke `7`.
2. `left` pada `7`, `right` pada `2`. Karena `2 < 7`, `left` tetap di `7`.
3. `left` pada `7`, `right` pada `89`. Karena `89 > 7`, pindahkan `left` ke `89`.
4. `left` pada `89`, `right` pada `3`. Karena `3 < 89`, `left` tetap di `89`.
5. Proses selesai — nilai pada `left` (`89`) adalah nilai terbesar.

---

## Implementasi Python

```python
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

"""
Output:
89
"""
```

Penjelasan kode:

1. Inisialisasi `var_arr = [1, 7, 2, 89, 3]`
2. `left_pointer = var_arr[0]` — pointer kiri dimulai dari elemen pertama
3. Perulangan `for` dari indeks ke-1 hingga akhir array
4. `right_pointer = var_arr[i]` — pointer kanan mengambil elemen berikutnya
5. Jika `right_pointer > left_pointer`, perbarui `left_pointer` dengan nilai `right_pointer`
6. Setelah perulangan selesai, `left_pointer` berisi nilai terbesar
7. Cetak `left_pointer`
