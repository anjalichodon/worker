/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.4.28-MariaDB : Database - tn
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tn` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `tn`;

/*Table structure for table `app_booking` */

DROP TABLE IF EXISTS `app_booking`;

CREATE TABLE `app_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Requestdate` varchar(20) NOT NULL,
  `Bookingdate` varchar(20) NOT NULL,
  `paymentstatus` varchar(25) NOT NULL,
  `workerstatus` varchar(20) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `WORKER_id` int(11) NOT NULL,
  `paymentdate` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_booking_USER_id_15dec690_fk_app_user_id` (`USER_id`),
  KEY `app_booking_WORKER_id_47cfd425_fk_app_worker_id` (`WORKER_id`),
  CONSTRAINT `app_booking_USER_id_15dec690_fk_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `app_user` (`id`),
  CONSTRAINT `app_booking_WORKER_id_47cfd425_fk_app_worker_id` FOREIGN KEY (`WORKER_id`) REFERENCES `app_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_booking` */

insert  into `app_booking`(`id`,`Requestdate`,`Bookingdate`,`paymentstatus`,`workerstatus`,`USER_id`,`WORKER_id`,`paymentdate`) values 
(1,'12/05/2023','14/05/2023','paid','approved',1,1,'18/09/2023');

/*Table structure for table `app_bookingsub` */

DROP TABLE IF EXISTS `app_bookingsub`;

CREATE TABLE `app_bookingsub` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `BOOKING_id` int(11) NOT NULL,
  `SERVICE_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_bookingub_BOOKING_id_e78baba3_fk_app_booking_id` (`BOOKING_id`),
  KEY `app_bookingub_SERVICE_id_52a1a411_fk_app_service_id` (`SERVICE_id`),
  CONSTRAINT `app_bookingub_BOOKING_id_e78baba3_fk_app_booking_id` FOREIGN KEY (`BOOKING_id`) REFERENCES `app_booking` (`id`),
  CONSTRAINT `app_bookingub_SERVICE_id_52a1a411_fk_app_service_id` FOREIGN KEY (`SERVICE_id`) REFERENCES `app_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_bookingsub` */

insert  into `app_bookingsub`(`id`,`BOOKING_id`,`SERVICE_id`) values 
(3,1,4);

/*Table structure for table `app_category` */

DROP TABLE IF EXISTS `app_category`;

CREATE TABLE `app_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_category` */

insert  into `app_category`(`id`,`name`) values 
(3,'painter'),
(4,'dd'),
(5,'carpender');

/*Table structure for table `app_chat` */

DROP TABLE IF EXISTS `app_chat`;

CREATE TABLE `app_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(15) NOT NULL,
  `chat` varchar(20) NOT NULL,
  `type` varchar(50) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `WORKER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_chat_USER_id_16a353bc_fk_app_user_id` (`USER_id`),
  KEY `app_chat_WORKER_id_bcf2b1d4_fk_app_worker_id` (`WORKER_id`),
  CONSTRAINT `app_chat_USER_id_16a353bc_fk_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `app_user` (`id`),
  CONSTRAINT `app_chat_WORKER_id_bcf2b1d4_fk_app_worker_id` FOREIGN KEY (`WORKER_id`) REFERENCES `app_worker` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_chat` */

/*Table structure for table `app_feedback` */

DROP TABLE IF EXISTS `app_feedback`;

CREATE TABLE `app_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(25) NOT NULL,
  `date` varchar(15) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_feedback_USER_id_97cd3eed_fk_app_user_id` (`USER_id`),
  CONSTRAINT `app_feedback_USER_id_97cd3eed_fk_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_feedback` */

insert  into `app_feedback`(`id`,`feedback`,`date`,`USER_id`) values 
(2,'good','13/06/2023',1);

/*Table structure for table `app_login` */

DROP TABLE IF EXISTS `app_login`;

CREATE TABLE `app_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_login` */

insert  into `app_login`(`id`,`username`,`password`,`usertype`) values 
(1,'a','12','admin'),
(2,'d','f','worker'),
(3,'a','g','user');

/*Table structure for table `app_rating` */

