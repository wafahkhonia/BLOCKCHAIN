// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SupplyChainKopi {

    // 1. Enum: Mendefinisikan pilihan status yang kaku (tidak bisa diisi sembarang teks)
    enum StatusKopi { Panen, Diproses, Dikirim, Diterima }

    // 2. Struct: Membuat tipe data bentukan (seperti Object/Dictionary di Python)
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