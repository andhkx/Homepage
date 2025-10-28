-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 27, 2025 at 06:51 AM
-- Server version: 5.7.39
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_nota_pembelian`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `kode_barang` varchar(6) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `harga_satuan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`kode_barang`, `nama_barang`, `harga_satuan`) VALUES
('CP001', 'Processor Intel i5', 2200000),
('CP002', 'Processor Ryzen 5', 2500000),
('CR005', 'CDRW Asus', 350000),
('CV987', 'HDMI Kabel', 90000),
('FD001', 'Flashdisk 32GB', 70000),
('FD002', 'Flashdisk 64GB', 120000),
('HD001', 'Harddisk 1TB', 650000),
('HD002', 'Harddisk 2TB', 950000),
('JX763', 'Jam', 200000),
('JX827', 'Speaker', 80000),
('MB001', 'Motherboard ASUS', 1500000),
('MB002', 'Motherboard MSI', 1800000),
('MC892', 'Keyboard', 200000),
('MN015', 'Monitor 15\"', 700000),
('PR001', 'Printer HP', 450000),
('RM001', 'RAM 8GB DDR4', 400000),
('RM002', 'RAM 16GB DDR4', 750000),
('SC002', 'Scanner UX', 400000),
('VC001', 'VGA GTX 1650', 2500000),
('VC002', 'VGA RTX 3060', 5500000),
('XI872', 'Mouse', 50000);

-- --------------------------------------------------------

--
-- Table structure for table `detail_transaksi`
--

CREATE TABLE `detail_transaksi` (
  `nota` varchar(7) NOT NULL,
  `kode_barang` varchar(6) NOT NULL,
  `jumlah_barang` int(11) NOT NULL,
  `harga_satuan` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `detail_transaksi`
--

INSERT INTO `detail_transaksi` (`nota`, `kode_barang`, `jumlah_barang`, `harga_satuan`, `total_harga`) VALUES
('NC001', 'PR001', 1, 450000, 450000),
('NC001', 'SC002', 1, 400000, 400000),
('NC002', 'CR005', 1, 350000, 350000),
('NC002', 'MN015', 1, 700000, 700000),
('NC003', 'FD001', 2, 70000, 140000),
('NC003', 'MC892', 1, 200000, 200000),
('NC003', 'XI872', 1, 50000, 50000),
('NC004', 'CR005', 1, 350000, 350000),
('NC004', 'FD002', 2, 120000, 240000),
('NC005', 'HD001', 1, 650000, 650000),
('NC005', 'RM001', 2, 400000, 800000),
('NC006', 'FD002', 2, 120000, 240000),
('NC006', 'VC001', 1, 2500000, 2500000),
('NC007', 'MN015', 1, 700000, 700000),
('NC008', 'MB001', 1, 1500000, 1500000),
('NC008', 'XI872', 1, 50000, 50000),
('NC009', 'RM002', 1, 750000, 750000),
('NC009', 'VC002', 1, 5500000, 5500000),
('NC010', 'HD001', 1, 650000, 650000),
('NC010', 'JX827', 2, 80000, 160000),
('NC011', 'XI872', 5, 50000, 250000),
('NC012', 'FD002', 3, 120000, 360000),
('NC012', 'HD001', 1, 650000, 650000),
('NC012', 'PR001', 1, 450000, 450000),
('NC013', 'CP001', 1, 2200000, 2200000),
('NC013', 'FD001', 3, 70000, 210000),
('NC013', 'RM002', 1, 750000, 750000),
('NC014', 'JX763', 2, 200000, 400000),
('NC014', 'MC892', 1, 200000, 200000),
('NC014', 'XI872', 3, 50000, 150000),
('NC015', 'FD001', 1, 70000, 70000),
('NC015', 'MB002', 1, 1800000, 1800000),
('NC016', 'JX827', 4, 80000, 320000),
('NC016', 'SC002', 1, 400000, 400000),
('NC017', 'CP001', 1, 2200000, 2200000),
('NC017', 'VC001', 1, 2500000, 2500000),
('NC018', 'MC892', 2, 200000, 400000),
('NC018', 'XI872', 2, 50000, 100000),
('NC019', 'FD002', 2, 120000, 240000),
('NC019', 'HD002', 2, 950000, 1900000),
('NC019', 'JX827', 2, 80000, 160000),
('NC020', 'CP002', 1, 2500000, 2500000),
('NC020', 'FD001', 5, 70000, 350000),
('NC020', 'RM002', 1, 750000, 750000);

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `kode_pelanggan` varchar(5) NOT NULL,
  `nama_pelanggan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`kode_pelanggan`, `nama_pelanggan`) VALUES
('P001', 'Heru'),
('P002', 'Arif'),
('P003', 'Dewi'),
('P004', 'Rina'),
('P005', 'Bagas'),
('P006', 'Yusuf'),
('P007', 'Rizki'),
('P008', 'Wahyu'),
('P009', 'Lina'),
('P010', 'Tono'),
('P011', 'Dina'),
('P012', 'Sinta'),
('P013', 'Gilang'),
('P014', 'Novi'),
('P015', 'Andi'),
('P016', 'Farhan'),
('P017', 'Cici'),
('P018', 'Adit'),
('P019', 'Rudi'),
('P020', 'Mega');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `nota` varchar(7) NOT NULL,
  `tanggal_beli` date NOT NULL,
  `kode_pelanggan` varchar(5) NOT NULL,
  `total_bayar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`nota`, `tanggal_beli`, `kode_pelanggan`, `total_bayar`) VALUES
('NC001', '2025-10-01', 'P001', 850000),
('NC002', '2025-10-03', 'P002', 1050000),
('NC003', '2025-10-05', 'P003', 470000),
('NC004', '2025-10-06', 'P004', 540000),
('NC005', '2025-10-06', 'P005', 1200000),
('NC006', '2025-10-07', 'P006', 2750000),
('NC007', '2025-10-08', 'P007', 700000),
('NC008', '2025-10-09', 'P008', 1550000),
('NC009', '2025-10-10', 'P009', 6250000),
('NC010', '2025-10-11', 'P010', 810000),
('NC011', '2025-10-12', 'P011', 250000),
('NC012', '2025-10-12', 'P012', 1250000),
('NC013', '2025-10-13', 'P013', 3200000),
('NC014', '2025-10-13', 'P014', 950000),
('NC015', '2025-10-14', 'P015', 1750000),
('NC016', '2025-10-15', 'P016', 720000),
('NC017', '2025-10-15', 'P017', 4850000),
('NC018', '2025-10-16', 'P018', 510000),
('NC019', '2025-10-17', 'P019', 2600000),
('NC020', '2025-10-18', 'P020', 3550000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`kode_barang`);

--
-- Indexes for table `detail_transaksi`
--
ALTER TABLE `detail_transaksi`
  ADD PRIMARY KEY (`nota`,`kode_barang`),
  ADD KEY `kode_barang` (`kode_barang`);

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`kode_pelanggan`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`nota`),
  ADD KEY `kode_pelanggan` (`kode_pelanggan`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detail_transaksi`
--
ALTER TABLE `detail_transaksi`
  ADD CONSTRAINT `detail_transaksi_ibfk_1` FOREIGN KEY (`kode_barang`) REFERENCES `barang` (`kode_barang`),
  ADD CONSTRAINT `detail_transaksi_ibfk_2` FOREIGN KEY (`nota`) REFERENCES `transaksi` (`nota`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`kode_pelanggan`) REFERENCES `pelanggan` (`kode_pelanggan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
