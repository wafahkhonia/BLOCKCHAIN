import streamlit as st
from core import Blockchain # Mengimpor mesin Blockchain yang kita buat

# --- KONFIGURASI HALAMAN ---
# [TAG: Konfigurasi Tampilan Utama] Mengatur judul tab browser, ikon, dan tata letak halaman
st.set_page_config(page_title="Blockchain Explorer", page_icon="🔗", layout="wide")

# [TAG: Judul Aplikasi] Menampilkan judul utama di bagian atas aplikasi
st.title("☕ Blockchain for Halal Coffee Supply Chain")

# --- SESSION STATE MANAGEMENT ---
# [TAG: Inisialisasi State] Memastikan data blockchain tidak terkonfigurasi ulang/hilang saat halaman direfresh
if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

# --- SIDEBAR: INPUT DATA ---
# [TAG: Sidebar Header] Menampilkan judul untuk formulir input di panel samping (sidebar)
st.sidebar.header("➕ Tambah Data Baru")

# Contoh Kasus: Rantai Pasok Kopi
# [TAG: Form Inputs] Komponen input form untuk menerima data dari pengguna
petani = st.sidebar.text_input("Nama Petani/Aktor:")
jumlah_kopi = st.sidebar.number_input("Jumlah Panen (Kg):", min_value=1)
lokasi = st.sidebar.text_input("Lokasi Kebun:")

# [TAG: Event Tombol] Aksi saat tombol "Tambahkan ke Blockchain" diklik
if st.sidebar.button("Tambahkan ke Blockchain"):
    # [TAG: Validasi Input] Memastikan input teks petani dan lokasi tidak kosong
    if petani and lokasi:
        # [TAG: Format Data] Mengemas data menjadi satu string JSON-like
        data_transaksi = f"Petani: {petani} | Panen: {jumlah_kopi} Kg | Lokasi: {lokasi}"
        
        # [TAG: Operasi Blockchain] Memanggil method add_block dari Object yang ada di memori
        st.session_state.my_blockchain.add_block(data_transaksi)
        
        # [TAG: Notifikasi Berhasil] Menampilkan pesan sukses di sidebar
        st.sidebar.success("Blok berhasil ditambahkan!")
    else:
        # [TAG: Notifikasi Gagal] Menampilkan pesan peringatan jika input belum lengkap
        st.sidebar.error("Lengkapi semua data!")

# --- MAIN AREA: VISUALISASI RANTAI ---
# [TAG: Area Utama Header] Menampilkan sub-header untuk buku besar (ledger)
st.subheader("📜 Blockchain Ledger (Buku Besar)")

# Status Validitas Rantai
# [TAG: Cek Validitas] Memanggil method is_chain_valid untuk mengecek integritas seluruh rantai
is_valid = st.session_state.my_blockchain.is_chain_valid()

# [TAG: Tampilan Status] Menampilkan indikator status keamanan blockchain (Aman / Rusak)
if is_valid:
    st.success("✔ Status Jaringan: Rantai Valid (Aman)")
else:
    st.error("❌ PERINGATAN: Integritas Rantai Rusak (Telah Dimanipulasi!)")

# Menampilkan semua blok dengan Looping
# [TAG: Iterasi Blok] Melakukan looping ke setiap blok yang ada di dalam rantai (blockchain.chain)
for block in st.session_state.my_blockchain.chain:
    # [TAG: Komponen Expander] Membuat UI dropdown/collapsible untuk setiap blok
    with st.expander(f"Blok #{block.index} | Hash: {block.hash[:15]}..."):
        # [TAG: Layout Kolom] Membuat 2 kolom untuk merapikan informasi di dalam blok
        col1, col2 = st.columns(2)

        # [TAG: Kolom 1 - Payload Data] Menampilkan data transaksi dan waktu pembuatan
        with col1:
            st.write("**Data Payload:**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")

        # [TAG: Kolom 2 - Kriptografi] Menampilkan hash unik blok dan pointer hash blok sebelumnya
        with col2:
            st.write("**Kriptografi:**")
            st.write(f"**Hash Saat Ini:**")
            st.code(block.hash, language='python')
            st.write(f"**Hash Sebelumnya (Pointer):**")
            st.code(block.prev_hash, language='python')