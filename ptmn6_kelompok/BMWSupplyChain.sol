// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BMWSupplyChain {
    
    // 1. Struktur Data (Struct) untuk informasi rantai pasok BMW
    struct TrackingStep {
        string model;
        string tahap;
        string lokasi;
        string keterangan;
        uint256 timestamp;
    }

    // 2. Pemetaan (Mapping) dari nomor VIN ke riwayat tahap pasok
    mapping(string => TrackingStep[]) private vehicleLedger;

    // Event untuk mencatat log aktivitas di blockchain
    event StepAdded(string indexed vin, string model, string tahap, uint256 timestamp);

    // 3. Alur Fungsi: Tambah Data (Create)
    function addTrackingStep(
        string memory _vin,
        string memory _model,
        string memory _tahap,
        string memory _lokasi,
        string memory _keterangan
    ) public {
        TrackingStep memory newStep = TrackingStep({
            model: _model,
            tahap: _tahap,
            lokasi: _lokasi,
            keterangan: _keterangan,
            timestamp: block.timestamp
        });

        // Menyimpan data ke mapping berdasarkan VIN kendaraan
        vehicleLedger[_vin].push(newStep);
        
        // Memicu event log
        emit StepAdded(_vin, _model, _tahap, block.timestamp);
    }

    // Fungsi pembaca untuk melihat seluruh riwayat perjalanan berdasarkan VIN
    function getVehicleHistory(string memory _vin) public view returns (TrackingStep[] memory) {
        return vehicleLedger[_vin];
    }
}