-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 03-11-2024 a las 22:50:10
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
CREATE DATABASE IF NOT EXISTS `casa_acme` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci;
USE `casa_acme`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caja`
--

DROP TABLE IF EXISTS `caja`;
CREATE TABLE IF NOT EXISTS `caja` (
  `cod_caja` int NOT NULL AUTO_INCREMENT,
  `empleado_cod_empleado` int NOT NULL,
  `estado` int DEFAULT NULL,
  PRIMARY KEY (`cod_caja`),
  KEY `fk_caja_empleado1_idx` (`empleado_cod_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `cod_empleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `apellido_paterno` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `apellido_materno` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `sexo` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `telefono` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `fecha_nac` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `correo` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `clave` varchar(200) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `cod_tipo_empleado` int NOT NULL,
  PRIMARY KEY (`cod_empleado`),
  KEY `fk_empleado_tipo_empleado1_idx` (`cod_tipo_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moneda`
--

DROP TABLE IF EXISTS `moneda`;
CREATE TABLE IF NOT EXISTS `moneda` (
  `cod_moneda` int NOT NULL AUTO_INCREMENT,
  `nom_moneda` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `tipo_cambio` decimal(10,2) DEFAULT NULL,
  `estado` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`cod_moneda`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `moneda`
--

INSERT INTO `moneda` (`cod_moneda`, `nom_moneda`, `tipo_cambio`, `estado`) VALUES
(1, 'USD', 870.00, '1'),
(2, 'EUR', 950.00, '1'),
(3, 'GBP', 1100.00, '1'),
(4, 'JPY', 8.00, '1'),
(5, 'AUD', 650.00, '1'),
(6, 'CAD', 660.00, '1'),
(7, 'CHF', 940.00, '1'),
(8, 'CNY', 130.00, '1'),
(9, 'MXN', 45.00, '1'),
(10, 'BRL', 170.00, '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `saldo_caja`
--

DROP TABLE IF EXISTS `saldo_caja`;
CREATE TABLE IF NOT EXISTS `saldo_caja` (
  `cod_caja` int NOT NULL,
  `cod_moneda` int NOT NULL,
  `disponibilidad` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`cod_caja`,`cod_moneda`),
  KEY `fk_caja_has_moneda_moneda1_idx` (`cod_moneda`),
  KEY `fk_caja_has_moneda_caja_idx` (`cod_caja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado`
--

DROP TABLE IF EXISTS `tipo_empleado`;
CREATE TABLE IF NOT EXISTS `tipo_empleado` (
  `cod_tipo_empleado` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(45) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`cod_tipo_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
CREATE TABLE IF NOT EXISTS `transaccion` (
  `cod_transaccion` int NOT NULL AUTO_INCREMENT,
  `cod_empleado` int NOT NULL,
  `cod_caja` int NOT NULL,
  `cod_moneda` int NOT NULL,
  `monto_transferido` decimal(15,2) DEFAULT NULL,
  `monto_recibido` decimal(15,2) DEFAULT NULL,
  `fecha_transaccion` datetime DEFAULT NULL,
  PRIMARY KEY (`cod_transaccion`),
  KEY `fk_transaccion_empleado1_idx` (`cod_empleado`),
  KEY `fk_transaccion_caja1_idx` (`cod_caja`),
  KEY `fk_transaccion_moneda1_idx` (`cod_moneda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `caja`
--
ALTER TABLE `caja`
  ADD CONSTRAINT `fk_caja_empleado1` FOREIGN KEY (`empleado_cod_empleado`) REFERENCES `empleado` (`cod_empleado`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `fk_empleado_tipo_empleado1` FOREIGN KEY (`cod_tipo_empleado`) REFERENCES `tipo_empleado` (`cod_tipo_empleado`);

--
-- Filtros para la tabla `saldo_caja`
--
ALTER TABLE `saldo_caja`
  ADD CONSTRAINT `fk_caja_has_moneda_caja` FOREIGN KEY (`cod_caja`) REFERENCES `caja` (`cod_caja`),
  ADD CONSTRAINT `fk_caja_has_moneda_moneda1` FOREIGN KEY (`cod_moneda`) REFERENCES `moneda` (`cod_moneda`);

--
-- Filtros para la tabla `transaccion`
--
ALTER TABLE `transaccion`
  ADD CONSTRAINT `fk_transaccion_caja1` FOREIGN KEY (`cod_caja`) REFERENCES `caja` (`cod_caja`),
  ADD CONSTRAINT `fk_transaccion_empleado1` FOREIGN KEY (`cod_empleado`) REFERENCES `empleado` (`cod_empleado`),
  ADD CONSTRAINT `fk_transaccion_moneda1` FOREIGN KEY (`cod_moneda`) REFERENCES `moneda` (`cod_moneda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
