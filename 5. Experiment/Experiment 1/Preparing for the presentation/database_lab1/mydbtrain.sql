-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: mydbtrain
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `checker`
--

DROP TABLE IF EXISTS `checker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `checker` (
  `name` varchar(20) DEFAULT NULL,
  `idcard` char(19) NOT NULL,
  `beauid` int DEFAULT NULL,
  `workage` int DEFAULT NULL,
  PRIMARY KEY (`idcard`),
  KEY `beauid` (`beauid`),
  CONSTRAINT `checker_ibfk_1` FOREIGN KEY (`beauid`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checker`
--

LOCK TABLES `checker` WRITE;
/*!40000 ALTER TABLE `checker` DISABLE KEYS */;
/*!40000 ALTER TABLE `checker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checklist`
--

DROP TABLE IF EXISTS `checklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `checklist` (
  `coachid` int DEFAULT NULL,
  `id` int NOT NULL,
  `timedate` char(9) DEFAULT NULL,
  `checkerid` char(19) DEFAULT NULL,
  `checkpart` varchar(80) DEFAULT NULL,
  `result` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `coachid` (`coachid`),
  KEY `checkerid` (`checkerid`),
  FULLTEXT KEY `checkpart` (`checkpart`),
  CONSTRAINT `checklist_ibfk_1` FOREIGN KEY (`coachid`) REFERENCES `traincoach` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `checklist_ibfk_2` FOREIGN KEY (`checkerid`) REFERENCES `checker` (`idcard`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checklist`
--

LOCK TABLES `checklist` WRITE;
/*!40000 ALTER TABLE `checklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `checklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platform`
--

DROP TABLE IF EXISTS `platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platform` (
  `id` int DEFAULT NULL,
  `stationbelong` varchar(30) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `kind` enum('side','island') DEFAULT NULL,
  KEY `stationbelong` (`stationbelong`),
  CONSTRAINT `platform_ibfk_1` FOREIGN KEY (`stationbelong`) REFERENCES `trainstation` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platform`
--

LOCK TABLES `platform` WRITE;
/*!40000 ALTER TABLE `platform` DISABLE KEYS */;
INSERT INTO `platform` VALUES (1,'harbin',520,'side'),(2,'harbin',560,'island');
/*!40000 ALTER TABLE `platform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `railwaybeureau`
--

DROP TABLE IF EXISTS `railwaybeureau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `railwaybeureau` (
  `id` int NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `numberofstation` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `railwaybeureau`
--

LOCK TABLES `railwaybeureau` WRITE;
/*!40000 ALTER TABLE `railwaybeureau` DISABLE KEYS */;
INSERT INTO `railwaybeureau` VALUES (10001,'harbin_beureau','harbin',2),(10003,'shijiazhuang_beureau','shijiazhuang',0),(11000,'northeast_beureau','harbin',1),(11001,'china_center_beureau','beijing',3),(11011,'beijing_beureau','beijing',3),(12001,'shenyang_beureau','shenyang',2),(12002,'dalian_beureau','dalian',2),(12005,'changchun_beureau','changchun',2);
/*!40000 ALTER TABLE `railwaybeureau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traincaptain`
--

DROP TABLE IF EXISTS `traincaptain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traincaptain` (
  `name` varchar(20) DEFAULT NULL,
  `idcard` char(19) NOT NULL,
  `beauid` int DEFAULT NULL,
  `workage` int DEFAULT NULL,
  PRIMARY KEY (`idcard`),
  KEY `beauid` (`beauid`),
  CONSTRAINT `traincaptain_ibfk_1` FOREIGN KEY (`beauid`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traincaptain`
--

LOCK TABLES `traincaptain` WRITE;
/*!40000 ALTER TABLE `traincaptain` DISABLE KEYS */;
/*!40000 ALTER TABLE `traincaptain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traincoach`
--

DROP TABLE IF EXISTS `traincoach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traincoach` (
  `id` int NOT NULL,
  `trainnub` varchar(6) DEFAULT NULL,
  `traindate` char(9) DEFAULT NULL,
  `kind` enum('yingwo','yingzuo','ruanzuo','ruanwo','canche','xingli','kongtiaofadian','yideng','erdeng','shangwu','shangwu_yideng','gaoruan','ruanbao') DEFAULT NULL,
  `upperid` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `upperid` (`upperid`),
  CONSTRAINT `traincoach_ibfk_1` FOREIGN KEY (`upperid`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traincoach`
--

LOCK TABLES `traincoach` WRITE;
/*!40000 ALTER TABLE `traincoach` DISABLE KEYS */;
/*!40000 ALTER TABLE `traincoach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traindriver`
--

DROP TABLE IF EXISTS `traindriver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traindriver` (
  `name` varchar(20) DEFAULT NULL,
  `idcard` char(19) NOT NULL,
  `beureauid` int DEFAULT NULL,
  `workage` int DEFAULT NULL,
  PRIMARY KEY (`idcard`),
  KEY `beureauid` (`beureauid`),
  CONSTRAINT `traindriver_ibfk_1` FOREIGN KEY (`beureauid`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traindriver`
--

LOCK TABLES `traindriver` WRITE;
/*!40000 ALTER TABLE `traindriver` DISABLE KEYS */;
INSERT INTO `traindriver` VALUES ('盖伦','111111222222333333',10001,10),('努努和威朗普','111112222211111222',11011,32),('墨菲特','111113333355555135',10001,1),('艾希','123456123456123456',11000,8),('易','123456789012345678',11000,16),('亚索','123456789123456789',11011,18),('莫德凯撒','198765098765098765',11000,23),('科加斯','234567890198765432',11001,1),('永恩','998877665544332211',11011,33);
/*!40000 ALTER TABLE `traindriver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainnumber`
--

DROP TABLE IF EXISTS `trainnumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainnumber` (
  `numberid` varchar(6) DEFAULT NULL,
  `startdata` char(9) DEFAULT NULL,
  `startstation` varchar(30) DEFAULT NULL,
  `endstation` varchar(30) DEFAULT NULL,
  `passstation` varchar(30) DEFAULT NULL,
  `driver` char(18) DEFAULT NULL,
  `captain` char(18) DEFAULT NULL,
  KEY `passstation` (`passstation`),
  KEY `driver` (`driver`),
  KEY `captain` (`captain`),
  CONSTRAINT `trainnumber_ibfk_1` FOREIGN KEY (`passstation`) REFERENCES `trainstation` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `trainnumber_ibfk_2` FOREIGN KEY (`driver`) REFERENCES `traindriver` (`idcard`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `trainnumber_ibfk_3` FOREIGN KEY (`captain`) REFERENCES `traincaptain` (`idcard`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainnumber`
--

LOCK TABLES `trainnumber` WRITE;
/*!40000 ALTER TABLE `trainnumber` DISABLE KEYS */;
/*!40000 ALTER TABLE `trainnumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainserver`
--

DROP TABLE IF EXISTS `trainserver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainserver` (
  `name` varchar(20) DEFAULT NULL,
  `idcard` char(19) NOT NULL,
  `beauid` int DEFAULT NULL,
  `workage` int DEFAULT NULL,
  `captainnumber` char(19) DEFAULT NULL,
  PRIMARY KEY (`idcard`),
  KEY `beauid` (`beauid`),
  CONSTRAINT `trainserver_ibfk_1` FOREIGN KEY (`beauid`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainserver`
--

LOCK TABLES `trainserver` WRITE;
/*!40000 ALTER TABLE `trainserver` DISABLE KEYS */;
/*!40000 ALTER TABLE `trainserver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainstation`
--

DROP TABLE IF EXISTS `trainstation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainstation` (
  `name` varchar(30) NOT NULL,
  `city` varchar(20) DEFAULT NULL,
  `upbeureau` int DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `upbeureau` (`upbeureau`),
  CONSTRAINT `trainstation_ibfk_1` FOREIGN KEY (`upbeureau`) REFERENCES `railwaybeureau` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainstation`
--

LOCK TABLES `trainstation` WRITE;
/*!40000 ALTER TABLE `trainstation` DISABLE KEYS */;
INSERT INTO `trainstation` VALUES ('beijing','beijing',11001),('beijing_chaoyang','beijing',11011),('beijing_north','beijing',11001),('beijing_south','beijing',11011),('beijing_west','beijing',11011),('changchun','changchun',12005),('changchun_west','changchun',12005),('dalian','dalian',12002),('dalian_north','dalian',12002),('harbin','harbin',10001),('harbin_south','harbin',11000),('harbin_west','harbin',10001),('liaoning_chaoyang','chaoyang',12001),('shenyang','shenyang',12001),('shenyang_north','shenyang',11001);
/*!40000 ALTER TABLE `trainstation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-23 16:43:59
