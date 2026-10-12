# LAPORAN PRAKTIKUM
## PEMBUATAN APLIKASI CURRICULUM VITAE (CV) DIGITAL BERBASIS STREAMLIT

---

**Disusun Oleh:**
* **Nama:** Wafah Khonia  
* **NIM:** 2530801081  
* **Program Studi:** Informatika  
* **Instansi:** UIN Syekh Nurjati Cirebon  

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Di era digitalisasi saat ini, penyajian profil profesional dan riwayat hidup (*Curriculum Vitae*) perlu dibuat lebih interaktif, mudah diakses, dan menarik. Penggunaan *CV static* berbasis dokumen cetak atau PDF seringkali kurang fleksibel dalam menampilkan pembaruan data secara langsung (*real-time*). 

Dengan memanfaatkan bahasa pemrograman Python dan kerangka kerja (*framework*) **Streamlit**, pembuat aplikasi dapat merancang antarmuka berbasis web secara cepat tanpa harus menguasai teknologi *front-end* yang kompleks. Aplikasi CV Digital ini dibuat untuk memudahkan mahasiswa dalam mengelola, mengedit, dan membagikan informasi profil diri, pengalaman organisasi, keahlian teknis, serta kontak secara dinamis.

### 1.2 Tujuan
1. Mengimplementasikan komponen-komponen dasar Streamlit untuk membangun aplikasi web interaktif.
2. Menampilkan profil diri, pengalaman organisasi, serta indikator keahlian teknis secara visual.
3. Menyediakan fitur manipulasi data secara langsung melalui kontrol *sidebar* (*input text*, *slider*, *file uploader*, dan *checkbox*).
4. Menyediakan fitur pengunduhan ringkasan CV dalam format teks.

---

## BAB II: STRUKTUR DAN PENJELASAN KODE

Aplikasi dibuat menggunakan file Python tunggal yang mengimpor pustaka `streamlit`. Berikut adalah penjelasan dari komponen-komponen utama pada kode:

### 2.1 Konfigurasi Halaman & Sidebar
* **`st.set_page_config()`**: Mengatur judul tab peramban menjadi *"CV Digital Mahasiswa"* dan menggunakan ikon topi toga (🎓).
* **`st.sidebar`**: Digunakan sebagai tempat panel kontrol *input* pengguna, sehingga tampilan utama tidak tertutup oleh formulir pengisian data.

### 2.2 Komponen Input Data
* **Input Teks (`st.sidebar.text_input`)**: Mengambil input singkat seperti Nama Lengkap dan NIM.
* **Pilihan Jurusan (`st.sidebar.selectbox`)**: Menyediakan pilihan menu drop-down untuk menentukan program studi.
* **Area Teks Multi-baris (`st.sidebar.text_area`)**: Digunakan untuk mengisi deskripsi biografi singkat serta riwayat pengalaman organisasi.
* **Unggah Foto (`st.sidebar.file_uploader`)**: Memungkinkan pengguna mengunggah berkas foto profil berformat JPG, JPEG, atau PNG.

### 2.3 Tata Letak dan Logika Tampilan
* **Layout Kolom (`st.columns`)**: Membagi area atas menjadi 2 kolom (rasio 2:1) untuk memisahkan teks profil di sebelah kiri dan foto profil di sebelah kanan.
* **Kondisional Sertifikasi/Magang (`st.sidebar.checkbox`)**: Menampilkan blok informasi tambahan secara dinamis jika pengguna mencentang opsi pengalaman magang/sertifikasi.
* **Slider Kemahiran (`st.sidebar.slider`) & Progress Bar (`st.progress`)**: Menghubungkan nilai persentase keahlian teknis (Python, Web Dev, Database) dari *slider* ke tampilan visual berupa garis progres.

### 2.4 Fitur Kontak & Ekspor Data
* **Expander (`st.expander`)**: Menyembunyikan dan menampilkan detail kontak (Email & GitHub) agar antarmuka tetap bersih.
* **Tombol Unduh (`st.download_button`)**: Menghasilkan berkas `.txt` yang berisi rangkuman data CV untuk diunduh langsung oleh pengguna.

---

## BAB III: IMPLEMENTASI KODE PROGRAM

Berikut adalah kode sumber lengkap dari aplikasi **CV Digital Mahasiswa**:

