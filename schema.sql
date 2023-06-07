DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;


DROP TABLE IF EXISTS `drivers`;
CREATE TABLE `drivers` (
	`name` varchar(100) NOT NULL,
	`number` tinyint,
	`nationality` varchar(50) NOT NULL,
	`dob` datetime
);