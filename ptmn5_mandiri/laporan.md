# LAPORAN TUGAS PROJEK MANDIRI
## Supply Chain Kopi Blockchain Ledger: Sistem Pelacakan Rantai Pasok Berbasis Streamlit & SHA-256

---

**Mata Kuliah:** Blockchain   
**Kelas:** 3 INF D  

---

### A. TUJUAN PEMBELAJARAN
1. Mahasiswa memahami konsep OOP pada Python melalui penerapan class `Block` dan `Blockchain`.  
2. Mahasiswa mampu menerapkan arsitektur modular dengan memisahkan backend (logika blockchain) dan frontend (Streamlit).  
3. Mahasiswa memahami konsep dasar blockchain: block, hash, nonce, dan hash pointer.  
4. Mahasiswa mampu menerapkan algoritma SHA‑256 untuk menjaga integritas data.  
5. Mahasiswa mampu membangun sistem sederhana untuk pelacakan rantai pasok kopi.  
6. Mahasiswa mampu melakukan validasi rantai dan mendeteksi manipulasi data.  

---

### B. KONSEP ARSITEKTUR MODULAR
- **Backend**: terdiri dari class `Block` dan `Blockchain`.  
  - `Block` menyimpan index, timestamp, data, previous_hash, nonce, dan hash.  
  - `Blockchain` mengatur genesis block, penambahan block baru dengan mining, serta validasi rantai.  
- **Frontend**: dibuat dengan Streamlit.  
  - Menyediakan input data pengiriman kopi.  
  - Tombol untuk mining block baru.  
  - Tombol validasi rantai.  
  - Ledger interaktif untuk melihat detail setiap block.  

---

### C. DESKRIPSI PROJECT
Proyek ini adalah **Supply Chain Kopi Blockchain Ledger**, sistem sederhana untuk mencatat perjalanan kopi dalam rantai pasok.  
Setiap tahapan pengiriman kopi (misalnya dari petani ke distributor) disimpan sebagai block dalam blockchain.  

---

### D. LANGKAH KERJA PROJECT
1. **Membuat struktur blockchain** dengan class `Block` dan `Blockchain`.  
2. **Genesis Block** sebagai blok pertama rantai kopi.  
3. **Menambahkan data pengiriman** kopi melalui antarmuka Streamlit.  
4. **Proses hashing SHA‑256** dengan nonce dan difficulty.  
5. **Validasi blockchain** untuk mendeteksi manipulasi data.  
6. **Ledger interaktif** menampilkan detail block (index, timestamp, data, nonce, hash).  

---

### E. HASIL IMPLEMENTASI
- Aplikasi web interaktif berbasis Streamlit.  
- Pengguna dapat menambahkan data pengiriman kopi → otomatis ditambang menjadi block baru.  
- Ledger menampilkan seluruh block dengan detail hash.  
- Fitur validasi rantai mendeteksi apakah data dimanipulasi.  

---

### F. ANALISIS HASIL
- Blockchain menjaga integritas data rantai pasok kopi.  
- Mining dengan nonce menunjukkan konsep Proof of Work.  
- Validasi rantai membuktikan bahwa manipulasi data dapat terdeteksi.  
- Streamlit memudahkan visualisasi ledger dan interaksi pengguna.  

---

### G. KESIMPULAN
Proyek Supply Chain Kopi Blockchain berhasil mengimplementasikan konsep dasar blockchain untuk pelacakan rantai pasok kopi.  
Sistem menggunakan struktur block yang saling terhubung melalui hash pointer, algoritma SHA‑256, dan validasi rantai.  
Dengan Streamlit, pengguna dapat berinteraksi langsung, menambahkan data, melihat ledger, dan melakukan validasi integritas rantai.  

---

### H. Dokumentasi Hasil
<img width="1917" height="1062" alt="image" src="https://github.com/user-attachments/assets/374baf17-6847-41c4-9efe-b73131165d98" />

