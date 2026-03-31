# Pengantar Unit Testing

Sampai pada tahap ini, sudah banyak modul pemrograman Python yang telah dipelajari. Kita telah mengenal operasi-operasi dasar dalam Python, seperti perulangan, fungsi, hingga OOP pada Python.

Saat Anda membangun aplikasi menggunakan Python dan aplikasi yang dikembangkan semakin kompleks, **dependensi** akan muncul. Artinya, satu atau lebih fungsi digunakan oleh fungsi lain. Bahkan, ketika kita mulai membangun aplikasi dengan rekan kita, kita membuat fungsi yang digunakan oleh rekan, ataupun sebaliknya.

Pada saat membuat fungsi baru ataupun mengubah fungsi yang sudah ada, tentunya perlu dipastikan bahwa fungsionalitas aplikasi yang sebelumnya tidak terganggu dengan adanya perubahan baru tersebut. Bagaimana jika fungsionalitas bukan hanya lima atau sepuluh, tetapi lebih dari itu? Tentu menyulitkan sekali untuk mengeceknya satu per satu setiap kita melakukan perubahan.

Di sinilah kita butuh **pengujian (test)** untuk fungsi-fungsi tersebut.

---

## Jenis Pengujian

Pengujian dapat dibedakan menjadi dua tipe utama:

### Manual Testing

Proses pengujian yang dilakukan oleh seseorang yang ditunjuk sebagai tester atau bahkan developer lainnya.

![Ilustrasi manual testing](assets/dos-991861b6f739678ea7ec17f6b1619aa220230823200517.png)

Tanpa sadar, sebenarnya ketika Anda menjalankan program pertama kali lalu mengecek bahwa output-nya sesuai atau tidak, itu merupakan pengujian manual.

### Testing Otomatis

Pengujian yang dilakukan secara otomatis terhadap kode-kode yang kita bangun berdasarkan **rencana pengujian** (*test plan*).

![Ilustrasi testing otomatis](assets/dos-b3bd6ef0676ff2031a3cf95f1de727b520230823200547.png)

Rencana pengujian terdiri dari bagian aplikasi yang ingin diuji, urutannya, dan tanggapan atau output yang diharapkan. Alur pengujian otomatis secara umum dimulai dari menyusun rencana pengujian, lalu membangun kode tes dan menjalankan kode tes tersebut. Jika kode tes gagal, kita perlu memperbarui kode; jika kode tes berhasil, kita melaju ke pengujian selanjutnya hingga selesai.

---

## Integration Testing vs Unit Testing

Tidak hanya sekadar manual dan otomatis, dalam dunia testing yang begitu luas, Anda akan menemui berbagai jenis testing. Dua di antaranya adalah **unit testing** dan **integration testing**.

### Integration Testing

Pengujian yang bertujuan untuk menguji suatu sistem sebagai satu kesatuan. Bayangkan Anda sedang mengecek lampu motor — hal pertama yang dilakukan adalah menyalakan motor. Lalu, Anda melihat lampu motor tersebut yang sempat menyala, tetapi perlahan mati.

Kejadian tersebut erat dengan konsep integration testing karena dengan menyalakan motor, kita dapat menguji seluruh bagian motor lain, seperti lampunya.

### Unit Testing

Pengujian yang lebih spesifik dan fokus terhadap bagian-bagian kecil. Bayangkan ketika mengecek lampu motor dan ternyata ia tidak menyala, Anda perlu mengecek lampu tersebut; apakah rusak? Atau ada kabel dari lampu tersebut yang tidak berfungsi? Hal-hal yang lebih spesifik tersebut adalah unit testing. Dalam pemrograman, bagian-bagian kecil tersebut berupa fungsi, kelas, dan sebagainya.

---

## Library unittest

Pada materi ini, kita akan mempelajari unit testing menggunakan salah satu library bawaan Python, yaitu **`unittest`**. Unit test adalah proses pengujian perangkat lunak yang memastikan setiap unit/fungsi dari program teruji.

Layaknya sebuah framework pengujian, library `unittest` mendukung beberapa hal esensial berikut:

- Pengujian secara otomatis
- Kode awal proses (*setup*) dan akhir proses (*shutdown*) yang dapat digunakan ulang
- Penyatuan sejumlah pengujian dalam sebuah koleksi
- Terpisahnya framework pengujian dari framework pelaporan (*reporting*)

Library `unittest` mendukung sejumlah konsep penting yang berorientasi objek:

| Konsep | Deskripsi |
|--------|-----------|
| **Test fixture** | Merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (*cleanup*). Contoh: menyiapkan basis data pengujian, direktori pengujian, atau mengaktifkan sebuah proses server |
| **Test case** | Sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. Library `unittest` menyediakan basis class `TestCase` yang akan digunakan untuk membuat kasus pengujian baru |
| **Test suite** | Sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya. Berguna untuk mengumpulkan pengujian-pengujian yang akan dieksekusi bersama |
| **Test runner** | Komponen yang akan mengatur (*orchestrates*) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna. Runner dapat menggunakan tampilan grafis, tampilan tekstual, atau mengembalikan nilai spesial yang menyatakan hasil dari pengujian |
