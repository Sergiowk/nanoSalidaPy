DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;


DROP TABLE IF EXISTS `Drivers`;
CREATE TABLE `Drivers` (
	`Name` varchar(100) NOT NULL,
	`Number` tinyint,
	`Nationality` varchar(50) NOT NULL,
	`DOB` datetime
);