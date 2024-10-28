-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: zomato
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `sno` int NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `restaurant` varchar(40) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Pizza','Dominos',249),(2,'Burger','McDonalds',79),(3,'Sandwich','Sagar Gaire',79),(4,'Noodles','Kakashi\'s Kitchen',89),(5,'Pasta','Sharma Vishnu',99),(6,'French fries','F for fries',69),(7,'Anglio Olio','Pin & Pan',169),(8,'Chilli Paneer','Sagar gaire',240),(9,'Manchurian','Ganesham',79),(10,'Fried rice','Ganesham',89),(11,'Chole kulche','Sharma Vishnu',219),(12,'Paneer kulche','Sagar Gaire',259),(13,'Paneer Veg Rolls','Rolls mania',169),(14,'Paneer Mushroom Rolls','Rolls mania',179),(15,'Cheesy BBQ Soya Chaap Roll','Rolls mania',219),(16,'Sev Tomato','Vrindavan Dhaba',89),(17,'Biryani','Biryani by Kilo',319),(18,'Malai Kofta','Vrindavan Dhaba',159),(19,'Jeera Rice','Vrindavan Dhaba',79),(20,'Mix Veg','Vrindavan Dhaba',119),(21,'Dal Tadka','Vrindavan Dhaba',99);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-28 11:54:58