DROP TABLE IF EXISTS `app_rating`;

CREATE TABLE `app_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(15) NOT NULL,
  `date` varchar(15) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `WORKER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_rating_USER_id_fd4e06db_fk_app_user_id` (`USER_id`),
  KEY `app_rating_WORKER_id_18ce12f0_fk_app_worker_id` (`WORKER_id`),
  CONSTRAINT `app_rating_USER_id_fd4e06db_fk_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `app_user` (`id`),
  CONSTRAINT `app_rating_WORKER_id_18ce12f0_fk_app_worker_id` FOREIGN KEY (`WORKER_id`) REFERENCES `app_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_rating` */

insert  into `app_rating`(`id`,`rating`,`date`,`USER_id`,`WORKER_id`) values 
(1,'5','6',1,1);

/*Table structure for table `app_service` */

DROP TABLE IF EXISTS `app_service`;

CREATE TABLE `app_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Amount` varchar(100) NOT NULL,
  `CATEGORY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_service_CATEGORY_id_397d9ea1_fk_app_category_id` (`CATEGORY_id`),
  CONSTRAINT `app_service_CATEGORY_id_397d9ea1_fk_app_category_id` FOREIGN KEY (`CATEGORY_id`) REFERENCES `app_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_service` */

insert  into `app_service`(`id`,`Amount`,`CATEGORY_id`) values 
(3,'',3),
(4,'654',4);

/*Table structure for table `app_user` */

DROP TABLE IF EXISTS `app_user`;

CREATE TABLE `app_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_user_LOGIN_id_b43bd763_fk_app_login_id` (`LOGIN_id`),
  CONSTRAINT `app_user_LOGIN_id_b43bd763_fk_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_user` */

insert  into `app_user`(`id`,`username`,`email`,`LOGIN_id`,`phone`,`pincode`,`place`,`post`) values 
(1,'f','h',3,'987654345','9987','ker','000');

/*Table structure for table `app_work` */

DROP TABLE IF EXISTS `app_work`;

CREATE TABLE `app_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `work_image` varchar(200) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` varchar(15) NOT NULL,
  `WORKER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_work_WORKER_id_689e62d2_fk_app_worker_id` (`WORKER_id`),
  CONSTRAINT `app_work_WORKER_id_689e62d2_fk_app_worker_id` FOREIGN KEY (`WORKER_id`) REFERENCES `app_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_work` */

insert  into `app_work`(`id`,`work_image`,`details`,`date`,`WORKER_id`) values 
(2,'/static/images/20240318-114834.jpg','mangalore22@gmail.com','2024-03-28',1),
(4,'/static/images/20240318-114834.jpg','thalhath','2024-03-19',1);

/*Table structure for table `app_worker` */

DROP TABLE IF EXISTS `app_worker`;

