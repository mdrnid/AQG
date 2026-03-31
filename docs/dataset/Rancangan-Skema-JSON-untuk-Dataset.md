# Rancangan Skema JSON untuk Dataset

Berdasarkan materi `perkenalan-pythn.md` dan format dataset yang telah didefinisikan, berikut adalah rancangan skema JSON yang dapat digunakan untuk setiap pasang data (input-target) dalam dataset Anda. Skema ini dirancang untuk memfasilitasi proses *fine-tuning* model IndoT5 dan integrasi dengan *frontend* melalui API.

```json
{
  "input": "<konteks materi dari perkenalan-pythn.md>\n\n<prompt instruksi untuk generasi pertanyaan>",
  "target": {
    "question": "<pertanyaan kuis yang dihasilkan>",
    "correct_answer": "<jawaban benar>",
    "distractors": [
      "<distraktor 1>",
      "<distraktor 2>",
      "<distraktor 3>",
      "<distraktor 4>"
    ],
    "metadata": {
      "difficulty": "<easy|medium|hard>",
      "question_type": "<MCQ|Code Completion>",
      "concept": "<konsep yang diuji, misal: Definisi Python, Versi Python, PEP>",
      "misconception_tags": [
        "<tag miskonsepsi 1>",
        "<tag miskonsepsi 2>"
      ]
    }
  }
}
```

## Penjelasan Komponen Skema JSON:

*   **`input` (String)**:
    *   Berisi gabungan dari **konteks materi** dan **prompt instruksi**. Konteks materi akan diambil dari paragraf atau bagian relevan dari `perkenalan-pythn.md`. Prompt instruksi akan memandu model untuk menghasilkan pertanyaan dan *distractor*.
    *   **Contoh Konteks**: "Python adalah bahasa pemrograman multifungsi yang dirilis pada tahun 1991 oleh Guido van Rossum (GvR). Beliau membuat Python sebagai bahasa pemrograman yang mudah dibaca dan dimengerti (*readable*) serta memiliki kemampuan penanganan kesalahan (*exception handling*)."
    *   **Contoh Prompt**: "Buatlah soal pilihan ganda tentang [Definisi Python] dengan tingkat kesulitan [mudah]. Sertakan jawaban benar dan 3 distraktor pedagogis."

*   **`target` (Object)**:
    *   **`question` (String)**: Pertanyaan kuis yang dihasilkan oleh model.
    *   **`correct_answer` (String)**: Jawaban yang benar untuk pertanyaan tersebut.
    *   **`distractors` (Array of Strings)**: Daftar 3 hingga 4 pilihan jawaban yang salah, namun *plausible* (masuk akal) dan berfungsi sebagai pengecoh.
    *   **`metadata` (Object)**:
        *   **`difficulty` (String)**: Tingkat kesulitan soal (`easy`, `medium`, `hard`). Ini akan sangat bergantung pada kompleksitas konsep yang diuji dan bagaimana *distractor* dirancang.
        *   **`question_type` (String)**: Tipe pertanyaan (`MCQ` untuk *Multiple Choice Question* atau `Code Completion` jika ada soal melengkapi kode). Untuk materi `perkenalan-pythn.md`, kemungkinan besar akan didominasi `MCQ`.
        *   **`concept` (String)**: Konsep utama yang diuji oleh pertanyaan. Contoh: "Definisi Python", "Sejarah Python", "Fitur Python 2.x", "Prinsip Python 3.x", "Zen of Python", "Manfaat Python".
        *   **`misconception_tags` (Array of Strings)**: Tag yang mengidentifikasi miskonsepsi umum yang mungkin diatasi oleh *distractor*. Contoh: `[
"salah_paham_versi", "salah_paham_pep"]`.

## Contoh Implementasi dari `perkenalan-pythn.md`

Berikut adalah contoh bagaimana satu paragraf dari materi dapat diubah menjadi format JSON ini:

**Konteks Materi:**
"Python adalah bahasa pemrograman multifungsi yang dirilis pada tahun 1991 oleh Guido van Rossum (GvR). Beliau membuat Python sebagai bahasa pemrograman yang mudah dibaca dan dimengerti (readable) serta memiliki kemampuan penanganan kesalahan (exception handling)."

**JSON Output:**
```json
{
  "input": "Konteks: Python adalah bahasa pemrograman multifungsi yang dirilis pada tahun 1991 oleh Guido van Rossum (GvR). Beliau membuat Python sebagai bahasa pemrograman yang mudah dibaca dan dimengerti (readable) serta memiliki kemampuan penanganan kesalahan (exception handling).\n\nPrompt: Buatlah satu soal pilihan ganda (MCQ) tentang pencipta bahasa Python berdasarkan konteks di atas. Tingkat kesulitan: mudah. Sertakan 1 jawaban benar dan 3 distraktor yang masuk akal.",
  "target": {
    "question": "Siapakah tokoh yang menciptakan bahasa pemrograman Python pada tahun 1991?",
    "correct_answer": "Guido van Rossum",
    "distractors": [
      "Dennis Ritchie",
      "James Gosling",
      "Bjarne Stroustrup"
    ],
    "metadata": {
      "difficulty": "easy",
      "question_type": "MCQ",
      "concept": "Sejarah Python",
      "misconception_tags": [
        "tokoh_pemrograman_lain"
      ]
    }
  }
}
```

Format JSON ini sangat ideal karena:
1.  **Terstruktur**: Memudahkan proses *parsing* saat *fine-tuning* model IndoT5.
2.  **Fleksibel**: Dapat dengan mudah dikonversi menjadi format JSONL (JSON Lines) yang sering digunakan oleh Hugging Face Datasets.
3.  **API-Ready**: Struktur ini sudah sangat siap untuk dikirimkan sebagai *response* dari API ke *frontend* Next.js Anda nantinya.
