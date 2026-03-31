# Pengenalan Python

Halo, calon programmer! Selamat datang pada modul pertama kelas **Memulai Pemrograman dengan Python**. Sebelum Anda mulai membuat program, mari mulai pembelajaran dengan mengenal terlebih dahulu bahasa pemrograman Python.

Python adalah bahasa pemrograman multifungsi yang dirilis pada tahun **1991** oleh **Guido van Rossum (GvR)**. Beliau membuat Python sebagai bahasa pemrograman yang mudah dibaca dan dimengerti (*readable*) serta memiliki kemampuan penanganan kesalahan (*exception handling*). Berdasarkan tujuan tersebut, Guido van Rossum berhasil menjadikan Python sebagai bahasa pemrograman yang dapat diimplementasikan ke dalam berbagai sektor. Python dapat digunakan untuk membangun website (server-side), analisis data, hingga pembelajaran mesin (*machine learning*).

Python memiliki ciri khas tersendiri sebagai salah satu pemrograman populer. Salah satu ciri khas yang paling dikenal adalah Python tidak mewajibkan penggunaan titik koma atau semi colon (`;`) pada setiap akhir kode programnya. Simak sintaks kode program di bawah.

```python
print("Hello World!")
```

Sintaks tersebut memberikan perintah untuk menampilkan/mencetak pesan berupa teks ke layar komputer. Perhatikan bahwa sintaks tersebut menggunakan kata `print` yang jika diterjemahkan ke dalam bahasa Indonesia memiliki arti mencetak. Cukup mudah dipahami, bukan?

---

## Versi Python

Sejak perilisan pertamanya, Python terus berkembang dan menyediakan beragam fitur baru.

### Python 2.x

Pada **Python versi 2** yang dirilis Oktober tahun 2000, Python mengembangkan berbagai fitur yang beberapa di antaranya adalah:

- **Garbage collector** — mengelola pembersihan memori secara otomatis
- **Memory management** — membantu programmer tidak perlu berfokus pada pengelolaan memori yang kompleks

Kedua fitur tersebut memungkinkan programmer untuk bisa berfokus pada pengembangan aplikasi atau program. Mengapa itu penting? Sejatinya ketika Anda membuat kode program, setiap kode tersebut akan disimpan dalam penyimpanan memori komputer. Jika penyimpanan memori tidak lagi terkontrol, komputer Anda akan mengalami kehabisan memori.

### Python 3.x

Python versi 2 lalu mengalami perubahan mayor dan bertransformasi menjadi **Python versi 3** yang dirilis pada Desember 2008. Versi 3 ini tidak bersifat *backward-compatible*, artinya beberapa sintaksis yang sebelumnya berjalan di versi 2.x tidak lagi dapat digunakan di versi ini. Semua perubahan tersebut merujuk kepada keinginan bahasa pemrograman Python yang memiliki prinsip:

> **Readable, Consistent, & Explicit**

Saat ini, Python versi 3.x terus berkembang dan dirilis setiap waktunya. Per kelas ini ditulis, **Python versi 3.11** merupakan versi terbaru dari Python yang dianggap memiliki kecepatan 10–60% lebih cepat dari versi sebelumnya, yakni 3.10.

Lihat penjelasan detail Python versi 3.11 di [dokumentasi resmi Python](https://docs.python.org/release/3.11.2/whatsnew/3.11.html).

---

## Python Overview

Pasca tahun 2000, Python membentuk beberapa sistem yang memungkinkan bahasa pemrograman ini menjadi bahasa yang mampu bertahan lama dan berkembang seiring waktu (*sustainable*). Dua sistem yang paling berdampak adalah:

### Python Software Foundation (PSF)

**Python Software Foundation (PSF)** merupakan lembaga non-komersial yang mengabdikan diri untuk menciptakan kondisi Python dan komunitas Python agar dapat tumbuh dan berkembang. Salah satu andil PSF adalah berkontribusi pada arah pengembangan Python yang sebelumnya dipegang oleh Guido van Rossum (GvR) sebagai **Benevolent Dictator For Life (BDFL)**. GvR menjabat gelar ini hingga 12 Juli 2018 dan menjadikan hampir semua keputusan pengembangan Python diambil alih oleh GvR pada kala itu.

### Python Enhancement Proposals (PEP)

**Python Enhancement Proposals (PEP)** menjadi panduan dalam pengembangan Python. Perubahan antar versi Python sebenarnya mengacu pada panduan-panduan PEP yang jumlahnya tidak hanya satu, tetapi ribuan panduan yang menjadi acuan perkembangan Python.

Lihat informasi detail mengenai PEP di [peps.python.org](https://peps.python.org/pep-0000/).

### Zen of Python (PEP 20)

Salah satu panduan yang menjadi patokan adalah **PEP 20** yang berjudul *Zen of Python*. PEP 20 ini menjadi dasar atau akar pada setiap pengambilan keputusan pengembangan Python. Berikut adalah isinya:

> Beautiful is better than ugly.
>
> Explicit is better than implicit.
>
> Simple is better than complex.
>
> Complex is better than complicated.
>
> Flat is better than nested.
>
> Sparse is better than dense.
>
> Readability counts.
>
> Special cases aren't special enough to break the rules.
>
> Although practicality beats purity.
>
> Errors should never pass silently.
>
> Unless explicitly silenced.
>
> In the face of ambiguity, refuse the temptation to guess.
>
> There should be one— and preferably only one —obvious way to do it.
>
> Although that way may not be obvious at first unless you're Dutch.
>
> Now is better than never.
>
> Although never is often better than *right* now.
>
> If the implementation is hard to explain, it's a bad idea.
>
> If the implementation is easy to explain, it may be a good idea.
>
> Namespaces are one honking great idea — let's do more of those!

Mungkin saat ini, Anda belum memahami betul maksud dari panduan tersebut. Jika Anda telah menyelesaikan kelas ini, silakan meninjau kembali panduan tersebut untuk bisa lebih memahami maksudnya.

---

## Mengapa Python?

Lantas, mengapa Anda harus memulai pemrograman menggunakan Python?

Selain mudah dimengerti dan dipelajari oleh orang yang sedang belajar pemrograman, efektivitas Python cukup terbukti dengan banyaknya jumlah pengguna bahasa pemrograman ini. **Stack Overflow** telah merilis hasil *Developers Survey* pada tahun 2022, dan Python merupakan tiga peringkat teratas bahasa pemrograman yang dipilih oleh para programmer maupun pemula untuk belajar kode/program.

Selain itu, Python juga dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, di antaranya:

- Terstruktur
- Prosedural
- Berorientasi objek
- Fungsional

Terakhir, Python dapat dimanfaatkan dalam berbagai sektor berikut:

- Web development (server-side)
- Software development
- Mathematics & data science
- Machine learning
- System scripting
- Internet of Things (IoT) development
- dan lain-lain

Sekali mendayung, dua tiga pulau terlampaui, bukan? Mari kita mulai belajar Python!
