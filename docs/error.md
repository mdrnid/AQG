---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[5], line 4
      1 from src.dataset.chunker import chunk_markdown, chunk_all_materials
      2 
      3 # Test dengan 1 file dulu
----> 4 chunks = chunk_markdown('dataset_aqg/materi/01-Berkenalan-dengan-python/01-perkenalan-pythn.md')
      5 print(f'Total chunks: {len(chunks)}')
      6 print()
      7 for i, c in enumerate(chunks):

File d:\2-Project\AQG\src\dataset\chunker.py:160, in chunk_markdown(filepath, max_tokens, min_tokens)
    151 """
    152 Membaca satu file Markdown dan mengembalikan list of Chunk.
    153 
   (...)    157 - Jika section > max_tokens, split di batas kalimat
    158 """
    159 path = Path(filepath)
--> 160 text = path.read_text(encoding="utf-8")
    161 source_file = str(path)
    163 # Split berdasarkan heading
    164 # Pattern: baris yang dimulai dengan #, ##, atau ###

File d:\conda_envs\nlp_project\Lib\pathlib.py:1027, in Path.read_text(self, encoding, errors)
   1023 """
   1024 Open the file in text mode, read it, and close the file.
   1025 """
   1026 encoding = io.text_encoding(encoding)
-> 1027 with self.open(mode='r', encoding=encoding, errors=errors) as f:
   1028     return f.read()

File d:\conda_envs\nlp_project\Lib\pathlib.py:1013, in Path.open(self, mode, buffering, encoding, errors, newline)
   1011 if "b" not in mode:
   1012     encoding = io.text_encoding(encoding)
-> 1013 return io.open(self, mode, buffering, encoding, errors, newline)

FileNotFoundError: [Errno 2] No such file or directory: 'dataset_aqg\\materi\\01-Berkenalan-dengan-python\\01-perkenalan-pythn.md'