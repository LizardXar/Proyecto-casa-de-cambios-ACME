-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 16-12-2024 a las 03:08:24
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `caja`
--

INSERT INTO `caja` (`cod_caja`, `empleado_cod_empleado`, `estado`) VALUES
(1, 4, 1),
(2, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `cod_empleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `apellido_paterno` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `apellido_materno` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `sexo` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `telefono` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `fecha_nac` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `correo` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `clave` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `cod_tipo_empleado` int NOT NULL,
  PRIMARY KEY (`cod_empleado`),
  KEY `fk_empleado_tipo_empleado1_idx` (`cod_tipo_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`cod_empleado`, `nombre`, `apellido_paterno`, `apellido_materno`, `sexo`, `telefono`, `fecha_nac`, `correo`, `clave`, `cod_tipo_empleado`) VALUES
(1, 'Juan', 'Perez', 'Pereira', 'Hombre', '+56912345678', '29/12/1999', 'cajero1', '1234', 4),
(2, 'Jose', 'Rojas', 'Araos', 'Hombre', '+56914253647', '29/12/1997', 'gerente', '1234', 2),
(3, 'Ramiro', 'Hernandes', 'Salvo', 'Hombre', '+56988884444', '10/09/2002', 'ejecutivo', '1234', 1),
(4, 'Pedro', 'Paz', 'Conejero', 'Hombre', '+56912349876', '10/10/1995', 'cajero2', '1234', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moneda`
--

DROP TABLE IF EXISTS `moneda`;
CREATE TABLE IF NOT EXISTS `moneda` (
  `cod_moneda` int NOT NULL AUTO_INCREMENT,
  `nom_moneda` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `tipo_cambio` decimal(10,2) DEFAULT NULL,
  `estado` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`cod_moneda`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `moneda`
--

INSERT INTO `moneda` (`cod_moneda`, `nom_moneda`, `tipo_cambio`, `estado`) VALUES
(1, 'USD', 870.00, '1'),
(2, 'EUR', 940.00, '1'),
(3, 'GBP', 900.00, '1'),
(4, 'JPY', 400.00, '1'),
(5, 'AUD', 650.00, '1'),
(6, 'CAD', 660.00, '1'),
(7, 'CHF', 940.00, '2'),
(8, 'CNY', 130.00, '1'),
(9, 'MXN', 200.00, '2'),
(10, 'BRL', 90.00, '2'),
(11, 'CLP', 1.00, '2');

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

--
-- Volcado de datos para la tabla `saldo_caja`
--

INSERT INTO `saldo_caja` (`cod_caja`, `cod_moneda`, `disponibilidad`) VALUES
(1, 1, 9658.10),
(1, 2, 204.00),
(1, 5, 250.00),
(1, 10, 400.00),
(1, 11, 300.00),
(2, 1, 509.00),
(2, 3, 550.00),
(2, 11, 9000.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado`
--

DROP TABLE IF EXISTS `tipo_empleado`;
CREATE TABLE IF NOT EXISTS `tipo_empleado` (
  `cod_tipo_empleado` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`cod_tipo_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `tipo_empleado`
--

INSERT INTO `tipo_empleado` (`cod_tipo_empleado`, `rol`) VALUES
(1, 'Gerente'),
(2, 'Ejecutivo'),
(3, 'Administrador'),
(4, 'Cajero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
CREATE TABLE IF NOT EXISTS `transaccion` (
  `cod_transaccion` int NOT NULL AUTO_INCREMENT,
  `cod_caja` int NOT NULL,
  `cod_moneda` int NOT NULL,
  `monto_transferido` decimal(15,2) DEFAULT NULL,
  `fecha_transaccion` datetime DEFAULT NULL,
  PRIMARY KEY (`cod_transaccion`),
  KEY `fk_transaccion_caja1_idx` (`cod_caja`),
  KEY `fk_transaccion_moneda1_idx` (`cod_moneda`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `transaccion`
--

INSERT INTO `transaccion` (`cod_transaccion`, `cod_caja`, `cod_moneda`, `monto_transferido`, `fecha_transaccion`) VALUES
(1, 1, 1, 20.00, '2024-12-11 13:01:55'),
(2, 1, 5, 30.00, '2024-12-12 13:01:55'),
(3, 1, 1, 30.00, '2024-12-12 13:25:34'),
(4, 1, 1, 50.00, '2024-12-31 13:02:34'),
(5, 1, 1, 400.00, '2024-12-14 20:30:48'),
(6, 1, 1, 20.00, '2024-12-14 20:56:25'),
(7, 1, 2, 200.00, '2024-12-14 21:01:52'),
(8, 1, 2, 20000.00, '2024-12-14 21:02:01'),
(9, 1, 1, 200.00, '2024-12-14 21:08:12'),
(10, 1, 1, 1.00, '2024-12-14 21:12:39'),
(11, 1, 1, 10.00, '2024-12-14 21:12:52'),
(12, 1, 1, 100.00, '2024-12-14 21:13:11'),
(13, 1, 1, 40000.00, '2024-12-14 21:13:41'),
(14, 2, 2, 2.00, '2024-12-14 22:03:49'),
(15, 1, 6, 10.00, '2024-12-14 22:12:01'),
(16, 1, 1, 100.00, '2024-12-14 22:14:09'),
(17, 2, 4, 100.00, '2024-12-14 22:35:07'),
(18, 1, 1, 200.00, '2024-12-15 17:11:00'),
(19, 1, 1, 9000.00, '2024-12-15 17:11:08'),
(20, 1, 1, 0.00, '2024-12-15 17:11:13'),
(21, 1, 1, 2.01, '2024-12-15 18:04:00'),
(22, 1, 1, 99.99, '2024-12-15 18:06:19'),
(23, 2, 4, 40.00, '2024-12-15 22:36:31'),
(24, 2, 4, 2.00, '2024-12-15 22:36:43'),
(25, 2, 1, 400.00, '2024-12-15 22:38:57'),
(26, 2, 1, 9.00, '2024-12-15 22:39:00'),
(27, 1, 2, 4.00, '2024-12-15 22:40:47'),
(28, 1, 4, 4.00, '2024-12-15 23:05:21'),
(29, 1, 1, 10.00, '2024-12-15 23:44:47');

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
  ADD CONSTRAINT `fk_transaccion_moneda1` FOREIGN KEY (`cod_moneda`) REFERENCES `moneda` (`cod_moneda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
