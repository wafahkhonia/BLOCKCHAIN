# Laporan Praktikum Smart Contract: Supply Chain Kopi

**Mata Kuliah:** Blockchain
**Nama:** WAFAH KHONIA 
**NIM:** 2530801081 
**Kelas:** INFORMATIKA 3D 

---

## A. Tujuan Praktikum

1. Mahasiswa memahami struktur dasar bahasa pemrograman Solidity (`pragma`, *State Variables*, `enum`, `struct`, `mapping`, dan *Functions*).
2. Mahasiswa mampu mengoperasikan Remix IDE untuk melakukan *compile* dan *deploy* *Smart Contract* ke *local environment* (Remix VM).
3. Mahasiswa mampu merancang logika sistem Rantai Pasok (*Supply Chain*) sederhana ke dalam sebuah *Smart Contract*.
4. Mahasiswa memahami fungsi `msg.sender` dan `require` untuk kontrol akses dan validasi data pada *Smart Contract*.

---

## B. Pengenalan Lingkungan Kerja (Remix IDE)

Untuk menulis, menguji, dan menyebarkan (*deploy*) *Smart Contract*, pengembangan dilakukan menggunakan IDE berbasis web resmi dari Ethereum, yaitu **Remix IDE** (https://remix.ethereum.org/). 

Keunggulan penggunaan Remix IDE antara lain:
* Tidak memerlukan instalasi *software* lokal yang berat.
* Menyediakan lingkungan simulasi *Virtual Machine* (Remix VM) lengkap dengan akun dompet *testnet* bernilai ETH virtual.
* Dilengkapi dengan alat pengujian interaktif untuk mengeksekusi fungsi *Smart Contract* secara langsung.

---

## C. Kode Program (SupplyChainKopi.sol)

Berikut adalah kode program Solidity yang diimplementasikan dalam praktikum ini:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SupplyChainKopi {

    // 1. Enum: Mendefinisikan pilihan status yang kaku (tidak bisa diisi sembarang teks)
    enum StatusKopi { Panen, Diproses, Dikirim, Diterima }

    // 2. Struct: Membuat tipe data bentukan (seperti Object/Dictionary)
    struct Kopi {
        uint256 id;
        string namaPetani;
        uint256 beratKg;
        StatusKopi status;
        address pemilikSaatIni; // Menyimpan alamat dompet (wallet) pemilik
    }

    // 3. State Variables: Data yang akan disimpan permanen di dalam Blockchain
    uint256 public totalKopi = 0;

    // Mapping: Berfungsi seperti kamus (Dictionary) untuk mencari Kopi berdasarkan ID
    mapping(uint256 => Kopi) public daftarKopi;

    // 4. Fungsi Tambah Data
    function daftarPanenBaru(string memory _namaPetani, uint256 _beratKg) public {
        // Increment ID Kopi
        totalKopi += 1;

        // Memasukkan data ke dalam mapping
        daftarKopi[totalKopi] = Kopi({
            id: totalKopi,
            namaPetani: _namaPetani,
            beratKg: _beratKg,
            status: StatusKopi.Panen,
            pemilikSaatIni: msg.sender // msg.sender adalah wallet orang yang mengeklik fungsi ini
        });
    }

    // 5. Fungsi Update Status
    function updateStatus(uint256 _id, StatusKopi _statusBaru) public {
        // Validasi 1: Pastikan ID kopi valid (ada di dalam sistem)
        require(_id > 0 && _id <= totalKopi, "Kopi tidak ditemukan di sistem!");

        // Validasi 2: HANYA pemilik saat ini yang boleh mengubah statusnya!
        // Jika orang lain mencoba, transaksi akan dibatalkan (Revert)
        require(msg.sender == daftarKopi[_id].pemilikSaatIni, "Ditolak: Anda bukan pemilik kopi ini!");

        // Jika lolos validasi, ubah statusnya
        daftarKopi[_id].status = _statusBaru;
    }
}
```

---

## D. Langkah Kerja Praktikum & Bukti Eksekusi

### 1. Autentikasi dan Lingkungan Kerja Remix IDE
Membuka halaman [Remix IDE](https://remix.ethereum.org/) dan melakukan autentikasi *login* menggunakan akun Google (Gmail) untuk menyimpan workspace.

<img width="1433" height="637" alt="image" src="https://github.com/user-attachments/assets/04b56304-f51b-48fe-8e67-4df4f8410407" />
*Gambar 1: Tampilan konfirmasi login ke Remix IDE.*

### 2. Pembuatan File dan Penulisan Kode
Pada panel **File Explorer** sebelah kiri, buat file baru bernama `SupplyChainKopi.sol` di dalam folder `contracts`, lalu ketik/tempel kode program Solidity di atas.

<img width="1335" height="643" alt="image" src="https://github.com/user-attachments/assets/42990d34-b8f5-4b84-89e8-aef56592231c" />
*Gambar 2: Pembuatan file SupplyChainKopi.sol dan penulisan kode Solidity pada editor.*

### 3. Kompilasi Kode (Compile)
Buka tab **Solidity Compiler** pada menu navigasi sebelah kiri. Pilih versi *compiler* `0.8.20` (sesuai `pragma`), lalu klik tombol **Compile SupplyChainKopi.sol**. Indikator centang hijau menandakan kode berhasil dikompilasi tanpa *error*.

<img width="1217" height="542" alt="image" src="https://github.com/user-attachments/assets/8bc42afe-7391-4df9-acac-97cd3ac7f22b" /> 
*Gambar 3: Proses kompilasi Smart Contract yang berhasil.*

### 4. Penyebaran Smart Contract (Deploy)
Buka tab **Deploy & Run Transactions**. Pastikan *Environment* teratur pada **Remix VM (Cancun/Shanghai)**. Pilih *Contract* `SupplyChainKopi`, lalu tekan tombol **Deploy**.

<img width="1237" height="598" alt="image" src="https://github.com/user-attachments/assets/45b17c43-5400-4db8-bb4f-b2463a58af5d" /> 
*Gambar 4: Eksekusi Deploy Smart Contract ke lingkungan simulasi Remix VM.*

---

## E. Pengujian Interaksi Fungsi (Testing)

Setelah *Smart Contract* berhasil di-*deploy*, pengujian dilakukan pada panel **Deployed Contracts**:

1. **Mendaftarkan Panen Baru (`daftarPanenBaru`)**:
   * Masukkan parameter: `_namaPetani: "Petani Robusta Garut"`, `_beratKg: 500`.
   * Klik **transact**. Transaksi berhasil dieksekusi dan `totalKopi` bertambah menjadi `1`.

2. **Pengecekan Data (`daftarKopi`)**:
   * Panggil fungsi `daftarKopi` dengan memasukkan ID `1`.
   * Output menampilkan data kopi: `id: 1`, `namaPetani: "Petani Robusta Garut"`, `beratKg: 500`, `status: 0` (Panen), dan `pemilikSaatIni` sesuai alamat *account* pengirim.

3. **Memperbarui Status (`updateStatus`)**:
   * Masukkan ID `1` dan nilai status `1` (`Diproses`).
   * Klik **transact**. Pembaruan status berhasil karena dipanggil oleh `msg.sender` yang merupakan pemilik sah kopi tersebut.

4. **Pengujian Kontrol Akses (`require`)**:
   * Mengubah akun pemanggil (*ACCOUNT*) di Remix VM ke alamat dompet lain.
   * Mencoba memanggil `updateStatus(1, 2)`.
   * **Hasil:** Transaksi gagal (*revert*) dengan pesan error: `"Ditolak: Anda bukan pemilik kopi ini!"`.

---

## F. Hasil dan Pembahasan

1. **`Enum` (`StatusKopi`)**: Menyediakan daftar konstanta bernilai integer konstan (`0 = Panen`, `1 = Diproses`, `2 = Dikirim`, `3 = Diterima`). Hal ini mencegah kesalahan penginputan teks status acak dan menghemat konsumsi *gas fee*.
2. **`Struct` (`Kopi`)**: Memungkinkan pengelompokan variabel dengan berbagai tipe data (ID, Nama, Berat, Status, Alamat Pemilik) ke dalam satu entitas objek tunggal.
3. **`Mapping` (`daftarKopi`)**: Menjadi basis data terdistribusi berbasis pasangan *Key-Value* (`uint256 => Kopi`) yang efisien untuk pencarian data langsung berdasarkan ID kopi tanpa perlu iterasi *looping*.
4. **`msg.sender`**: Menjamin keandalan identitas digital pengguna secara eksplisit berdasarkan alamat (*address*) kriptografi akun yang mengeksekusi fungsi.
5. **`require`**: Bertindak sebagai mekanisme keamanan (*assertion*) untuk memastikan bahwa syarat kelayakan (misalnya hak milik akun dan keberadaan ID) terpenuhi sebelum status disimpan secara permanen di blockchain.

---

## G. Kesimpulan

1. Praktikum ini berhasil mengimplementasikan *Smart Contract* **SupplyChainKopi** menggunakan bahasa Solidity pada **Remix IDE**.
2. Fitur-fitur dasar Solidity seperti `struct`, `mapping`, `enum`, `msg.sender`, dan `require` mampu membentuk sistem rantai pasok kopi transparan, aman, dan dapat diverifikasi (*auditable*).
3. Penggunaan `require` secara rinci terbukti efektif mencegah manipulasi data oleh pihak yang tidak memiliki hak akses (*unauthorized user*) pada ekosistem terdesentralisasi.
