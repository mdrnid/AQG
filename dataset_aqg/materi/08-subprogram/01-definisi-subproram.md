# Definisi Subprogram

Sejauh ini, Anda telah membuat program yang beragam. Setiap program yang Anda bangun akan semakin besar seiring kompleksitas masalah yang perlu diselesaikan. Semakin besar sebuah program, bagian kode yang berulang akan bertambah — tidak efisien jika harus mengetik ulang atau copy-paste.

Salah satu kode yang sering berulang adalah rumus atau formula:

```python
# Luas pertama
panjang = 5
lebar = 10
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

"""
Output:
50
60
"""
```

Kode di atas perlu menuliskan rumus yang sama dua kali. Solusinya adalah menggunakan **subprogram** — salah satu jenisnya adalah fungsi:

```python
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)

"""
Output:
50
60
"""
```

---

## Jenis Subprogram

**Subprogram** adalah serangkaian instruksi yang dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Ada dua jenis subprogram yang umum digunakan:

- **Fungsi** — blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. Output dinyatakan dalam tipe data yang eksplisit (integer, string, dll.)
- **Prosedur** — deretan instruksi yang jelas keadaan awal (*initial state*) dan keadaan akhirnya (*final state*). Mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.
