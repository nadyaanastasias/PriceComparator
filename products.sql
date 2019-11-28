-- Isi dari database "Buram"

DROP TABLE IF EXISTS `keretabayi`;

CREATE TABLE `keretabayi` (
  `idkb` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `namap` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL
);

LOCK TABLES `keretabayi` WRITE;

UNLOCK TABLES;


DROP TABLE IF EXISTS `perlmandi`;

CREATE TABLE `perlmandi` (
  `idpm` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `namap` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL
);

LOCK TABLES `perlmandi` WRITE;

UNLOCK TABLES;


DROP TABLE IF EXISTS `mainan`;

CREATE TABLE `mainan` (
  `idm` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `namap` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL
);

LOCK TABLES `mainan` WRITE;

UNLOCK TABLES;


DROP TABLE IF EXISTS `handuk`;

CREATE TABLE `handuk` (
  `idh` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `namap` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL
);

LOCK TABLES `handuk` WRITE;

UNLOCK TABLES;


DROP TABLE IF EXISTS `makananbayi`;

CREATE TABLE `makananbayi` (
  `idmb` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `namap` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL
);

LOCK TABLES `makananbayi` WRITE;

UNLOCK TABLES;