```python
import streamlit as st

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="CV Digital Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# 2. Membuat Sidebar untuk Input Data
st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

# Komponen Input Teks
nama = st.sidebar.text_input("Nama Lengkap", "Wafah Khonia")
nim = st.sidebar.text_input("NIM", "2530801081")
jurusan = st.sidebar.selectbox(
    "Jurusan",
    ["Informatika", "Sistem Informasi", "Teknik Elektro"]
)

# Komponen Input Teks Area (Multi-baris)
deskripsi = st.sidebar.text_area(
    "Deskripsi Singkat (Bio)",
    "Saya adalah mahasiswa Informatika yang tertarik dengan pengembangan teknologi, pemrograman, dan pengembangan perangkat lunak."
)

# Komponen Input Teks Area untuk Organisasi
organisasi = st.sidebar.text_area(
    "Pengalaman Organisasi",
    """HIMAFOR UIN Syekh Nurjati Cirebon
Sekretaris Umum II | 2026–2027

- Mengelola administrasi dan pengarsipan dokumen organisasi.
- Menyusun surat masuk dan surat keluar.
- Menyusun notula dan dokumentasi hasil rapat.
- Mengelola data administrasi departemen, absensi, dan inventaris.
- Membantu Sekretaris Umum I dalam tugas kesekretariatan.

Ikatan Mahasiswa Indramayu
Anggota

Himpunan Santri Indramayu
Anggota"""
)

# Komponen Logika Kondisional untuk Sertifikasi/Magang
st.sidebar.markdown("---")
punya_pengalaman = st.sidebar.checkbox(
    "Punya Pengalaman Magang/Sertifikasi?"
)

# Komponen Upload File (Gambar)
foto_profil = st.sidebar.file_uploader(
    "Unggah Foto Profil (Opsional)",
    type=["jpg", "jpeg", "png"]
)

# --- AREA UTAMA (MAIN DASHBOARD) ---
st.title("🎓 Curriculum Vitae Digital")
st.markdown("---")

# 3. Membuat Layout 2 Kolom
kolom_kiri, kolom_kanan = st.columns([2, 1])

with kolom_kiri:
    # Menampilkan data menggunakan Typography Streamlit
    st.header(nama)
    st.subheader(f"{jurusan} | NIM: {nim}")
    st.write(deskripsi)

with kolom_kanan:
    # Menampilkan foto jika user mengunggahnya
    if foto_profil is not None:
        st.image(
            foto_profil,
            width=200,
            caption="Foto Profil"
        )
    else:
        st.info("Belum ada foto yang diunggah.")

# --- BAGIAN PENGALAMAN ORGANISASI ---
st.markdown("---")
st.markdown("### 👥 Pengalaman Organisasi")
st.write(organisasi)

# --- BAGIAN SERTIFIKASI / MAGANG ---
st.markdown("---")
st.markdown("### 💼 Sertifikasi / Magang")

if punya_pengalaman:
    detail_pengalaman = st.sidebar.text_area(
        "Detail Pengalaman Magang/Sertifikasi",
        "Tulis detail pengalaman di sini."
    )

    if detail_pengalaman:
        st.success(detail_pengalaman)
    else:
        st.info(
            "Silakan isi detail pengalaman magang/sertifikasi "
            "pada sidebar."
        )
else:
    st.write("Tidak ada riwayat magang atau sertifikasi.")

# --- BAGIAN KEAHLIAN (SKILLS) ---
st.markdown("---")
st.markdown("### 🔧 Keahlian Teknis")

# Sidebar slider untuk mengatur level skill
st.sidebar.markdown("---")
st.sidebar.subheader("Atur Kemahiran Skill")

skill_python = st.sidebar.slider("Python", 0, 100, 80)
skill_web = st.sidebar.slider("Web Development", 0, 100, 60)
skill_db = st.sidebar.slider("Database", 0, 100, 70)

# Menampilkan indikator visual (Progress Bar)
st.write("Python")
st.progress(skill_python)

st.write("Web Development (HTML/CSS)")
st.progress(skill_web)

st.write("Database (SQL)")
st.progress(skill_db)

# --- BAGIAN KONTAK ---
st.markdown("---")
st.markdown("### 📬 Hubungi Saya")

with st.expander("Klik untuk melihat detail kontak"):
    st.write("📧 Email: wafahkhonia3@gmail.com")
    st.write("💻 GitHub: https://github.com/wafahkhonia")

# --- DOWNLOAD CV ---
st.markdown("---")

data_cv = f"""
CURRICULUM VITAE

Nama: {nama}
NIM: {nim}
Jurusan: {jurusan}

Deskripsi:
{deskripsi}

Pengalaman Organisasi:
{organisasi}

Email: wafahkhonia3@gmail.com
GitHub: https://github.com/wafahkhonia
"""

st.download_button(
    label="📥 Download Data CV",
    data=data_cv,
    file_name="cv_wafah_khonia.txt"
)
```

---

## BAB IV: HASIL DAN TAMPILAN APLIKASI

Berikut adalah tangkapan layar antarmuka dari aplikasi CV Digital Mahasiswa yang telah dijalankan:



---

## BAB V: KESIMPULAN

Aplikasi **CV Digital Mahasiswa** berbasis Streamlit ini berhasil dibangun dan berjalan dengan baik. Fitur-fitur utama seperti pengisian data dinamis melalui *sidebar*, penyesuaian indikator keahlian dengan *slider*, unggah foto profil, hingga fitur unduh berkas teks telah berfungsi sebagaimana mestinya. Penggunaan Streamlit terbukti sangat efisien dalam memfasilitasi pembuatan aplikasi interaktif sederhana berbasis data secara cepat dan intuitif.