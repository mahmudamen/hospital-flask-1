-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: erp
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `PatientList`
--

DROP TABLE IF EXISTS `PatientList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PatientList` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PatientName` varchar(155) DEFAULT NULL,
  `Address` varchar(245) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `CreatedBy` varchar(45) DEFAULT NULL,
  `CreatedDate` varchar(45) DEFAULT NULL,
  `ServID` varchar(45) DEFAULT NULL,
  `UserName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PatientList`
--

LOCK TABLES `PatientList` WRITE;
/*!40000 ALTER TABLE `PatientList` DISABLE KEYS */;
INSERT INTO `PatientList` VALUES (3,'sddddddddddddddd','ddddddddddddddddddd',NULL,NULL,NULL,'51','mmmm'),(4,'aaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaa',NULL,NULL,NULL,'232','mmmm'),(5,'sdfsfasfsafasfa','sdfasdfafasdfas',NULL,NULL,NULL,'324','mmmm'),(6,'dfsd','asfasfdsdfsafssdfff',NULL,NULL,NULL,'213231','mmmm'),(7,'aDSDS','egypt aswan',NULL,NULL,NULL,'23','mmmm'),(8,'sdfsda','fdsafsadf',NULL,NULL,NULL,'py','mmmm'),(9,'fgddhfdvcbc','sfgsgdgdgd',NULL,NULL,NULL,'NV','mmmm');
/*!40000 ALTER TABLE `PatientList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Role`
--

DROP TABLE IF EXISTS `Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Role` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `RoleName` varchar(45) NOT NULL,
  `RoleDescription` varchar(300) NOT NULL,
  `IsActive` bit(1) NOT NULL,
  `ValidFrom` date NOT NULL,
  `CreateDate` date NOT NULL,
  `CreatedTime` time NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Role`
--

LOCK TABLES `Role` WRITE;
/*!40000 ALTER TABLE `Role` DISABLE KEYS */;
/*!40000 ALTER TABLE `Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ServList`
--

DROP TABLE IF EXISTS `ServList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ServList` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ServName` varchar(145) CHARACTER SET latin1 DEFAULT NULL,
  `ServType` int(11) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT '0.00',
  `IsActive` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ServList`
--

LOCK TABLES `ServList` WRITE;
/*!40000 ALTER TABLE `ServList` DISABLE KEYS */;
INSERT INTO `ServList` VALUES (5,'aksdfjlk',NULL,322.00,NULL);
/*!40000 ALTER TABLE `ServList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserRole`
--

DROP TABLE IF EXISTS `UserRole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserRole` (
  `ID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `RoleID` int(11) NOT NULL,
  `IsActive` bit(1) NOT NULL,
  `ValidFrom` date NOT NULL,
  `CreatedBy` int(11) NOT NULL,
  `CreatedDate` date NOT NULL,
  `CreatedTime` time NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserRole`
--

LOCK TABLES `UserRole` WRITE;
/*!40000 ALTER TABLE `UserRole` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserRole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `body` varchar(305) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `d` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(300) NOT NULL,
  `userID` int(11) DEFAULT NULL,
  `RoleID` int(11) DEFAULT NULL,
  `Entrykey` varchar(45) DEFAULT NULL,
  `Telephone` varchar(45) DEFAULT NULL,
  `IsActive` bit(1) DEFAULT NULL,
  `CreatedBy` int(11) DEFAULT NULL,
  `ValidFrom` date DEFAULT NULL,
  `CreatedDate` date DEFAULT NULL,
  `CreatedTime` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'نيتمبمسيشسي','mahmudamen@gmail.com','mahmud','$5$rounds=535000$wYgEDkvq8VzXGp03$rMG6YkMoWG6JpFapV54HSuEA40xwxwJ/vqFSiGLk9k2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'MAHMO','mahmudamen@gmail.com','mmmm','$5$rounds=535000$8eGT894iXiotbIlY$LhoUN/YdF9HHENriSFSbXQAQTwebT8nv8AE7U7ro0C6',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'sdfs','sdfasdfadfafasdfas','asdfasfmmmm','$5$rounds=535000$vlUp4syreBJbz4u9$AyO/TtgptDJojhoLTGEPEMdxI6TA0Y.XiXRhs9RaYQ8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'erp'
--

--
-- Dumping routines for database 'erp'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-24 19:32:11
