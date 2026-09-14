import hashlib
import time
from datetime import datetime, timezone

# 1. Mendefinisikan Struktur Data Tunggal (Satu Blok)
# [TAG: Kelas Blok] Cetakan dasar untuk membuat satu objek blok transaksi
class Block:
    # [TAG: Inisialisasi Atribut Blok] Mengatur data awal saat sebuah blok baru dibuat
    def __init__(self, index, data, prev_hash):
        self.index = index                      # [TAG: Nomor Urut] Posisi blok dalam rantai
        self.timestamp = time.time()            # [TAG: Waktu Dibuat] Waktu pembuatan dalam detik (UNIX timestamp)
        self.data = data                        # [TAG: Isian Data] Informasi/transaksi yang disimpan
        self.prev_hash = prev_hash              # [TAG: Hash Sebelumnya] Pointer yang menghubungkan ke blok terdahulu
        self.hash = self.calculate_hash()       # [TAG: Generasi Hash] Menghitung hash unik untuk blok ini

    # [TAG: Format Waktu] Properti untuk mengubah timestamp menjadi tanggal yang mudah dibaca manusia
    @property
    def timestamp_readable(self):
        # Cukup ganti baris timezone.localtime() jadi datetime.now().astimezone().tzinfo
        local_tz = datetime.now().astimezone().tzinfo
        dt = datetime.fromtimestamp(self.timestamp, tz=local_tz)
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    # [TAG: Kalkulasi Hash Kriptografi] Menghitung sidik jari digital (SHA-256) berdasarkan isi blok
    def calculate_hash(self):
        # [TAG: Penggabungan String] Menggabungkan seluruh komponen blok menjadi satu string
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash)
        # [TAG: Enkripsi SHA-256] Mengubah string menjadi nilai hash 64 karakter heksadesimal
        return hashlib.sha256(block_string.encode()).hexdigest()

# 2. Mendefinisikan Rantai Blok (Manajer Kumpulan Blok)
# [TAG: Kelas Blockchain] Mengelola daftar seluruh blok dan memvalidasi keamanannya
class Blockchain:
    # [TAG: Inisialisasi Rantai] Membuat list kosong dan membuat blok pertama (Genesis)
    def __init__(self):
        self.chain = []                         # [TAG: List Rantai] Kurung siku mencerminkan list kosong penampung blok
        self.create_genesis_block()             # [TAG: Panggil Genesis] Otomatis jalankan pembuat blok pertama

    # [TAG: Blok Pertama] Membuat blok pertama yang mengawali seluruh rantai
    def create_genesis_block(self):
        # Blok pertama selalu hardcoded
        genesis_block = Block(1, "Genesis Block (Awal Mula)", "0")    # [TAG: Data Default] prev_hash diisi "0"
        self.chain.append(genesis_block)        # [TAG: Tambah ke Rantai] Memasukkan genesis ke daftar

    # [TAG: Tambah Blok Baru] Fungsi untuk menambah transaksi/blok baru ke dalam rantai
    def add_block(self, data):
        # Mengambil hash dari blok terakhir sebagai pointer
        last_block = self.chain[-1]             # [TAG: Ambil Blok Terakhir] Mendapatkan blok paling ujung saat ini
        new_block = Block(last_block.index + 1, data, last_block.hash) # [TAG: Buat Blok Baru] Menghubungkan hash sebelumnya
        self.chain.append(new_block)            # [TAG: Simpan Blok] Memasukkan blok baru ke list rantai

    # [TAG: Cek Keamanan] Memeriksa apakah seluruh rantai aman dari manipulasi data
    def is_chain_valid(self):
        # Loop dari blok ke-1 (setelah Genesis) sampai akhir
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]       # [TAG: Blok Saat Ini] Blok yang sedang diperiksa
            previous_block = self.chain[i-1]    # [TAG: Blok Sebelumnya] Blok patokan di depannya

            # Cek apakah hash saat ini valid
            # [TAG: Cek Integritas Data] Jika data diubah, hasil calculate_hash() tidak akan cocok dengan hash lama
            if current_block.hash != current_block.calculate_hash():
                return False                    # [TAG: Data Dimanipulasi] Rantai tidak valid

            # Cek apakah pointer prev_hash merujuk ke blok sebelumnya dengan benar
            # [TAG: Cek Sambungan Rantai] Memastikan prev_hash di blok saat ini sama dengan hash blok sebelumnya
            if current_block.prev_hash != previous_block.hash:
                return False                    # [TAG: Rantai Terputus] Rantai tidak valid

        return True                             # [TAG: Rantai Aman] Semua blok terverifikasi valid