CREATE TABLE `app_worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `experience` varchar(150) NOT NULL,
  `age` varchar(5) NOT NULL,
  `IDproof` varchar(15) NOT NULL,
  `lattitude` varchar(20) NOT NULL,
  `longitude` varchar(20) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_worker_LOGIN_id_6c9a14e5_fk_app_login_id` (`LOGIN_id`),
  CONSTRAINT `app_worker_LOGIN_id_6c9a14e5_fk_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `app_worker` */

insert  into `app_worker`(`id`,`name`,`email`,`phone`,`experience`,`age`,`IDproof`,`lattitude`,`longitude`,`LOGIN_id`) values 
(1,'thalu','tahlu@gmail.com','7554555651','5years','27','876654','hfh','rd',2);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can add permission',2,'add_permission'),
(5,'Can change permission',2,'change_permission'),
(6,'Can delete permission',2,'delete_permission'),
(7,'Can add group',3,'add_group'),
(8,'Can change group',3,'change_group'),
(9,'Can delete group',3,'delete_group'),
(10,'Can add user',4,'add_user'),
(11,'Can change user',4,'change_user'),
(12,'Can delete user',4,'delete_user'),
(13,'Can add content type',5,'add_contenttype'),
(14,'Can change content type',5,'change_contenttype'),
(15,'Can delete content type',5,'delete_contenttype'),
(16,'Can add session',6,'add_session'),
(17,'Can change session',6,'change_session'),
(18,'Can delete session',6,'delete_session'),
(19,'Can add booking',7,'add_booking'),
(20,'Can change booking',7,'change_booking'),
(21,'Can delete booking',7,'delete_booking'),
(22,'Can add bookingub',8,'add_bookingub'),
(23,'Can change bookingub',8,'change_bookingub'),
(24,'Can delete bookingub',8,'delete_bookingub'),
(25,'Can add category',9,'add_category'),
(26,'Can change category',9,'change_category'),
(27,'Can delete category',9,'delete_category'),
(28,'Can add chat',10,'add_chat'),
(29,'Can change chat',10,'change_chat'),
(30,'Can delete chat',10,'delete_chat'),
(31,'Can add feedback',11,'add_feedback'),
(32,'Can change feedback',11,'change_feedback'),
(33,'Can delete feedback',11,'delete_feedback'),
(34,'Can add login',12,'add_login'),
(35,'Can change login',12,'change_login'),
(36,'Can delete login',12,'delete_login'),
(37,'Can add rating',13,'add_rating'),
(38,'Can change rating',13,'change_rating'),
(39,'Can delete rating',13,'delete_rating'),
(40,'Can add service',14,'add_service'),
(41,'Can change service',14,'change_service'),
(42,'Can delete service',14,'delete_service'),
(43,'Can add user',15,'add_user'),
(44,'Can change user',15,'change_user'),
(45,'Can delete user',15,'delete_user'),
(46,'Can add work',16,'add_work'),
(47,'Can change work',16,'change_work'),
(48,'Can delete work',16,'delete_work'),
(49,'Can add worker',17,'add_worker'),
(50,'Can change worker',17,'change_worker'),
(51,'Can delete worker',17,'delete_worker'),
(52,'Can add bookingsub',8,'add_bookingsub'),
(53,'Can change bookingsub',8,'change_bookingsub'),
(54,'Can delete bookingsub',8,'delete_bookingsub');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'','0000-00-00 00:00:00.000000',0,'','','f','vc',0,0,'0000-00-00 00:00:00.000000');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(7,'app','booking'),
(8,'app','bookingsub'),
(9,'app','category'),
(10,'app','chat'),
(11,'app','feedback'),
(12,'app','login'),
(13,'app','rating'),
(14,'app','service'),
(15,'app','user'),
(16,'app','work'),
(17,'app','worker'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-01 10:24:19.127103'),
(2,'auth','0001_initial','2024-02-01 10:24:20.319958'),
(3,'admin','0001_initial','2024-02-01 10:24:20.540039'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-01 10:24:20.560707'),
(5,'app','0001_initial','2024-02-01 10:24:22.458439'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-01 10:24:22.563605'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-01 10:24:22.663771'),
(8,'auth','0003_alter_user_email_max_length','2024-02-01 10:24:22.694468'),
(9,'auth','0004_alter_user_username_opts','2024-02-01 10:24:22.710089'),
(10,'auth','0005_alter_user_last_login_null','2024-02-01 10:24:22.788666'),
(11,'auth','0006_require_contenttypes_0002','2024-02-01 10:24:22.788666'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-01 10:24:22.804288'),
(13,'auth','0008_alter_user_username_max_length','2024-02-01 10:24:22.835528'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-01 10:24:22.864189'),
(15,'sessions','0001_initial','2024-02-01 10:24:22.914066'),
(16,'app','0002_auto_20240205_1610','2024-02-05 10:40:34.115010'),
(17,'app','0003_auto_20240318_1045','2024-03-18 05:15:22.330718'),
(18,'app','0004_auto_20240318_1150','2024-03-18 06:20:56.455872'),
(19,'app','0005_booking_paymentdate','2024-03-26 09:02:12.037289');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('papmzey3qjfu5gq542ezl0d0ez0iqz15','NGZhZTkwNzA3NmFlMDFhNjRlOTUwZTNjZjYwMjQ1YTM2NGU1NGJjZjp7ImxpZCI6MX0=','2024-04-16 09:13:26.678780');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
