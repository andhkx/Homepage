
-- ======================================================
-- Database: andhikabakery (Normalisasi versi benar)
-- Dibuat oleh ChatGPT (GPT-5) untuk Andhika
-- ======================================================

CREATE DATABASE IF NOT EXISTS andhikabakery;
USE andhikabakery;

-- ========================
-- 1. Tabel Pelanggan
-- ========================
CREATE TABLE tbl_pelanggan (
    no_pelanggan VARCHAR(6) PRIMARY KEY,
    nama VARCHAR(30),
    alamat VARCHAR(30)
) ENGINE=InnoDB;

-- ========================
-- 2. Tabel Barang
-- ========================
CREATE TABLE tbl_barang (
    no_barang VARCHAR(6) PRIMARY KEY,
    nama_barang VARCHAR(30),
    harga INT(6)
) ENGINE=InnoDB;

-- ========================
-- 3. Tabel Head (Invoice)
-- ========================
CREATE TABLE tbl_head (
    no_invoice VARCHAR(15) PRIMARY KEY,
    no_pelanggan VARCHAR(6),
    tanggal DATE,
    total_bayar INT(7),
    ongkir INT(7),
    FOREIGN KEY (no_pelanggan) REFERENCES tbl_pelanggan(no_pelanggan)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ========================
-- 4. Tabel Detail (Rincian Barang)
-- ========================
CREATE TABLE tbl_detail (
    id_detail INT AUTO_INCREMENT PRIMARY KEY,
    no_invoice VARCHAR(15),
    no_barang VARCHAR(6),
    jumlah INT(3),
    subtotal INT(7),
    FOREIGN KEY (no_invoice) REFERENCES tbl_head(no_invoice)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (no_barang) REFERENCES tbl_barang(no_barang)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ========================
-- 5. Contoh Data
-- ========================

INSERT INTO tbl_pelanggan VALUES
('C00001', 'APOTEK K24', 'Babakan Asih');

INSERT INTO tbl_barang VALUES
('B00001', 'THE SOSRO', 3600),
('B00002', 'ROTI MAHKOTA', 13000),
('B00003', 'ROTI KEJU', 11000),
('B00004', 'ROTI COKLAT', 9000),
('B00005', 'ROTI ABON SAPI', 13000);

INSERT INTO tbl_head VALUES
('20230329-00001', 'C00001', '2023-03-29', 250000, 0);

INSERT INTO tbl_detail (no_invoice, no_barang, jumlah, subtotal) VALUES
('20230329-00001', 'B00001', 5, 18000),
('20230329-00001', 'B00002', 5, 65000),
('20230329-00001', 'B00003', 5, 55000),
('20230329-00001', 'B00004', 5, 45000),
('20230329-00001', 'B00005', 5, 65000);
