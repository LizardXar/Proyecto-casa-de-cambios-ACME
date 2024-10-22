-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 21-10-2024 a las 18:41:59
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `casa_acme`
--
CREATE DATABASE IF NOT EXISTS `casa_acme` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE `casa_acme`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `monedas`
--

DROP TABLE IF EXISTS `monedas`;
CREATE TABLE IF NOT EXISTS `monedas` (
  `cod_moneda` int NOT NULL AUTO_INCREMENT,
  `nom_moneda` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  `tipo_cambio` decimal(10,2) NOT NULL,
  `estado` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`cod_moneda`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `monedas`
--

INSERT INTO `monedas` (`cod_moneda`, `nom_moneda`, `tipo_cambio`, `estado`) VALUES
(5, 'YENES', 6.00, 1),
(4, 'WAN', 130.00, 1),
(3, 'ARS', 5.00, 1),
(2, 'DOLAR', 850.00, 2),
(1, 'EURO', 870.00, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
