import streamlit as st
from core import Block, Blockchain

st.set_page_config(page_title="Supply Chain Kopi", page_icon="☕")
st.title("☕ Sistem Pelacakan Rantai Pasok Kopi")

# Inisialisasi Blockchain di Session State
if "kopi_chain" not in st.session_state:
    st.session_state.kopi_chain = Blockchain()

# --- FORM INPUT & MINING BLOK ---
data_kopi = st.text_input("Masukkan Data Pengiriman (Misal: '100kg - Petani A'):")

if st.button("⚒️ Mine Block (Tambah Data)"):
    if data_kopi:
        new_index = len(st.session_state.kopi_chain.chain)
        new_block = Block(new_index, data_kopi, "")

        # Streamlit Spinner untuk efek loading saat proses PoW berlangsung
        with st.spinner("Sedang mencari Hash yang tepat (Mining)..."):
            st.session_state.kopi_chain.add_block(new_block)

        st.success("Blok berhasil ditambang dan diamankan ke dalam rantai!")
        st.rerun()
    else:
        st.warning("Data pengiriman tidak boleh kosong!")

# --- FITUR VALIDASI RANTAI ---
st.markdown("---")
if st.button("🛡️️ Cek Integritas Rantai"):
    validation_result = st.session_state.kopi_chain.is_chain_valid()
    
    # Menangani jika is_chain_valid() mengembalikan tuple (is_valid, msg) atau cuma boolean (is_valid)
    if isinstance(validation_result, tuple):
        is_valid, msg = validation_result
    else:
        is_valid, msg = validation_result, "Pengecekan selesai."

    if is_valid:
        st.success("Status Jaringan: AMAN (Rantai Valid)")
    else:
        st.error("BAHAYA (Data telah dimanipulasi!)")

st.markdown("---")

# --- SIDEBAR: SIMULASI SERANGAN (HACKING) ---
st.sidebar.title("🧪 Simulasi Peretasan")

if st.sidebar.button("HACK BLOK 1"):
    if len(st.session_state.kopi_chain.chain) > 1:
        # Mengubah data blok indeks 1 secara paksa tanpa update hash
        st.session_state.kopi_chain.chain[1].data = "DATA PALSU!"
        st.sidebar.warning("⚠️ Data Blok 1 berhasil diubah secara paksa menjadi 'DATA PALSU!'")
        st.rerun()
    else:
        st.sidebar.error("Blok 1 belum tersedia. Tambahkan/tambang blok baru terlebih dahulu!")

# --- BUKU BESAR (LEDGER) ---
st.subheader("📜 Buku Besar (Ledger)")
for block in st.session_state.kopi_chain.chain:
    with st.expander(f"Block #{block.index} - Hash: {block.hash[:15]}..."):
        st.write(f"**Waktu:** {block.timestamp}")
        st.write(f"**Data:** {block.data}")
        st.write(f"**Nonce (Tebakan):** {block.nonce}")
        st.write(f"**Prev Hash:** {block.previous_hash}")
        st.info(f"**Hash:** {block.hash}")