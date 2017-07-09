--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
CREATE TABLE `device` (
  `id` bigint(32) NOT NULL,
  `snmp_comm` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vendor` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `os` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `os_ver` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_discover` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `interface_groups`
--
DROP TABLE IF EXISTS `device_port`;
DROP TABLE IF EXISTS `interface_groups`;
CREATE TABLE `interface_groups` (
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `device_port`
--

DROP TABLE IF EXISTS `device_port`;
CREATE TABLE `device_port` (
  `id` bigint(32) NOT NULL,
  `port` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alias` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prefix_len` tinyint(4) DEFAULT NULL,
  `descr` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mac` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vlan` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `present` tinyint(1) DEFAULT '1',
  `igroup` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`,`port`),
  KEY `igroup` (`igroup`),
  CONSTRAINT `device_port_ibfk_1` FOREIGN KEY (`igroup`) REFERENCES `interface_groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `service_requests`
--

DROP TABLE IF EXISTS `service_requests`;
CREATE TABLE `service_requests` (
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `creation_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `device` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `task_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customer` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `result` longtext COLLATE utf8mb4_unicode_ci,
  `port` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `service` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `resources` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `customer` (`customer`),
  KEY `service` (`service`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
CREATE TABLE `services` (
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `interface_group` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_role` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `config_snippet` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `fields` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `activate_snippet` text COLLATE utf8mb4_unicode_ci,
  `deactivate_snippet` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `supernets`
--

DROP TABLE IF EXISTS `supernets`;
CREATE TABLE `supernets` (
  `id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `network` bigint(32) NOT NULL,
  `prefix` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `network` (`network`,`prefix`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
