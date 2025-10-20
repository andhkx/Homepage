-- ===================================================
-- DATABASE: Andhika_elektronik
-- TABEL: pelanggan, barang, head, detail
-- ===================================================

CREATE DATABASE IF NOT EXISTS Andhika_elektronik;
USE Andhika_elektronik;

-- ==============================
-- TABEL PELANGGAN
-- ==============================
CREATE TABLE pelanggan (
    kode_pelanggan CHAR(4) PRIMARY KEY,
    nama_pelanggan VARCHAR(50) NOT NULL
);

-- ==============================
-- TABEL BARANG
-- ==============================
CREATE TABLE barang (
    kode_barang CHAR(5) PRIMARY KEY,
    nama_barang VARCHAR(50) NOT NULL,
    harga_satuan INT NOT NULL
);

-- ==============================
-- TABEL HEAD (nota / pembelian)
-- ==============================
CREATE TABLE head (
    id_nota CHAR(6) PRIMARY KEY,
    kode_pelanggan CHAR(4),
    tgl DATE NOT NULL,
    total_bayar INT NOT NULL,
    FOREIGN KEY (kode_pelanggan) REFERENCES pelanggan(kode_pelanggan)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ==============================
-- TABEL DETAIL
-- ==============================
CREATE TABLE detail (
    id_detail CHAR(6) PRIMARY KEY,
    id_nota CHAR(6),
    kode_barang CHAR(5),
    jumlah_barang INT NOT NULL,
    total_harga INT NOT NULL,
    FOREIGN KEY (id_nota) REFERENCES head(id_nota)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (kode_barang) REFERENCES barang(kode_barang)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ===================================================
-- DATA AWAL
-- ===================================================

-- Pelanggan
INSERT INTO pelanggan VALUES
('P001', 'Heni'),
('P002', 'Arif');

-- Barang
INSERT INTO barang VALUES
('PR001', 'Printer HP', 450000),
('SC002', 'Scanner UX', 400000),
('MN015', 'Monitor 15"', 700000),
('CR005', 'CDRW Asus', 350000);

-- Head (nota)
INSERT INTO head VALUES
('NC001', 'P001', '2004-03-03', 850000),
('NC002', 'P002', '2004-03-05', 1050000);

-- Detail
INSERT INTO detail VALUES
('D0001', 'NC001', 'PR001', 1, 450000),
('D0002', 'NC001', 'SC002', 1, 400000),
('D0003', 'NC002', 'MN015', 1, 700000),
('D0004', 'NC002', 'CR005', 1, 350000);
