# Menjalankan Kode Program di Lokal

Setelah mempersiapkan instalasi Python dan memilih IDE, mari kita jalankan kode program pertama Anda menggunakan lokal komputer.

Ada tiga mode untuk menjalankan kode program Python menggunakan lokal komputer:

1. **Kode Interaktif**
2. **Script**
3. **Notebook**

---

## 1. Kode Interaktif

![Mode kode interaktif Python](assets/mode-interaktif.jpeg)

Mode kode interaktif memungkinkan Anda menjalankan kode Python langsung dari terminal atau command prompt, tanpa perlu membuat file terlebih dahulu. Mode ini biasanya digunakan untuk bereksplorasi dan menjalankan dua hingga tiga baris kode saja.

> Pastikan Python sudah terinstal sebelum menggunakan mode ini.

### Langkah-langkah

1. Buka terminal atau command prompt.

2. Jalankan perintah berikut untuk masuk ke mode interaktif:

   ```bash
   python
   ```

3. Tampilan mode interaktif akan muncul seperti berikut:

   ![Tampilan mode interaktif Python di terminal](assets/mode-interaktif-terminal.png)

4. Coba jalankan kode berikut:

   ```python
   print("Hello World!")
   ```

   Kode di atas akan menampilkan teks `Hello World!` pada terminal Anda.

5. Anda juga bisa melakukan operasi matematika langsung di terminal:

   ```python
   2 + 2
   ```

   Kode di atas akan menghasilkan nilai `4` sebagai hasil dari operasi penjumlahan.

---

## 2. Script

![Mode script Python](assets/mode-script.png)

Script adalah mode yang paling sering digunakan oleh programmer. Anda akan membuat sebuah file (disebut *script*) dengan ekstensi `.py`, lalu mengeksekusinya untuk menjalankan kode di dalamnya.

### Langkah-langkah

1. Buka IDE atau editor kode Anda, misalnya **Visual Studio Code**.

2. Buka folder kerja melalui **File > Open Folder** di pojok kiri atas, lalu pilih folder tempat Anda ingin menyimpan file script.

3. Buat file Python baru melalui **File > New File**, lalu pilih salah satu opsi berikut:

   - **Jika tersedia opsi "Python File":**
     - Pilih opsi tersebut — file berekstensi `.py` akan langsung terbuat.
     - Simpan file dengan `Ctrl + S`.

   - **Jika tersedia opsi "Text File":**
     - Pilih opsi tersebut untuk membuka file teks kosong.
     - Simpan file dengan `Ctrl + S`.
     - Masukkan nama file dengan ekstensi `.py`, contoh: `first-program.py`, lalu klik simpan.

4. Masukkan kode program berikut ke dalam file, lalu simpan dengan `Ctrl + S`:

   ```python
   print("Hello World!")
   ```

5. Eksekusi file tersebut melalui terminal:

   - Buka terminal atau command prompt.
   - Pastikan terminal mengarah ke folder yang berisi file Anda:

     ![Tampilan terminal di folder proyek](assets/terminal-folder-proyek.png)

   - Jalankan perintah berikut:

     ```bash
     python <nama-file>.py
     ```

     > Ganti `<nama-file>` dengan nama file Python yang telah Anda buat. Contoh: `python first-program.py`

---

## 3. Notebook

Untuk menggunakan mode Notebook, Anda bisa menggunakan **Google Colaboratory** atau **Jupyter Notebook** yang sebelumnya telah diinstal.

### Menggunakan Google Colaboratory

1. Buka [Google Colaboratory](https://colab.research.google.com/).

2. Pilih **New Notebook** untuk membuat notebook baru.

3. Pada sel kode kosong yang tersedia, masukkan kode berikut:

   ```python
   print("Hello World!")
   ```

4. Klik tombol **Run cell** di sebelah kiri sel untuk menjalankan kode. Hasilnya akan ditampilkan langsung di bawah sel.

   ![Tampilan hasil eksekusi kode di Google Colaboratory](assets/colab-run-cell.png)

---

Sampai sini, Anda telah mempelajari tiga mode menjalankan kode Python di lokal komputer. Anda bisa mencoba mengikuti kelas ini sembari membuat kode program sendiri menggunakan salah satu mode yang paling nyaman bagi Anda.
