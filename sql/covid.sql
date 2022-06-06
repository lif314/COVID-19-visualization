/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.38-log : Database - covid
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`covid` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `covid`;

/*Table structure for table `details` */

DROP TABLE IF EXISTS `details`;

CREATE TABLE `details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime DEFAULT NULL,
  `province` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `confirm` int(11) DEFAULT NULL,
  `confirm_add` int(11) DEFAULT NULL,
  `heal` int(11) DEFAULT NULL,
  `dead` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `details` */

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `ds` datetime NOT NULL,
  `confirm` int(11) DEFAULT NULL,
  `confirm_add` int(11) DEFAULT NULL,
  `suspect` int(11) DEFAULT NULL,
  `suspect_add` int(11) DEFAULT NULL,
  `heal` int(11) DEFAULT NULL,
  `heal_add` int(11) DEFAULT NULL,
  `dead` int(11) DEFAULT NULL,
  `dead_add` int(11) DEFAULT NULL,
  PRIMARY KEY (`ds`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `history` */

/*Table structure for table `hotsearch` */

DROP TABLE IF EXISTS `hotsearch`;

CREATE TABLE `hotsearch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `hotsearch` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
