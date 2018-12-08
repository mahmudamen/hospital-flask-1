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
-- Table structure for table `Dept`
--

DROP TABLE IF EXISTS `Dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dept` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DeptName` varchar(45) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL,
  `IsActive` bit(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dept`
--

LOCK TABLES `Dept` WRITE;
/*!40000 ALTER TABLE `Dept` DISABLE KEYS */;
INSERT INTO `Dept` VALUES (1,'الداخلي',7,NULL),(2,'الخارجي',7,NULL);
/*!40000 ALTER TABLE `Dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ItemList`
--

DROP TABLE IF EXISTS `ItemList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ItemList` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(145) DEFAULT NULL,
  `ItemType` int(11) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT '0.00',
  `IsActive` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ItemList`
--

LOCK TABLES `ItemList` WRITE;
/*!40000 ALTER TABLE `ItemList` DISABLE KEYS */;
INSERT INTO `ItemList` VALUES (3,'ستروسين',NULL,75.00,NULL),(4,'sdfadff',NULL,1512.00,NULL),(5,'sdfafdas',NULL,323.00,NULL),(6,'sdfasdfa',NULL,232.00,NULL),(7,'sdfsa',NULL,2332.00,NULL),(8,'bbbbbbbb',NULL,233.00,NULL);
/*!40000 ALTER TABLE `ItemList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Patient` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PatientName` varchar(155) DEFAULT NULL,
  `Address` varchar(245) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `CreatedBy` varchar(45) DEFAULT NULL,
  `ServID` int(11) DEFAULT NULL,
  `UserName` varchar(45) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT '0.00',
  `ServName` varchar(145) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL,
  `IsActive` bit(1) DEFAULT NULL,
  `CreatedDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (42,'اشرف محمد','اسوان خور عواضة',NULL,NULL,5,NULL,150.00,'كشف مستعجل ',NULL,NULL,NULL),(44,'محمود امين','اسوان صحاري',NULL,NULL,4,NULL,25.00,'استشارة',NULL,NULL,NULL),(47,'حسين عبد العظيم','اسوان كوم امبو',NULL,NULL,2,NULL,50.00,'x ray',NULL,NULL,'2018-12-01 01:05:42');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

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
  `ServID` int(11) DEFAULT NULL,
  `UserName` varchar(45) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT '0.00',
  `ServName` varchar(145) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL,
  `IsActive` bit(1) NOT NULL,
  PRIMARY KEY (`ID`,`IsActive`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PatientList`
--

LOCK TABLES `PatientList` WRITE;
/*!40000 ALTER TABLE `PatientList` DISABLE KEYS */;
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
  `ServName` varchar(145) DEFAULT NULL,
  `ServType` int(11) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT '0.00',
  `IsActive` int(11) DEFAULT NULL,
  `DeptID` int(11) DEFAULT NULL,
  `DeptName` varchar(45) DEFAULT NULL,
  `CreatedDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ServList`
--

LOCK TABLES `ServList` WRITE;
/*!40000 ALTER TABLE `ServList` DISABLE KEYS */;
INSERT INTO `ServList` VALUES (2,'كشف عادي',NULL,50.00,NULL,NULL,NULL,'2018-12-01 19:20:04'),(5,'كشف مستعجل ',NULL,150.00,NULL,NULL,NULL,'2018-12-01 19:20:04'),(6,'استشارة',NULL,322.00,NULL,NULL,NULL,'2018-12-01 19:20:04'),(7,'x ray',NULL,75.00,NULL,NULL,NULL,'2018-12-01 19:20:04'),(8,'sadfasfa',NULL,324.00,NULL,NULL,NULL,'2018-12-01 19:20:04');
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
  `IsActive` bit(1) DEFAULT NULL,
  `ValidFrom` date DEFAULT NULL,
  `CreatedBy` int(11) DEFAULT NULL,
  `CreatedDate` date DEFAULT NULL,
  `CreatedTime` time DEFAULT NULL,
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
-- Temporary table structure for view `new_view`
--

DROP TABLE IF EXISTS `new_view`;
/*!50001 DROP VIEW IF EXISTS `new_view`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `new_view` AS SELECT 
 1 AS `ID`,
 1 AS `PatientName`,
 1 AS `Address`,
 1 AS `Age`,
 1 AS `CreatedBy`,
 1 AS `CreatedDate`,
 1 AS `ServID`,
 1 AS `UserName`,
 1 AS `Price`*/;
SET character_set_client = @saved_cs_client;

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'meno','mahmudamen@gmail.com','mahmud','$5$rounds=535000$wYgEDkvq8VzXGp03$rMG6YkMoWG6JpFapV54HSuEA40xwxwJ/vqFSiGLk9k2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'meno','mahmudamen@gmail.com','back.kode','$5$rounds=535000$3oAHjYSLHAAv7zHE$Yp9.GSPaZGvK96sqrhRPCGGVPX/CYGt45Mdp5MxKsn5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,'asfasdfa','sfasfsafsa','aaaaaa','$5$rounds=535000$/briUc2TnpNjNYji$3EYUfVJQg6B3R11Lq4t.DaAiKVApVQYVuhp053JVzZ2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,'asdfasdfas','sdfafasdf','sadfa','$5$rounds=535000$AuDUgqzMAIksFQjR$oyaGbwZ02nbs.ILviVwAFe90B9wh5nBfLc3WLB5PKdC',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xpatient`
--

DROP TABLE IF EXISTS `xpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xpatient` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PatientName` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xpatient`
--

LOCK TABLES `xpatient` WRITE;
/*!40000 ALTER TABLE `xpatient` DISABLE KEYS */;
/*!40000 ALTER TABLE `xpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'erp'
--

--
-- Dumping routines for database 'erp'
--
/*!50003 DROP FUNCTION IF EXISTS `func01` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `func01`(value1 INT ) RETURNS decimal(10,2)
    DETERMINISTIC
BEGIN
  DECLARE var_name decimal(15,2);
  SET var_name = 0;
  SELECT Price INTO var_name
    FROM ServList
    WHERE ID = value1;
  RETURN var_name;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `new_view`
--

/*!50001 DROP VIEW IF EXISTS `new_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `new_view` AS select `PatientList`.`ID` AS `ID`,`PatientList`.`PatientName` AS `PatientName`,`PatientList`.`Address` AS `Address`,`PatientList`.`Age` AS `Age`,`PatientList`.`CreatedBy` AS `CreatedBy`,`PatientList`.`CreatedDate` AS `CreatedDate`,`PatientList`.`ServID` AS `ServID`,`PatientList`.`UserName` AS `UserName`,`PatientList`.`Price` AS `Price` from `PatientList` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-04 19:43:33
