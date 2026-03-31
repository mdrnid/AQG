# Bersiap Membuat Kode Program di Lokal

Bagaimana pendapat Anda setelah menjalankan kode program pertama? Seru sekali, bukan? Sekarang mari kita lanjut ke materi berikutnya. Anda akan menjalankan kode program menggunakan lokal komputer — sederhananya menggunakan laptop atau komputer Anda sekarang.

Untuk menjalankan program Python di lokal komputer, Anda perlu mempersiapkan dua hal:

1. Menginstal Python
2. Menyiapkan Integrated Development Environment (IDE)

---

## Instal Python

Semua contoh dan tutorial pada kelas ini akan menggunakan **Python versi 3**. Jika Anda ingin mencoba membuat kode program secara mandiri sembari mengikuti kelas ini, pastikan menggunakan versi Python yang sesuai.

### Cek Apakah Python Sudah Terinstal

Sebelum mulai menginstal, pastikan Python belum terpasang pada lokal komputer Anda. Pengguna **Mac OS** atau **Ubuntu** umumnya sudah memiliki Python yang terinstal secara otomatis. Ikuti langkah berikut untuk mengeceknya:

1. Buka terminal atau command prompt:
   - **Windows** — klik tombol Windows lalu ketik `Command Prompt`
   - **Mac OS** — tekan `Command + Spacebar`, lalu ketik `Terminal`
   - **Ubuntu** — tekan `Ctrl + Alt + T`

2. Jalankan perintah berikut:

   ```bash
   python --version
   ```

3. Sistem akan menampilkan versi Python yang telah terinstal.

   ![Tampilan Windows OS saat cek versi Python](assets/cek-versi-python-windows.png)

Jika **Python versi 3 sudah terinstal**, silakan langsung menuju bagian [Menyiapkan IDE](#menyiapkan-integrated-development-environment-ide). Jika belum, ikuti panduan instalasi di bawah ini.

---

### Panduan Instalasi Python

#### Windows

1. Kunjungi [halaman unduhan Python untuk Windows](https://www.python.org/downloads/windows/).
2. Pilih versi Python yang diinginkan — kami merekomendasikan **versi 3.7 atau lebih tinggi**.
3. Pilih **Windows installer (64-bit)** atau **Windows installer (32-bit)** sesuai spesifikasi komputer Anda. Umumnya komputer saat ini mendukung 64-bit.
4. Setelah installer berhasil diunduh, jalankan instalasi dan pastikan mencentang **"Add Python 3.x to PATH"**.

   ![Centang Add Python to PATH saat instalasi](assets/instalasi-python-windows-path.png)

   > **Catatan:** Sebaiknya klik **Disable path length limit** untuk mengatasi masalah path yang melebihi 255 karakter.

   ![Disable path length limit](assets/instalasi-python-windows-pathlength.png)

> Jika mengalami kendala saat instalasi, Anda dapat merujuk ke [dokumentasi instalasi Python](https://docs.python.org/id/3.8/installing/index.html), menggunakan mesin pencari, ChatGPT, Google Gemini, atau forum diskusi Dicoding.

#### Mac OS

Kunjungi [halaman unduhan Python](https://www.python.org/downloads/) dan unduh installer untuk Mac OS, lalu ikuti proses instalasi yang tersedia.

#### Ubuntu

Jalankan perintah berikut di terminal:

```bash
sudo apt update
sudo apt install python3
```

---

## Menyiapkan Integrated Development Environment (IDE)

**Integrated Development Environment (IDE)** merupakan aplikasi yang menyediakan fasilitas komprehensif untuk pengembangan aplikasi bagi para programmer. IDE memiliki banyak fitur, salah satunya adalah kode editor yang mengizinkan Anda untuk membuat dan mengubah kode program.

Berikut adalah beberapa IDE populer yang dapat digunakan untuk menulis program Python:

---

### Visual Studio Code

**Visual Studio Code** merupakan salah satu IDE populer yang dapat digunakan untuk membuat kode program menggunakan berbagai bahasa pemrograman. IDE ini menyediakan ribuan ekstensi atau plugin yang dapat memperluas fungsionalitasnya — salah satunya ekstensi **"Python"** yang mendukung fitur seperti *debugging* dan *formatting* kode.

Pelajari lebih lanjut tentang ekstensi VS Code di [Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace).

Langkah instalasi:

1. Kunjungi [code.visualstudio.com](https://code.visualstudio.com/).
2. Unduh Visual Studio Code sesuai sistem operasi Anda.
3. Jalankan installer dan ikuti proses instalasi.
4. Setelah selesai, aplikasi akan terbuka dengan file dan proyek baru.

![Tampilan awal Visual Studio Code](assets/vscode-tampilan-awal.png)

---

### PyCharm

**PyCharm** merupakan IDE yang dibuat khusus untuk pengembangan aplikasi menggunakan bahasa pemrograman Python. Banyak fitur khusus yang disediakan untuk mempermudah proses pengembangan aplikasi Python.

Langkah instalasi:

1. Kunjungi [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/).
2. Unduh PyCharm sesuai sistem operasi Anda, lalu pilih **Community — For pure Python development**.
3. Jalankan installer dan PyCharm akan terbuka dengan file dan proyek baru.

![Tampilan awal PyCharm](assets/pycharm-tampilan-awal.png)

---

### Jupyter Notebook

**Jupyter Notebook** merupakan IDE berbasis web yang memungkinkan Anda membuat dan berbagi kode program, serta berkolaborasi dengan programmer lain. Jupyter Notebook terdiri dari beberapa sel — setiap sel dapat berisi kode atau teks, dan dapat dijalankan satu per satu tanpa harus membangun semua kode terlebih dahulu.

Langkah instalasi:

1. Buka terminal atau command prompt.

2. Pastikan `pip` menggunakan versi terbaru:

   ```bash
   pip install --upgrade pip
   ```

3. Instal Jupyter Notebook:

   ```bash
   pip install jupyter
   ```

4. Akses Jupyter Notebook dengan menjalankan:

   ```bash
   jupyter notebook
   ```

   > **Catatan:** Pastikan Anda membuka terminal dari folder proyek yang diinginkan. Contohnya folder `Memulai Pemrograman dengan Python\Jupyter Notebook`.

   ![Tampilan terminal Jupyter Notebook](assets/jupyter-terminal.png)

5. Untuk berpindah ke folder tertentu, gunakan perintah:

   ```bash
   cd <nama-folder>
   ```

6. Setelah perintah dijalankan, laman Jupyter Notebook akan terbuka di browser.

   ![Tampilan laman Jupyter Notebook](assets/jupyter-tampilan-web.png)

---

### Google Colaboratory

**Google Colaboratory** merupakan IDE berbasis web online yang memiliki fungsi serupa dengan Jupyter Notebook. Keunggulannya, Anda tidak perlu melakukan instalasi apa pun. Cukup akses [colab.research.google.com](https://colab.research.google.com/) dan proyek Google Colaboratory akan langsung terbuka.
