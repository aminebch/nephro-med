-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 20 juin 2023 à 00:31
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `connexionbddappli`
--

-- --------------------------------------------------------

--
-- Structure de la table `antecedentchirurgicaux`
--

DROP TABLE IF EXISTS `antecedentchirurgicaux`;
CREATE TABLE IF NOT EXISTS `antecedentchirurgicaux` (
  `id_antchir` int NOT NULL AUTO_INCREMENT,
  `id_consultation` int NOT NULL,
  `nom_chirurgie` varchar(255) DEFAULT NULL,
  `date_debut` date DEFAULT NULL,
  `lieu` varchar(255) DEFAULT NULL,
  `remarque` text,
  PRIMARY KEY (`id_antchir`),
  KEY `fk_consultation` (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `antecedentchirurgicaux`
--

INSERT INTO `antecedentchirurgicaux` (`id_antchir`, `id_consultation`, `nom_chirurgie`, `date_debut`, `lieu`, `remarque`) VALUES
(1, 105, 'aaaa', '2023-06-11', 'oran', 'aaa'),
(2, 105, 'Inter', '2023-06-11', 'CHU', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `antecedentfamiliaux`
--

DROP TABLE IF EXISTS `antecedentfamiliaux`;
CREATE TABLE IF NOT EXISTS `antecedentfamiliaux` (
  `id_antfam` int NOT NULL AUTO_INCREMENT,
  `id_consultation` int DEFAULT NULL,
  `nom_maladie` varchar(255) DEFAULT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `remarque` text,
  PRIMARY KEY (`id_antfam`),
  KEY `fk2_consultation` (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `antecedentfamiliaux`
--

INSERT INTO `antecedentfamiliaux` (`id_antfam`, `id_consultation`, `nom_maladie`, `date_debut`, `date_fin`, `remarque`) VALUES
(1, 105, '', '2023-06-11', '2023-06-11', 'aaaa');

-- --------------------------------------------------------

--
-- Structure de la table `antecedentmedicaux`
--

DROP TABLE IF EXISTS `antecedentmedicaux`;
CREATE TABLE IF NOT EXISTS `antecedentmedicaux` (
  `id_antmed` int NOT NULL AUTO_INCREMENT,
  `id_consultation` int NOT NULL,
  `nom_maladie` varchar(255) DEFAULT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `remarque` text,
  PRIMARY KEY (`id_antmed`),
  KEY `fk1_consultation` (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `antecedentmedicaux`
--

INSERT INTO `antecedentmedicaux` (`id_antmed`, `id_consultation`, `nom_maladie`, `date_debut`, `date_fin`, `remarque`) VALUES
(1, 105, 'diabete', '2023-06-11', '2023-06-11', 'lakal'),
(2, 105, 'hypertension', '2023-06-15', '2023-06-15', 'rien');

-- --------------------------------------------------------

--
-- Structure de la table `atc`
--

DROP TABLE IF EXISTS `atc`;
CREATE TABLE IF NOT EXISTS `atc` (
  `id_atc` int NOT NULL AUTO_INCREMENT,
  `code_atc` varchar(255) DEFAULT NULL,
  `atc_description` text,
  PRIMARY KEY (`id_atc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `bilan`
--

DROP TABLE IF EXISTS `bilan`;
CREATE TABLE IF NOT EXISTS `bilan` (
  `id_bilan` int NOT NULL AUTO_INCREMENT,
  `id_consultation` int NOT NULL,
  `date_bilan` date NOT NULL,
  `resultat` text,
  `conclusion` text,
  `remarque` text,
  PRIMARY KEY (`id_bilan`),
  KEY `id_consultation` (`id_consultation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `consultation`
--

DROP TABLE IF EXISTS `consultation`;
CREATE TABLE IF NOT EXISTS `consultation` (
  `id_consultation` int NOT NULL AUTO_INCREMENT,
  `id_patient` int NOT NULL,
  `id_medecin` int NOT NULL,
  `date_consultation` date NOT NULL,
  `heure_consultation` time NOT NULL,
  `remarques` text,
  PRIMARY KEY (`id_consultation`),
  KEY `id_patient` (`id_patient`),
  KEY `id_medecin` (`id_medecin`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `consultation`
--

INSERT INTO `consultation` (`id_consultation`, `id_patient`, `id_medecin`, `date_consultation`, `heure_consultation`, `remarques`) VALUES
(44, 4, 36, '2023-06-10', '22:06:14', 'llll'),
(45, 8, 36, '2023-06-10', '22:06:42', 'aaaa'),
(46, 8, 37, '2023-06-10', '22:07:06', 'aaaaa'),
(47, 12, 36, '2023-06-11', '09:35:25', 'jjjjjjjjjhhh'),
(48, 14, 36, '2023-06-11', '10:16:35', 'qqqqqq'),
(49, 14, 36, '2023-06-11', '10:16:49', 'ppppppp'),
(50, 3, 36, '2023-06-11', '12:20:59', 'pzpzpzp'),
(51, 5, 36, '2023-06-11', '18:57:45', 'mimi'),
(52, 3, 36, '2023-06-11', '22:45:55', 'aaaaaaaa'),
(53, 7, 36, '2023-06-11', '22:46:56', 'aaaaaa'),
(54, 5, 36, '2023-06-11', '22:47:51', 'aapapa'),
(55, 4, 36, '2023-06-11', '22:49:23', 'qqqqqqqqqqqq'),
(56, 4, 37, '2023-06-11', '22:53:21', 'aaaaaaaaaaa'),
(57, 4, 36, '2023-06-11', '22:55:15', 'aaaaa'),
(58, 6, 36, '2023-06-11', '22:56:16', 'aaa'),
(59, 4, 36, '2023-06-11', '23:05:05', 'qqqqqqqq'),
(60, 6, 36, '2023-06-11', '23:10:34', 'qlqkqlq'),
(61, 5, 36, '2023-06-11', '23:13:07', 'aaaaaaamaaaaa'),
(62, 5, 36, '2023-06-11', '23:22:16', 'maa'),
(63, 4, 36, '2023-06-11', '23:23:54', 'aaa'),
(64, 5, 36, '2023-06-11', '23:26:21', 'mamamma'),
(65, 5, 36, '2023-06-11', '23:27:26', 'aaa'),
(66, 6, 36, '2023-06-11', '23:28:40', 'aaaa'),
(67, 6, 36, '2023-06-11', '23:30:11', 'lalala'),
(68, 10, 36, '2023-06-11', '23:30:56', 'lkll'),
(69, 6, 36, '2023-06-11', '23:32:42', 'llll'),
(70, 4, 36, '2023-06-11', '23:59:08', 'qllqmlqmqm'),
(71, 5, 36, '2023-06-12', '00:01:00', 'aaa'),
(72, 4, 36, '2023-06-12', '00:04:32', 'kakka'),
(73, 4, 36, '2023-06-12', '00:21:32', 'aaa'),
(74, 4, 36, '2023-06-12', '00:22:45', 'kakak'),
(75, 5, 36, '2023-06-12', '02:16:53', '444'),
(76, 6, 36, '2023-06-12', '02:21:19', 'aaa'),
(77, 5, 36, '2023-06-12', '02:23:33', 'qqqq'),
(78, 5, 36, '2023-06-12', '02:29:43', 'aaa'),
(79, 6, 36, '2023-06-12', '02:31:14', 'ppppppppppp'),
(80, 6, 36, '2023-06-12', '02:48:29', 'aaa'),
(81, 6, 36, '2023-06-12', '22:40:55', 'rien'),
(82, 4, 36, '2023-06-12', '22:48:57', 'rien'),
(83, 5, 36, '2023-06-12', '22:49:35', '20'),
(84, 7, 36, '2023-06-12', '22:50:31', 'rien de spéciale'),
(85, 5, 36, '2023-06-12', '22:51:39', 'rien'),
(86, 5, 36, '2023-06-12', '22:52:18', 'rien'),
(87, 5, 36, '2023-06-12', '22:59:15', 'rien'),
(88, 4, 37, '2023-06-12', '23:04:11', 'rien'),
(89, 6, 36, '2023-06-13', '01:10:04', 'rien'),
(90, 45, 36, '2023-06-13', '18:28:23', 'rien de spécial'),
(91, 45, 36, '2023-06-14', '02:18:14', 'probleme respiratoire'),
(92, 45, 36, '2023-06-14', '03:16:25', 'manque de someil'),
(93, 49, 36, '2023-06-14', '13:23:41', 'rien de spéciale'),
(94, 45, 36, '2023-06-14', '13:24:42', 'mmama'),
(95, 45, 36, '2023-06-14', '13:54:15', 'rien'),
(96, 45, 36, '2023-06-14', '21:18:26', 'malade'),
(97, 45, 36, '2023-06-14', '21:26:39', 'rien'),
(98, 45, 36, '2023-06-14', '21:37:32', 'rien'),
(99, 45, 36, '2023-06-14', '21:38:22', 'rien'),
(100, 45, 36, '2023-06-14', '21:54:07', 'rien'),
(101, 45, 36, '2023-06-14', '21:55:21', 'rien'),
(102, 45, 36, '2023-06-14', '23:06:48', 'rineee'),
(103, 45, 36, '2023-06-14', '23:08:26', 'rieee'),
(104, 49, 36, '2023-06-15', '00:15:21', 'rien'),
(105, 50, 36, '2023-06-15', '03:08:13', 'rien'),
(106, 51, 36, '2023-06-15', '13:04:35', 'rien'),
(107, 51, 36, '2023-06-16', '18:52:02', 'rien');

-- --------------------------------------------------------

--
-- Structure de la table `detail_bilan`
--

DROP TABLE IF EXISTS `detail_bilan`;
CREATE TABLE IF NOT EXISTS `detail_bilan` (
  `id_detail_bilan` int NOT NULL AUTO_INCREMENT,
  `id_bilan` int NOT NULL,
  `id_parametre` int NOT NULL,
  `valeur` float DEFAULT NULL,
  PRIMARY KEY (`id_detail_bilan`),
  KEY `id_bilan` (`id_bilan`),
  KEY `id_parametre` (`id_parametre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `diagnostique`
--

DROP TABLE IF EXISTS `diagnostique`;
CREATE TABLE IF NOT EXISTS `diagnostique` (
  `id_diagnostique` int NOT NULL AUTO_INCREMENT,
  `nom_diagnostique` varchar(255) NOT NULL,
  `abreviation` varchar(50) DEFAULT NULL,
  `description` text,
  `date_diagnostique` date NOT NULL,
  `id_consultation` int NOT NULL,
  PRIMARY KEY (`id_diagnostique`),
  KEY `id_consultation` (`id_consultation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `entreprise`
--

DROP TABLE IF EXISTS `entreprise`;
CREATE TABLE IF NOT EXISTS `entreprise` (
  `id_ent` int NOT NULL,
  `nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `examen_clinique`
--

DROP TABLE IF EXISTS `examen_clinique`;
CREATE TABLE IF NOT EXISTS `examen_clinique` (
  `id_examen` int NOT NULL AUTO_INCREMENT,
  `id_nom_examen` int NOT NULL,
  `description` text,
  `date_examen` date DEFAULT NULL,
  `resultat` text,
  `id_consultation` int NOT NULL,
  PRIMARY KEY (`id_examen`),
  KEY `fk_examen_clinique` (`id_consultation`),
  KEY `fk1_examen_clinique` (`id_nom_examen`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `examen_clinique`
--

INSERT INTO `examen_clinique` (`id_examen`, `id_nom_examen`, `description`, `date_examen`, `resultat`, `id_consultation`) VALUES
(1, 7, 'kkk', '2023-06-12', 'lll', 79),
(2, 8, '2', '2023-06-15', 'neg', 105);

-- --------------------------------------------------------

--
-- Structure de la table `grade`
--

DROP TABLE IF EXISTS `grade`;
CREATE TABLE IF NOT EXISTS `grade` (
  `id_grade` int NOT NULL AUTO_INCREMENT,
  `nom_grade` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_grade`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `grade`
--

INSERT INTO `grade` (`id_grade`, `nom_grade`, `description`) VALUES
(1, 'résident(e)', NULL),
(2, 'médecin généraliste', NULL),
(3, 'médecin spécialiste', NULL),
(4, 'maître assistant(e)', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `gravite_sympthome`
--

DROP TABLE IF EXISTS `gravite_sympthome`;
CREATE TABLE IF NOT EXISTS `gravite_sympthome` (
  `id_gravite_sympthome` int NOT NULL AUTO_INCREMENT,
  `nom_gravite_sympthome` varchar(100) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_gravite_sympthome`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `gravite_sympthome`
--

INSERT INTO `gravite_sympthome` (`id_gravite_sympthome`, `nom_gravite_sympthome`, `description`) VALUES
(1, 'Légère', 'Le symptôme est présent mais n\'entraîne qu\'une gêne mineure et a peu d\'impact sur les activités quotidiennes.'),
(2, 'Modérée', 'Le symptôme est perceptible et peut causer une certaine gêne ou une perturbation modérée des activités quotidiennes.'),
(3, 'Sévère', 'Le symptôme est intense, provoque une gêne significative et interfère avec les activités normales. Il peut nécessiter une attention médicale immédiate.'),
(4, 'Critique', 'Le symptôme est extrêmement grave, mettant la vie en danger ou entraînant une détérioration grave de l état de santé. Il nécessite une intervention médicale urgence.');

-- --------------------------------------------------------

--
-- Structure de la table `habitudevie`
--

DROP TABLE IF EXISTS `habitudevie`;
CREATE TABLE IF NOT EXISTS `habitudevie` (
  `id_habitude` int NOT NULL AUTO_INCREMENT,
  `id_consultation` int NOT NULL,
  `id_option_habitude` int DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id_habitude`),
  KEY `fk3_consultation` (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `habitudevie`
--

INSERT INTO `habitudevie` (`id_habitude`, `id_consultation`, `id_option_habitude`, `description`) VALUES
(1, 70, 1, 'qq'),
(2, 70, 3, 'qq'),
(3, 71, 1, ''),
(4, 71, 3, ''),
(5, 71, 1, ''),
(6, 71, 3, ''),
(7, 71, 2, '');

-- --------------------------------------------------------

--
-- Structure de la table `interaction_entre_medicaments`
--

DROP TABLE IF EXISTS `interaction_entre_medicaments`;
CREATE TABLE IF NOT EXISTS `interaction_entre_medicaments` (
  `id_interaction` int NOT NULL AUTO_INCREMENT,
  `médicament1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `catégorie1` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `médicament2` varchar(25) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `catégorie2` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `niveau` varchar(7) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id_interaction`)
) ENGINE=MyISAM AUTO_INCREMENT=264 DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `interaction_entre_medicaments`
--

INSERT INTO `interaction_entre_medicaments` (`id_interaction`, `médicament1`, `catégorie1`, `médicament2`, `catégorie2`, `niveau`) VALUES
(1, ' CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(2, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'METHYLPREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(3, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'BUDESONIDE', 'CORTICOÏDES ', 'modéré '),
(4, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(5, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'IBUPROFENE ', 'AINS ', 'modéré '),
(6, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'FLURBIPROFENE ', 'AINS ', 'modéré '),
(7, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACIDE TIAPROFENIQUE ', 'AINS ', 'modéré '),
(8, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MELOXICAM ', 'AINS ', 'modéré '),
(9, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACIDE NIFLUMIQUE ', 'AINS ', 'modéré '),
(10, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ALMINOPROFENE', 'AINS ', 'modéré '),
(11, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CELECOXIB', 'AINS ', 'modéré '),
(12, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ETORICOXIB', 'AINS ', 'modéré '),
(13, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'KETOPROFENE', 'AINS ', 'modéré '),
(14, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PIROXICAM', 'AINS ', 'modéré '),
(15, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'INDOMETACINE ', 'AINS ', 'modéré '),
(16, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACIDE MEFENAMIQUE', 'AINS ', 'modéré '),
(17, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SULINDAC', 'AINS ', 'modéré '),
(18, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'DICLOFENAC ', 'AINS ', 'modéré '),
(19, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AMLODIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(20, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'LERCANIDIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(21, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'NICARDIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(22, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'DILTIAZEM ', 'ANTIHYPERTENSEURS ', 'modéré '),
(23, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ALISKIREN   ', 'ANTIHYPERTENSEURS ', 'majeur '),
(24, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'FUROSEMIDE  ', 'DIURETIQUES', 'modéré '),
(25, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SPIRONOLACTONE ', 'DIURETIQUES', 'modéré '),
(26, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'INDAPAMIDE', 'DIURETIQUES', 'modéré '),
(27, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACETAZOLAMIDE', 'DIURETIQUES', 'modéré '),
(28, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'HEPARINES (HNF/HBPM) ', 'HBPM', 'modéré '),
(29, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'METRONIDAZOLE ', 'ANTIFONGIQUES ', 'modéré '),
(30, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'VORICONAZOLE', 'ANTIFONGIQUES ', 'majeur '),
(31, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'KETOCONAZOLE (PER OS) ', 'ANTIFONGIQUES ', 'majeur '),
(32, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'POSACONAZOLE', 'ANTIFONGIQUES ', 'majeur '),
(33, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ITRACONAZOLE', 'ANTIFONGIQUES ', 'modéré '),
(34, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'FLUCONAZOLE ', 'ANTIFONGIQUES ', 'modéré '),
(35, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MICONAZOLE', 'ANTIFONGIQUES ', 'modéré '),
(36, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AMPHOTERICINE B (IV)', 'ANTIFONGIQUES ', 'modéré '),
(37, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ROSUVASTATINE', 'HYPOLIPEMIANTS ', 'majeur '),
(38, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ATORVASTATINE', 'HYPOLIPEMIANTS ', 'majeur '),
(39, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'LOVASTATINE', 'HYPOLIPEMIANTS ', 'majeur '),
(40, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SIMVASTATINE', 'HYPOLIPEMIANTS ', 'majeur '),
(41, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PRAVASTATINE', 'HYPOLIPEMIANTS ', 'modéré '),
(42, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'FLUVASTATINE', 'HYPOLIPEMIANTS ', 'modéré '),
(43, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'OMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(44, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'LANSOPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(45, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ESOMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(46, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'RABEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(47, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AZATHIOPRINE', 'IMMUNOSUPPRESSEURS ', 'modéré '),
(48, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MYCOPHENOLATE MOFETIL ', 'IMMUNOSUPPRESSEURS ', 'modéré '),
(49, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SIROLIMUS     ', 'IMMUNOSUPPRESSEURS ', 'modéré '),
(50, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MÉTHOTREXATE    ', 'ANTI CANCEREUX ', 'modéré '),
(51, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CARBAMAZEPINE ', 'ANTIEPILEPTIQUE', 'majeur '),
(52, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PHENOBARBITAL', 'ANTIEPILEPTIQUE', 'modéré '),
(53, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PHENYTOINE', 'ANTIEPILEPTIQUE', 'modéré '),
(54, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'REPAGLINIDE ', 'ANTIDIABETIQUES ', 'majeur '),
(55, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AMIODARONE', 'ANTIARYTHMIQUES ', 'modéré'),
(56, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CIPROFLOXACINE ', 'ANTIBIOTIQUES', 'modéré '),
(57, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CEFTAZIDIME (C3G) ', 'ANTIBIOTIQUES', 'modéré '),
(58, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CEFTRIAXONE (C3G) ', 'ANTIBIOTIQUES', 'modéré '),
(59, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'GENTAMICINE', 'ANTIBIOTIQUES', 'modéré '),
(60, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AMIKACINE', 'ANTIBIOTIQUES', 'modéré '),
(61, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'NETILMICINE', 'ANTIBIOTIQUES', 'modéré '),
(62, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'STREPTOMYCINE ', 'ANTIBIOTIQUES', 'modéré '),
(63, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'VANCOMYCINE  ', 'ANTIBIOTIQUES', 'modéré '),
(64, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'TEICOPLANINE ', 'ANTIBIOTIQUES', 'modéré '),
(65, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AZITHROMYCINE  ', 'ANTIBIOTIQUES', 'modéré '),
(66, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ERYTHROMYCINE ', 'ANTIBIOTIQUES', 'majeur '),
(67, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'TELITHROMYCINE ', 'ANTIBIOTIQUES', 'majeur '),
(68, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CLARITHROMYCINE ', 'ANTIBIOTIQUES', 'majeur '),
(69, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'JOSAMYCINE  ', 'ANTIBIOTIQUES', 'modéré '),
(70, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'NORFLOXACINE  ', 'ANTIBIOTIQUES', 'modéré '),
(71, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PRISTINAMYCINE   ', 'ANTIBIOTIQUES', 'modéré '),
(72, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'COTRIMOXAZOLE ', 'ANTIBIOTIQUES', 'majeur '),
(73, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'COTRIMOXAZOLE (IV) ', 'ANTIBIOTIQUES', 'majeur '),
(74, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'IMIPENEME', 'ANTIBIOTIQUES', 'modéré '),
(75, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACICLOVIR', 'ANTIVIRAUX ', 'modéré '),
(76, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'VALGANCICLOVIR', 'ANTIVIRAUX ', 'modéré '),
(77, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'GANCICLOVIR ', 'ANTIVIRAUX ', 'modéré '),
(78, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ENTECAVIR', 'ANTIVIRAUX ', 'modéré '),
(79, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'INDINAVIR  ', 'ANTIVIRAUX ', 'majeur '),
(80, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'BOCEPREVIR   ', 'ANTIVIRAUX ', 'majeur '),
(81, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'TELEPREVIR   ', 'ANTIVIRAUX ', 'majeur '),
(82, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'EFAVIRENZ', 'ANTIVIRAUX ', 'modéré '),
(83, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'NEVIRAPINE', 'ANTIVIRAUX ', 'modéré '),
(84, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ACIDE URSODESOXYCHOLIQUE ', '', 'modéré '),
(85, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'AFATINIB   ', '', 'modéré '),
(86, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MELPHALAN  ', '', 'modéré '),
(87, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'ALLOPURINOL ', 'hypo uricemiant', 'modéré '),
(88, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'COLCHICINE ', '', 'majeur '),
(89, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'BOSENTAN ', '', 'modéré '),
(90, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'MESALAZINE (5-ASA)', '', 'modéré '),
(91, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SULFASALAZINE', '', 'majeur '),
(92, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'BROMOCRIPTINE', '', 'majeur '),
(93, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'TENOFOVIR', '', 'majeur '),
(94, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'LOPIRAMIDE', '', 'modéré '),
(95, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'SORAFENIB ', '', 'modéré '),
(96, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CORTICOIDES ', 'CORTICOÏDES ', 'modéré '),
(97, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ACICLOVIR', 'ANTIVIRAUX ', 'majeur '),
(98, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'AMPHOTERECINE B', '', 'modéré '),
(99, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CANDESARTAN (ATACAND)', 'ANTIHYPERTENSEURS ', 'modéré '),
(100, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'VALSARTAN  ', 'ANTIHYPERTENSEURS ', 'modéré '),
(101, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'INSULINE  ', 'ANTIDIABETIQUES ', 'modéré '),
(102, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'METFORMINE', 'ANTIDIABETIQUES ', 'modéré '),
(103, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CARBAMAZÉPINE', 'ANTIEPILEPTIQUE', 'majeur '),
(104, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PHÉNOBARBITAL', 'ANTIEPILEPTIQUE', 'majeur '),
(105, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CLONAZEPAM', 'ANTIEPILEPTIQUE', 'modéré '),
(106, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ETHOSUXIMIDE', '', 'modéré '),
(107, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'OXCARBAZÉPINE', 'ANTIEPILEPTIQUE', 'modéré '),
(108, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Flurbiprofène ', 'AINS ', 'modéré '),
(109, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Ibuprofène ', 'AINS ', 'modéré '),
(110, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Indométacine', 'AINS ', 'modéré '),
(111, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Kétoprofène', 'AINS ', 'modéré '),
(112, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Acide Mefénamique ', 'AINS ', 'modéré '),
(113, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Méloxicam ', 'AINS ', 'modéré '),
(114, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Naproxène ', 'AINS ', 'modéré '),
(115, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'RAMIPRIL ', 'ANTIHYPERTENSEURS ', 'modéré '),
(116, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'AMLODIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(117, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'NICARDIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(118, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'DILTIAZEM ', 'ANTIHYPERTENSEURS ', 'modéré '),
(119, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'VALGANCICLOVIR', 'ANTIVIRAUX ', 'modéré '),
(120, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'OMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'majeur '),
(121, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'BUDESONIDE', 'CORTICOÏDES ', 'modéré '),
(122, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'COLCHICINE  ', '', 'majeur '),
(123, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'AZATHIOPRINE', 'IMMUNOSUPPRESSEURS ', 'modéré '),
(124, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PHENYTOINE', 'ANTIEPILEPTIQUE', 'majeur '),
(125, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CARBAMAZEPINE ', 'ANTIEPILEPTIQUE', 'majeur '),
(126, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PHENOBARBITAL', 'ANTIEPILEPTIQUE', 'majeur '),
(127, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ATORVASTATINE', 'HYPOLIPEMIANTS ', 'modéré '),
(128, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'SIMVASTATINE', 'HYPOLIPEMIANTS ', 'modéré '),
(129, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'COTRIMOXAZOLE  ', 'ANTIBIOTIQUES ', 'modéré '),
(130, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CELECOXIB', 'AINS ', 'modéré '),
(131, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'DICLOFENAC ', 'AINS ', 'modéré '),
(132, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PIROXICAM', 'AINS ', 'modéré '),
(133, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ACIDE NIFLUMIQUE ', 'AINS ', 'modéré '),
(134, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'SULFASALAZINE', 'ANTI-INFLAMATOIRE', 'modéré '),
(135, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'MESALAZINE (5-ASA)', '', 'modéré '),
(136, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ENTECAVIR', 'ANTIVIRAUX ', 'modéré '),
(137, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'VORICONAZOLE', 'ANTIFONGIQUES ', 'majeur '),
(138, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'SORAFENIB ', '', 'modéré '),
(139, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(140, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'CALCIUM ', '', 'modéré '),
(141, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'GANCICLOVIR ', 'ANTIVIRAUX ', 'modéré '),
(142, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'COTRIMOXAZOLE  ', 'ANTIBIOTIQUES ', 'modéré '),
(143, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'OMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(144, 'FUROSEMIDE  ', 'DIURETIQUES', 'PREDNISONE', 'CORTICOÏDES ', 'modéré '),
(145, 'FUROSEMIDE  ', 'DIURETIQUES', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(146, 'FUROSEMIDE  ', 'DIURETIQUES', 'VANCOMYCINE  ', 'ANTIBIOTIQUES ', 'modéré '),
(147, 'PREDNISONE', 'CORTICOÏDES ', 'BISOPROLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(148, 'PREDNISONE', 'CORTICOÏDES ', 'METHYLDOPA', 'ANTIHYPERTENSEURS ', 'modéré '),
(149, 'PREDNISONE', 'CORTICOÏDES ', 'METHYLDOPA', 'ANTIHYPERTENSEURS ', 'modéré '),
(150, 'ATENOLOL ', 'ANTIHYPERTENSEURS ', 'CALCIUM ', '', 'modéré '),
(151, 'FUROSEMIDE  ', 'DIURETIQUES', 'INSULINE  ', 'ANTIDIABETIQUES ', 'modéré '),
(152, 'CIPROFLOXACINE ', 'ANTIBIOTIQUES ', 'INSULINE  ', 'ANTIDIABETIQUES ', 'majeur '),
(153, 'IRBESARTAN  ', 'ANTIHYPERTENSEURS ', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(154, 'LOSARTAN ', 'ANTIHYPERTENSEURS ', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(155, 'LOSARTAN ', 'ANTIHYPERTENSEURS ', 'SPIRONOLACTONE ', 'DIURETIQUES', 'modéré '),
(156, 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'SPIRONOLACTONE ', 'DIURETIQUES', 'mineur '),
(157, 'OMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'VORICONAZOLE', 'ANTIFONGIQUES ', 'modéré '),
(158, 'INSULINE  ', 'ANTIDIABETIQUES ', 'FUROSEMIDE', 'DIURETIQUES', 'modéré '),
(159, 'ESOMEPRAZOLE ', 'INHIBITEURS DE LA POMPE A PROTON', 'ATORVASTATINE', 'HYPOLIPEMIANTS ', 'modéré '),
(160, 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(161, 'ONDANSETRON ', 'ANTIHEMITIQUE ', 'VORICONAZOLE', 'ANTIFONGIQUES ', 'modéré '),
(162, 'FUROSEMIDE  ', 'DIURETIQUES', 'PREDNISOLONE', 'CORTICOÏDES ', 'mineur '),
(163, 'FUROSEMIDE  ', 'DIURETIQUES', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(164, 'INSULINE  ', 'ANTIDIABETIQUES ', 'PREDNISONE', 'CORTICOÏDES ', 'modéré '),
(165, 'INSULINE  ', 'ANTIDIABETIQUES ', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(166, 'METFORMINE', 'ANTIDIABETIQUES ', 'PREDNISOLONE', 'CORTICOÏDES ', 'modéré '),
(167, 'INSULINE  ', 'ANTIDIABETIQUES ', 'ACEBUTOLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(168, 'PREDNISONE', 'CORTICOÏDES ', 'NICARDIPINE ', 'ANTIHYPERTENSEURS ', 'modéré '),
(169, 'PREDNISOLONE', 'CORTICOÏDES ', 'BISOPROLOL', 'ANTIHYPERTENSEURS', 'modéré '),
(170, 'PREDNISONE', 'CORTICOÏDES ', 'ACEBUTOLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(171, 'PREDNISOLONE', 'CORTICOÏDES ', 'IRBESARTAN  ', 'ANTIHYPERTENSEURS ', 'modéré '),
(172, 'LEVODOPA', '', 'PERINDOPRIL ', '', 'modéré '),
(173, 'NICARDIPINE ', 'ANTIHYPERTENSEURS ', 'BISOPROLOL', 'ANTIHYPERTENSEURS', 'modéré '),
(174, 'PHYSIOTENS (MOXONIDINE) ', 'ANTIHYPERTENSEURS ', 'BISOPROLOL', 'ANTIHYPERTENSEURS', 'modéré '),
(175, 'LERCANIDIPINE ', 'ANTIHYPERTENSEURS ', 'BISOPROLOL', 'ANTIHYPERTENSEURS', 'modéré '),
(176, 'CHLORPROMAZINE ', '', 'LEVOFLOXACINE ', 'ANTIBIOTIQUES ', 'modéré '),
(177, 'VORICONAZOLE', 'ANTIFONGIQUES ', 'LEVOFLOXACINE ', 'ANTIBIOTIQUES ', 'modéré '),
(178, 'VANCOMYCINE  ', 'ANTIBIOTIQUES ', 'ACYCLOVIR ', 'ANTIVIRAUX ', 'modéré '),
(179, 'TENOFOVIR', '', 'ACYCLOVIR ', 'ANTIVIRAUX ', 'Majeur'),
(180, 'RAMIPRIL ', 'ANTIHYPERTENSEURS ', 'PREDNISONE', 'CORTICOÏDES ', 'modéré '),
(182, 'LOVENOX (ENOXAPARINE) ', 'HBPM', 'IRBESARTAN  ', 'ANTIHYPERTENSEURS ', 'modéré '),
(183, 'SULFATE FERREUX ', '', 'OMEPRAZOLE', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(184, 'BACTRIM ', 'ANTIBIOTIQUES ', 'ACIDE FOLIQUE ', '', 'modéré '),
(185, 'METFORMINE', 'ANTIDIABETIQUES ', 'INSULINE LISPRO', 'ANTIDIABETIQUES ', 'modéré '),
(186, 'GENTAMICINE', 'ANTIBIOTIQUES ', 'VANCOMYCINE  ', 'ANTIBIOTIQUES ', 'modéré '),
(187, 'AMLODIPINE ', 'ANTIHYPERTENSEURS ', 'BISOPROLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(188, 'LACTULOSE', '', 'VORICONAZOLE', 'ANTIFONGIQUES ', 'modéré '),
(189, 'VORICONAZOLE', 'ANTIFONGIQUES ', 'SORAFENIB ', '', 'modéré '),
(190, 'ASPEGIC ', '', 'RAMIPRIL ', 'ANTIHYPERTENSEURS ', 'modéré '),
(191, 'ACENOCOUMAROL ', '', 'PREDNISONE', 'CORTICOÏDES ', 'modéré '),
(192, 'AMIODARONE', 'ANTIARYTHMIQUES ', 'BISOPROLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(193, 'LOVENOX (ENOXAPARINE) ', 'HBPM', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(194, 'GENTAMICINE', 'ANTIBIOTIQUES ', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(195, 'RIFAMPICINE', 'ANTIBIOTIQUES ', 'BISOPROLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(196, 'AMITRYPTILINE', '', 'BISOPROLOL', 'ANTIHYPERTENSEURS ', 'modéré '),
(197, 'RIFAMPICINE', 'ANTIBIOTIQUES ', 'METFORMINE', 'ANTIDIABETIQUES ', 'modéré '),
(198, 'PREDNISONE', 'CORTICOÏDES ', 'PYRIDOSTIGMINE', '', 'modéré '),
(199, 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'INSULINE  ', 'ANTIDIABETIQUES ', 'modéré '),
(200, 'COLCHICINE  ', '', 'clopidogrel ', '', 'majeur '),
(201, 'DILTIAZEM ', 'ANTIHYPERTENSEURS ', 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'modéré '),
(202, 'DILTIAZEM ', 'ANTIHYPERTENSEURS ', 'COLCHICINE  ', '', 'majeur '),
(203, 'INSULINE  ', '', 'IRBESARTAN  ', 'ANTIHYPERTENSEURS ', 'modéré '),
(204, 'FUROSEMIDE  ', 'DIURETIQUES', 'IRBESARTAN  ', 'ANTIHYPERTENSEURS ', 'modéré '),
(205, 'MOLSIDOMINE ', '', 'DILTIAZEM ', 'ANTIHYPERTENSEURS ', 'mineur '),
(206, 'ATENOLOL ', 'ANTIHYPERTENSEURS ', 'REPAGLINIDE ', 'ANTIDIABETIQUES ', 'modéré '),
(207, 'GENTAMICINE', 'ANTIBIOTIQUES ', 'CEFAZOLINE ', 'ANTIBIOTIQUES ', 'modéré '),
(208, 'ACIDE ACETYL SALICYLIQUE', 'AINS ', 'REPAGLINIDE ', 'ANTIDIABETIQUES ', 'modéré '),
(209, 'CEFOTAXIME', 'ANTIBIOTIQUES ', 'FUROSEMIDE  ', 'DIURETIQUES', 'modéré '),
(210, 'GENTAMICINE', 'ANTIBIOTIQUES ', 'ESOMEPRAZOLE ', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(211, 'FUROSEMIDE  ', 'DIURETIQUES', 'PHÉNOBARBITAL', 'ANTIEPILEPTIQUE', 'modéré '),
(212, 'VANCOMYCINE  ', 'ANTIBIOTIQUES ', 'CEFOTAXIME', 'ANTIBIOTIQUES ', 'modéré '),
(213, 'FUROSEMIDE  ', 'DIURETIQUES', 'AMIODARONE', 'ANTIARYTHMIQUES ', 'majeur '),
(214, 'CARBAMAZEPINE ', 'ANTIEPILEPTIQUE', 'TOPIRAMATE', 'ANTIEPILEPTIQUE', 'modéré '),
(215, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'glipizide', 'SULFAMIDES HYPOGLYCEMIANTS ', 'modéré '),
(216, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'glibenclamide', 'SULFAMIDES HYPOGLYCEMIANTS ', 'modéré '),
(217, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'gliclazide ', 'SULFAMIDES HYPOGLYCEMIANTS ', 'modéré '),
(218, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', ' glimeperide', 'SULFAMIDES HYPOGLYCEMIANTS ', 'modéré '),
(219, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'TOBRAMYCINE', 'ANTIBIOTIQUES ', 'modéré '),
(220, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'STREPTOMYCINE', 'ANTIBIOTIQUES ', 'modéré '),
(221, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Indométacine', 'AINS ', 'modéré '),
(222, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Naproxène', 'AINS ', 'modéré '),
(223, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Méloxicam', 'AINS ', 'modéré '),
(224, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Kétoprofène', 'AINS ', 'modéré '),
(225, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Acide Mefénamique ', 'AINS ', 'modéré '),
(226, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'CIPROFLOXACINE', 'ANTIBIOTIQUES ', 'modéré '),
(227, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'LORATADINE', '', 'modéré '),
(228, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'GLUCONATE DE POTASSIUM ', '', 'modéré '),
(229, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'MERCILON ', '', 'modéré '),
(230, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'ERYTHROMICYNE', 'ANTIBIOTIQUES ', 'majeur '),
(231, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'rivaroxaban', '', 'modéré '),
(232, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'PRISTINAMYCINE', 'ANTIBIOTIQUES ', 'modéré '),
(233, 'TACROLIMUS ', 'IMMUNOSUPPRESSEURS ', 'Rifampicine ', 'ANTIBIOTIQUES ', 'majeur '),
(234, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'GLUCONATE DE POTASSIUM', '', 'modéré '),
(235, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'colistimethate ', '', 'modéré '),
(236, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PRISTINAMYCINE ', 'ANTIBIOTIQUES ', 'modéré '),
(237, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'déférasirox', '', 'majeur '),
(238, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'METRONIDAZOLE ', '', 'modéré '),
(239, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', 'PENICILLINE V ', '', 'modéré '),
(240, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', ' LEVOFLOXACINE ', 'ANTIBIOTIQUES ', 'modéré '),
(241, 'MYCOPHENOLATE MOFETIL(MMF)', 'IMMUNOSUPPRESSEURS ', ' VANCOMYCINE ', 'ANTIBIOTIQUES ', 'modéré '),
(242, 'BISOPROLOL ', 'ANTIHYPERTENSEURS ', 'CALCIUM ', '', 'modéré '),
(243, 'FUROSEMIDE', 'DIURETIQUES', 'lamsoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(244, 'FUROSEMIDE', 'DIURETIQUES', 'oméprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(245, 'FUROSEMIDE', 'DIURETIQUES', 'pantoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré '),
(246, 'LACTULOSE', '', 'ACETAZOLAMIDE', '', 'modéré'),
(247, 'INSULINE', '', 'LEVOTHYROXINE', '', 'modéré '),
(248, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'CANDESARTAN (ATACAND)', 'ANTIHYPERTENSEURS', 'modéré'),
(249, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'IRBESARTAN  ', 'ANTIHYPERTENSEURS', 'modéré'),
(250, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'losartan', 'ANTIHYPERTENSEURS', 'modéré'),
(251, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'VALSARTAN  ', 'ANTIHYPERTENSEURS', 'modéré'),
(252, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'telmisartan', 'ANTIHYPERTENSEURS', 'modéré'),
(253, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'captopril', 'ANTIHYPERTENSEURS', 'modéré'),
(254, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'énalapril', 'ANTIHYPERTENSEURS', 'modéré'),
(255, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'lisinopril', 'ANTIHYPERTENSEURS', 'modéré'),
(256, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'RAMIPRIL ', 'ANTIHYPERTENSEURS', 'modéré'),
(257, ' Hydrochlorthiazide', 'DIURETIQUES', 'lamsoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(258, 'Hydrochlorthiazide', 'DIURETIQUES', 'oméprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(259, 'Hydrochlorthiazide', 'DIURETIQUES', 'pantoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(260, 'indapamide', 'DIURETIQUES', 'lamsoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(261, 'indapamide', 'DIURETIQUES', 'oméprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(262, 'indapamide', 'DIURETIQUES', 'pantoprazole', 'INHIBITEURS DE LA POMPE A PROTON', 'modéré'),
(263, 'CICLOSPORINE', 'IMMUNOSUPPRESSEURS ', 'PREDNISONE  ', 'CORTICOÏDES ', 'modéré ');

-- --------------------------------------------------------

--
-- Structure de la table `medecin`
--

DROP TABLE IF EXISTS `medecin`;
CREATE TABLE IF NOT EXISTS `medecin` (
  `id_medecin` int NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `sexe` enum('M','F','Autre') NOT NULL,
  `date_naissance` date NOT NULL,
  `email` varchar(150) NOT NULL,
  `nom_utilisateur` varchar(100) NOT NULL,
  `mot_de_passe` varchar(100) NOT NULL,
  `telephone` int NOT NULL,
  `adresse` varchar(200) NOT NULL,
  `id_grade` int DEFAULT NULL,
  `id_unite` int DEFAULT NULL,
  `id_specialite` int DEFAULT NULL,
  PRIMARY KEY (`id_medecin`),
  KEY `id_grade` (`id_grade`),
  KEY `id_unite` (`id_unite`),
  KEY `id_specialite` (`id_specialite`)
) ;

--
-- Déchargement des données de la table `medecin`
--

INSERT INTO `medecin` (`id_medecin`, `nom`, `prenom`, `sexe`, `date_naissance`, `email`, `nom_utilisateur`, `mot_de_passe`, `telephone`, `adresse`, `id_grade`, `id_unite`, `id_specialite`) VALUES
(36, 'makhlouf', 'kawther', 'F', '2000-01-26', 'kawthermm@gmail.com', 'kawther', '1234', 55555566, 'xxxxxyy', 4, 1, 1),
(37, 'ikhlas', 'ouasti', 'F', '1994-05-28', 'iklas@gmail.com', 'ikhlas', '1234', 55555555, 'xxxxxxxxx', NULL, NULL, NULL),
(38, 'ikhlasaa', 'ouasti', 'M', '1994-05-28', 'iklas@gmail.com', 'ikhlasaaa', '', 55555555, 'xxxxxxxxx', 2, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `medicament`
--

DROP TABLE IF EXISTS `medicament`;
CREATE TABLE IF NOT EXISTS `medicament` (
  `id_medicament` int NOT NULL AUTO_INCREMENT,
  `nom_medicament` varchar(100) NOT NULL,
  `dosage` varchar(255) DEFAULT NULL,
  `nom_compro` varchar(255) DEFAULT NULL,
  `taille` varchar(255) DEFAULT NULL,
  `id_voie` int DEFAULT NULL,
  PRIMARY KEY (`id_medicament`),
  KEY `id_voie` (`id_voie`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `medicament`
--

INSERT INTO `medicament` (`id_medicament`, `nom_medicament`, `dosage`, `nom_compro`, `taille`, `id_voie`) VALUES
(2, 'med', '20', 'med', NULL, 4),
(3, 'med', '20', 'med', NULL, 5),
(4, 'med', '20', 'med', NULL, 1),
(5, 'med', '20', 'med', NULL, 5),
(6, 'med', '20', 'med', NULL, 6),
(7, 'med', '20', 'med', NULL, 4),
(8, 'medicament1', '20', 'medicament1', NULL, 4),
(9, 'medicament1', '20', 'medicament1', NULL, 5),
(10, 'medicament2', '20', 'medicament2', NULL, 5),
(11, 'med1', '20', 'med1', NULL, 5),
(12, 'med1', '20', 'med1', NULL, 6),
(13, 'CICLOSPORIN', '20 mg', 'mm', NULL, 4),
(14, 'medm', '20', 'medd', NULL, 6);

-- --------------------------------------------------------

--
-- Structure de la table `motif`
--

DROP TABLE IF EXISTS `motif`;
CREATE TABLE IF NOT EXISTS `motif` (
  `id_motif` int NOT NULL AUTO_INCREMENT,
  `nom_motif` varchar(100) NOT NULL,
  `abreviation` varchar(50) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_motif`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `nom_examen`
--

DROP TABLE IF EXISTS `nom_examen`;
CREATE TABLE IF NOT EXISTS `nom_examen` (
  `id_nom_examen` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_nom_examen`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `nom_examen`
--

INSERT INTO `nom_examen` (`id_nom_examen`, `nom`) VALUES
(1, 'poids'),
(2, 'labstix'),
(3, 'glycémie'),
(4, 'tension'),
(5, 'Glycémie'),
(6, 'Labstix'),
(7, 'Glycémie'),
(8, 'Glycémie');

-- --------------------------------------------------------

--
-- Structure de la table `options_habitudes`
--

DROP TABLE IF EXISTS `options_habitudes`;
CREATE TABLE IF NOT EXISTS `options_habitudes` (
  `id_option_habitude` int NOT NULL AUTO_INCREMENT,
  `nom_habitude` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_option_habitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `options_habitudes`
--

INSERT INTO `options_habitudes` (`id_option_habitude`, `nom_habitude`) VALUES
(1, 'Tabagisme'),
(2, 'Alcool'),
(3, 'Drogue');

-- --------------------------------------------------------

--
-- Structure de la table `orientation`
--

DROP TABLE IF EXISTS `orientation`;
CREATE TABLE IF NOT EXISTS `orientation` (
  `id_orientation` int NOT NULL AUTO_INCREMENT,
  `date_orientation` date NOT NULL,
  `type_orientation` enum('externe','interne','urgence') NOT NULL,
  `id_service_origine` int DEFAULT NULL,
  `id_service_destination` int DEFAULT NULL,
  `id_patient` int DEFAULT NULL,
  PRIMARY KEY (`id_orientation`),
  KEY `id_service_origine` (`id_service_origine`),
  KEY `id_service_destination` (`id_service_destination`),
  KEY `id_patient` (`id_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `orientation`
--

INSERT INTO `orientation` (`id_orientation`, `date_orientation`, `type_orientation`, `id_service_origine`, `id_service_destination`, `id_patient`) VALUES
(1, '2023-06-07', 'interne', 3, 6, 45),
(2, '2023-06-14', 'interne', 7, 6, 49),
(3, '2023-06-15', 'interne', 6, 5, 50),
(4, '2023-06-14', 'urgence', 6, 4, 51);

-- --------------------------------------------------------

--
-- Structure de la table `parametre_bilan`
--

DROP TABLE IF EXISTS `parametre_bilan`;
CREATE TABLE IF NOT EXISTS `parametre_bilan` (
  `id_parametre` int NOT NULL AUTO_INCREMENT,
  `nom_parametre` varchar(100) NOT NULL,
  `unite_mesure` varchar(50) DEFAULT NULL,
  `valeur_min` float DEFAULT NULL,
  `valeur_max` float DEFAULT NULL,
  PRIMARY KEY (`id_parametre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `id_patient` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `sexe` enum('femme','homme','autre') NOT NULL,
  `date_naissance` date NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `telephone` int DEFAULT NULL,
  `adresse` varchar(200) DEFAULT NULL,
  `groupe_sanguin` enum('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
  `profession` varchar(255) DEFAULT NULL,
  `situation_familiale` enum('Célibataire','Marié(e)','Divorcé(e)') DEFAULT NULL,
  PRIMARY KEY (`id_patient`)
) ;

--
-- Déchargement des données de la table `patient`
--

INSERT INTO `patient` (`id_patient`, `nom`, `prenom`, `sexe`, `date_naissance`, `email`, `telephone`, `adresse`, `groupe_sanguin`, `profession`, `situation_familiale`) VALUES
(3, 'dcd', 'dccd', 'femme', '2023-05-03', 'dcdcdcdc@gmail.com', 1444, 'dsdfd', 'B+', 'ddfsdf', 'Célibataire'),
(4, 'abggg', 'ccccc', 'femme', '2023-05-04', 'bvvbv@gmail.om', 1233456, '', '', '', ''),
(5, 'TTT', 'HHH', '', '1900-01-02', 'GGG@GHHJ.COM', 5556, 'KKJJ', 'A-', 'JJJJ', 'Marié(e)'),
(6, 'kaid', 'omar adel', '', '1900-01-06', 'kaiomaradel@gmail.com', 664590601, 'Mostaganm', 'A+', 'RESIDANTS', 'Célibataire'),
(7, 'makhlouf', 'kawther', 'femme', '1900-01-13', 'makhlouf@gmail.com', 556257004, '22 rue ', 'B+', 'etudiant', 'Célibataire'),
(9, 'ma', 'mohamed', 'homme', '2023-05-30', 'mmmm@gmail.com', 55555, 'mmmmmmmmm', 'A+', 'agent', 'Marié(e)'),
(10, 'Célibataire', 'aaaa', 'femme', '2023-05-30', 'aaaaa@gmail.com', 555, 'aaaa', 'A+', 'aaaa', 'Célibataire'),
(11, 'aa', 'aaa', 'homme', '2023-05-30', 'aaa@gmail.com', 0, '4aaa', 'A+', 'aaaaa', 'Célibataire'),
(12, 'mohaeeddd', 'aaaaa', 'femme', '2023-06-10', 'aaaaa@gmail.com', 55555, 'aaaaaaaa', 'AB+', 'aaaaa', 'Célibataire'),
(13, 'linda', 'mmama', 'homme', '2023-06-10', 'aaaa@gmail.com', 5555, 'mmmmmm', 'B+', 'aaaa', 'Marié(e)'),
(14, 'meriem', 'makhl', 'homme', '2023-06-11', 'aaaa@gmail.com', 55555, 'mmmmmmmm', 'A+', 'sssssssss', 'Célibataire'),
(15, 'lindaaaa', 'mamamam', 'femme', '2023-06-13', 'mamam@gmail.com', 6666666, 'AAAA', 'A+', 'AAAAA', 'Célibataire'),
(16, 'mama', 'mama', 'femme', '2023-06-13', 'mama@gmail.com', 366, 'mmamam', 'A+', 'mama', 'Célibataire'),
(17, 'maria', 'mimiimu', 'homme', '2023-06-13', 'aa@gmail.com', 4444, 'aaaaaa', 'A+', 'aaaaaa', 'Célibataire'),
(18, 'aaaa', 'aaa', 'femme', '2023-06-13', 'pap@gmail.com', 5555, 'aaaaaaa', 'A+', 'aaa', 'Célibataire'),
(19, 'mojaj', '666a', 'homme', '2023-06-13', 'aaa@gmail.com', 5555, 'aaaaa', 'A+', 'aaa', 'Célibataire'),
(20, 'aa', 'az', 'femme', '2023-06-13', 'lll@gmail.com', 555, 'aaaaa', 'A+', 'aaa', 'Célibataire'),
(21, 'll', 'aaaa', 'homme', '2023-06-13', 'mmm@gmail.com', 555, 'aaaaaa', 'A+', 'llllllll', 'Célibataire'),
(22, 'maria', 'maria', 'femme', '2023-06-13', 'maria@gmail.com', 555, 'aaaa', 'A+', 'ennnf', 'Célibataire'),
(23, 'aaa', 'aaaaaaaa', 'homme', '2023-06-13', 'aaaaa@gmail.com', 6666, 'aaaa', 'A+', 'aaaaa', 'Célibataire'),
(24, 'mmm', 'mmmm', 'femme', '2023-06-13', 'aaa@gmail.com', 555, 'mmm', 'A+', 'aaa', 'Célibataire'),
(25, 'mm', 'm', 'homme', '2023-06-13', 'aaaa@gmail.com', 5555, 'mmmmmmm', 'A+', 'llll', 'Célibataire'),
(26, 'mamam', 'mama', 'femme', '2023-06-13', 'aaa@gmail.com', 555, 'aaa', 'A-', 'zzz', 'Célibataire'),
(27, 'aaa', 'aa', 'femme', '2023-06-13', 'aa@gmail.com', 555, 'aaa', 'A+', 'aaa', 'Célibataire'),
(28, 'mamam', 'mmm', 'homme', '2023-06-13', 'mmm@gmail.com', 555, 'aaaaa', 'A+', 'aaaaaa', 'Célibataire'),
(29, 'aa', 'aaa', 'homme', '2023-06-13', 'aa@gmail.com', 555555, 'pppp', 'A+', 'aa', 'Célibataire'),
(30, 'mamam', 'mamam', 'homme', '2023-06-13', 'aaaa@gmail.com', 555, 'mmmm', 'A+', 'aaa', 'Célibataire'),
(31, 'amama', 'mamam', 'homme', '2023-06-13', 'aaa@gmail.com', 555, 'aaaa', 'B-', 'aaa', 'Célibataire'),
(32, 'mamam', 'mamam', 'autre', '2023-06-13', 'mm@gmail.com', 555555, 'aaaaa', 'B+', 'aaa', 'Marié(e)'),
(33, 'mamam', 'aaa', 'homme', '2023-06-13', 'aaa@gmail.com', 666666, 'mmmm', 'A+', 'aaa', 'Célibataire'),
(34, 'aaa', 'aaa', 'homme', '2023-06-13', 'aaa@gmail.com', 555, 'aaaa', 'A+', 'aaa', 'Célibataire'),
(35, 'aaa', 'aaa', 'homme', '2023-06-13', 'aaa@gmail.com', 55, 'aaa', 'A+', 'aaa', 'Célibataire'),
(36, 'amam', 'mama', 'homme', '2023-06-13', 'aa@gmail.com', 666, 'aaaa', 'A+', 'aaa', 'Célibataire'),
(37, 'salim', 'makhlouf', 'homme', '2023-06-13', 'kawther@gmail.com', 55555, 'mmmmm', 'O+', 'medecin', 'Marié(e)'),
(38, 'linda', 'mk', 'femme', '2023-06-13', 'mmm@gmail.com', 6666, 'mmm', 'B-', 'aaa', 'Marié(e)'),
(39, 'mamam', 'mmmm', 'homme', '2023-06-13', 'ppp@gmail.com', 666, 'aaa', 'B-', 'aaa', 'Marié(e)'),
(40, 'aaa', 'aaa', 'autre', '2023-06-13', 'aaa@gmail.com', 666, 'aa', 'B-', 'aa', 'Divorcé(e)'),
(41, 'aaaa', 'aaa', 'homme', '2023-06-13', 'pm@gmail.com', 0, 'aaa', 'AB-', 'aa', 'Célibataire'),
(42, 'mm', 'mm', 'homme', '2023-06-13', 'mmm@gmail.com', 555, 'aaaaa', 'B+', 'aaa', 'Célibataire'),
(43, 'mmama', 'aa', 'homme', '2023-06-13', 'aaa@gmail.com', 555, 'lll', 'A-', 'mmm', 'Célibataire'),
(44, 'mmm', 'mmm', 'homme', '2023-06-13', 'mmmm@gmail.com', 555, 'mmm', 'B-', 'aaaa', 'Célibataire'),
(45, 'mmma', 'aaa', 'homme', '2023-06-13', 'mmmm@gmail.com', 5555, 'mmm', 'B+', 'mmm', 'Célibataire'),
(46, 'mmm', 'mmm', 'homme', '2023-06-13', 'aaa@gmail.com', 555, 'aaaa', 'B+', 'aaa', 'Célibataire'),
(47, 'aaa', 'aaa', 'homme', '2023-06-13', 'aaa@gmail.com', 555, 'aaa', 'AB+', 'aaa', 'Marié(e)'),
(48, 'imen', 'bou', 'femme', '2023-06-14', 'mmm@gmail.com', 5555, 'mmmmmm', 'B-', 'bnbn', 'Célibataire'),
(49, 'mamma', 'mmm', 'homme', '2023-06-14', 'aaa@gmail.com', 55, 'kkk', 'AB-', 'aaa', 'Célibataire'),
(50, 'Ouasti', 'Ikhlas', 'femme', '2023-06-15', 'ikhlaso@gmail.com', 55555, 'fernanville', 'AB+', 'medecin ophtalmo', 'Marié(e)'),
(51, 'xxxx', 'yyyy', 'homme', '2023-06-15', 'ppp@gmail.com', 5555, 'mmmmm', 'B+', 'aaaa', 'Marié(e)');

-- --------------------------------------------------------

--
-- Structure de la table `profil_utilisateur`
--

DROP TABLE IF EXISTS `profil_utilisateur`;
CREATE TABLE IF NOT EXISTS `profil_utilisateur` (
  `id_profil` int NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int DEFAULT NULL,
  `id_grade` int DEFAULT NULL,
  `id_unite` int DEFAULT NULL,
  `id_specialite` int DEFAULT NULL,
  PRIMARY KEY (`id_profil`),
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_grade` (`id_grade`),
  KEY `id_unite` (`id_unite`),
  KEY `id_specialite` (`id_specialite`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `service`
--

DROP TABLE IF EXISTS `service`;
CREATE TABLE IF NOT EXISTS `service` (
  `id_service` int NOT NULL AUTO_INCREMENT,
  `nom_service` varchar(100) NOT NULL,
  `id_hopital` int DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_service`),
  KEY `id_hopital` (`id_hopital`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `service`
--

INSERT INTO `service` (`id_service`, `nom_service`, `id_hopital`, `description`) VALUES
(1, 'néphrologie ', 1, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `service_destination`
--

DROP TABLE IF EXISTS `service_destination`;
CREATE TABLE IF NOT EXISTS `service_destination` (
  `id_service` int NOT NULL AUTO_INCREMENT,
  `nom_service` varchar(100) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_service`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `service_destination`
--

INSERT INTO `service_destination` (`id_service`, `nom_service`, `description`) VALUES
(1, 'Néphrologie', NULL),
(2, 'Dermatologie', NULL),
(3, 'Epidémiologie', NULL),
(4, 'Gastro-entérologie', NULL),
(5, 'Gynécologie-obstétrique', NULL),
(6, 'Hématologie', NULL),
(7, 'Histologie', NULL),
(8, 'Maladies infectieuses', NULL),
(9, 'Médecine du travail', NULL),
(10, 'Médecine interne', NULL),
(11, 'Chirurgie hépatobiliaire', NULL),
(12, 'Neurologie', NULL),
(13, 'Chirurgie thoracique', NULL),
(14, 'Oncologie médicale', NULL),
(15, 'Urgences', NULL),
(16, 'Orl', NULL),
(17, 'Orthopédie', NULL),
(18, 'Pneumologie', NULL),
(19, 'Psychiatrie', NULL),
(20, 'Rhumatologie', NULL),
(21, 'Médecine légale', NULL),
(22, 'Chirurgie maxilo-faciale', NULL),
(23, 'Chirurgie générale', NULL),
(24, 'Néphrologie', NULL),
(25, 'Cardiologie', NULL),
(26, 'Endocrinologie', NULL),
(27, 'Pharmacologie', NULL),
(28, 'Transfusion sanguine', NULL),
(29, 'Maternité', NULL),
(30, 'Ophtalmologie', NULL),
(31, 'Urologie', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `service_origine`
--

DROP TABLE IF EXISTS `service_origine`;
CREATE TABLE IF NOT EXISTS `service_origine` (
  `id_service_origine` int NOT NULL AUTO_INCREMENT,
  `nom_service` varchar(100) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_service_origine`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `service_origine`
--

INSERT INTO `service_origine` (`id_service_origine`, `nom_service`, `description`) VALUES
(1, 'Néphrologie', NULL),
(2, 'Dermatologie', NULL),
(3, 'Epidémiologie', NULL),
(4, 'Gastro-entérologie', NULL),
(5, 'Gynécologie-obstétrique', NULL),
(6, 'Hématologie', NULL),
(7, 'Histologie', NULL),
(8, 'Maladies infectieuses', NULL),
(9, 'Médecine du travail', NULL),
(10, 'Médecine interne', NULL),
(11, 'Chirurgie hépatobiliaire', NULL),
(12, 'Neurologie', NULL),
(13, 'Chirurgie thoracique', NULL),
(14, 'Oncologie médicale', NULL),
(15, 'Urgences', NULL),
(16, 'Orl', NULL),
(17, 'Orthopédie', NULL),
(18, 'Pneumologie', NULL),
(19, 'Psychiatrie', NULL),
(20, 'Rhumatologie', NULL),
(21, 'Médecine légale', NULL),
(22, 'Chirurgie maxilo-faciale', NULL),
(23, 'Chirurgie générale', NULL),
(24, 'Néphrologie', NULL),
(25, 'Cardiologie', NULL),
(26, 'Endocrinologie', NULL),
(27, 'Pharmacologie', NULL),
(28, 'Transfusion sanguine', NULL),
(29, 'Maternité', NULL),
(30, 'Ophtalmologie', NULL),
(31, 'Urologie', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `specialite`
--

DROP TABLE IF EXISTS `specialite`;
CREATE TABLE IF NOT EXISTS `specialite` (
  `id_specialite` int NOT NULL AUTO_INCREMENT,
  `nom_specialite` varchar(100) DEFAULT NULL,
  `id_service` int DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_specialite`),
  KEY `id_service` (`id_service`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `specialite`
--

INSERT INTO `specialite` (`id_specialite`, `nom_specialite`, `id_service`, `description`) VALUES
(1, 'néphrologie ', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `symptome`
--

DROP TABLE IF EXISTS `symptome`;
CREATE TABLE IF NOT EXISTS `symptome` (
  `id_symptome` int NOT NULL AUTO_INCREMENT,
  `id_type_symptome` int NOT NULL,
  `id_gravite_symptome` int NOT NULL,
  `date_symptome` date DEFAULT NULL,
  `id_consultation` int NOT NULL,
  PRIMARY KEY (`id_symptome`),
  KEY `fk5_consultation` (`id_consultation`),
  KEY `fk1_type_symptome` (`id_type_symptome`),
  KEY `fk1_gravite_sympthome` (`id_gravite_symptome`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `symptome`
--

INSERT INTO `symptome` (`id_symptome`, `id_type_symptome`, `id_gravite_symptome`, `date_symptome`, `id_consultation`) VALUES
(1, 3, 4, '2023-06-12', 80),
(2, 34, 2, '2023-06-15', 105);

-- --------------------------------------------------------

--
-- Structure de la table `traitement`
--

DROP TABLE IF EXISTS `traitement`;
CREATE TABLE IF NOT EXISTS `traitement` (
  `id_traitement` int NOT NULL AUTO_INCREMENT,
  `id_medicament` int DEFAULT NULL,
  `id_consultation` int DEFAULT NULL,
  `medicament_actuel` enum('oui','non','prescrit') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `duree_prise` int DEFAULT NULL,
  PRIMARY KEY (`id_traitement`),
  KEY `id_medicament` (`id_medicament`),
  KEY `id_consultation` (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `traitement`
--

INSERT INTO `traitement` (`id_traitement`, `id_medicament`, `id_consultation`, `medicament_actuel`, `date_debut`, `date_fin`, `duree_prise`) VALUES
(1, 3, 87, 'oui', '2023-06-12', '2023-06-12', 20),
(2, 4, 88, 'oui', '2023-06-07', '2023-05-30', 20),
(3, 5, 94, 'non', '2023-06-12', '2023-06-13', 20),
(4, 6, 96, 'oui', '2023-06-14', '2023-06-14', 20),
(5, 7, 96, 'prescrit', '2023-06-13', '2023-06-20', 22),
(6, 8, 102, 'prescrit', '2023-06-16', '2023-06-14', 20),
(7, 9, 103, 'prescrit', '2023-06-14', '2023-06-14', 20),
(8, 10, 103, 'prescrit', '2023-06-13', '2023-06-01', 20),
(9, 11, 104, 'prescrit', '2023-06-15', '2023-06-15', 20),
(10, 12, 105, 'prescrit', '2023-06-06', '2023-06-15', 20),
(11, 13, 106, 'prescrit', '2023-06-15', '2023-06-15', 20),
(12, 14, 107, 'prescrit', '2023-06-16', '2023-06-16', 20);

-- --------------------------------------------------------

--
-- Structure de la table `typeantecedent`
--

DROP TABLE IF EXISTS `typeantecedent`;
CREATE TABLE IF NOT EXISTS `typeantecedent` (
  `id_type` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `description` text,
  `antecedent` int DEFAULT NULL,
  PRIMARY KEY (`id_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `type_symptome`
--

DROP TABLE IF EXISTS `type_symptome`;
CREATE TABLE IF NOT EXISTS `type_symptome` (
  `id_type_symptome` int NOT NULL AUTO_INCREMENT,
  `nom_type_symptome` varchar(255) NOT NULL,
  `abreviation` varchar(50) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_type_symptome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `type_symptome`
--

INSERT INTO `type_symptome` (`id_type_symptome`, `nom_type_symptome`, `abreviation`, `description`) VALUES
(1, 'Anurie', 'ANU', 'Absence ou diminution significative de la production d\'urine'),
(2, 'Arthralgie', 'ART', 'Douleurs articulaires'),
(3, 'Battements cardiaques rapides', 'BCR', 'Rythme cardiaque accéléré'),
(4, 'Bourdonnements d\'oreilles', 'BOU', 'Sensation de bruit ou de bourdonnement dans les oreilles'),
(5, 'Bouffissure de visage', 'BOV', 'Gonflement du visage'),
(6, 'Brûlure mictionnelle', 'BRM', 'Sensation de brûlure ou de douleur lors de la miction'),
(7, 'Confusion', 'CON', 'Trouble de la pensée ou de la compréhension'),
(8, 'Constipation', 'CON', 'Difficulté à évacuer les selles de manière régulière'),
(9, 'Convulsions ou crises convulsives', 'CON', 'Contractions musculaires soudaines et involontaires'),
(10, 'Crampes musculaires', 'CRA', 'Contractions musculaires douloureuses et involontaires'),
(11, 'Diarrhée', 'DIA', 'Selles fréquentes et liquides'),
(12, 'Difficulté à parler ou à comprendre la parole', 'DPC', 'Troubles de la communication verbale'),
(13, 'Difficulté à respirer ou respiration sifflante', 'DRS', 'Inconfort respiratoire ou sifflements lors de la respiration'),
(14, 'Douleurs abdominales', 'DOA', 'Douleurs dans la région de l\'abdomen'),
(15, 'Douleurs abdominales intenses', 'DOI', 'Douleurs intenses dans la région de l\'abdomen'),
(16, 'Douleurs articulaires', 'DOA', 'Douleurs dans les articulations'),
(17, 'Douleurs lombaires', 'DOL', 'Douleurs dans la région lombaire'),
(18, 'Douleurs musculaires', 'DOM', 'Douleurs dans les muscles'),
(19, 'Douleurs pelviennes', 'DOP', 'Douleurs dans la région pelvienne'),
(20, 'Douleurs thoraciques', 'DOT', 'Douleurs dans la région thoracique'),
(21, 'Douleurs à la poitrine', 'DOP', 'Douleurs dans la poitrine'),
(22, 'Démangeaisons', 'DEM', 'Sensation d\'irritation cutanée qui provoque le besoin de se gratter'),
(23, 'Engourdissement ou faiblesse soudaine d\'un côté du corps', 'EFC', 'Perte de sensibilité ou de force dans un côté du corps'),
(24, 'Essoufflement', 'ESS', 'Difficulté à respirer ou sensation de manque d\'air'),
(25, 'Essoufflement au repos', 'ESR', 'Difficulté à respirer même au repos'),
(26, 'Essoufflement intense', 'ESI', 'Difficulté extrême à respirer ou sensation d\'étouffement'),
(27, 'Éruptions cutanées', 'ERC', 'Apparition de plaques, rougeurs ou lésions sur la peau'),
(28, 'Éruptions cutanées sévères ou éruptions cutanées généralisées', 'ERC', 'Apparition étendue de plaques, rougeurs ou lésions sur la peau'),
(29, 'Étourdissements sévères ou perte de conscience', 'ETC', 'Sensation de déséquilibre, vertiges intenses ou perte de connaissance'),
(30, 'Évanouissements', 'EVA', 'Perte de connaissance brève et soudaine'),
(31, 'Fatigue persistante et sensation de faiblesse', 'FAT', 'Épuisement constant et sentiment de manque d\'énergie'),
(32, 'Fièvre', 'FIE', 'Augmentation de la température corporelle'),
(33, 'Frissons', 'FRI', 'Sensation de froid accompagnée de tremblements'),
(34, 'Gonflement des pieds et des chevilles (œdème)', 'GON', 'Augmentation de volume des pieds et des chevilles'),
(35, 'Hypertension artérielle (pression artérielle élevée)', 'HYP', 'Augmentation de la pression sanguine dans les artères'),
(36, 'Lombalgie', 'LOM', 'Douleurs dans la région lombaire'),
(37, 'Mal de gorge', 'MDS', 'Douleur ou irritation de la gorge'),
(38, 'Maux de tête', 'MDT', 'Douleurs localisées à la tête'),
(39, 'Maux de tête sévères', 'MDT', 'Douleurs intenses localisées à la tête'),
(40, 'Mictions fréquentes', 'MIF', 'Besoin fréquent d\'uriner'),
(41, 'Nausées', 'NAU', 'Sensation de malaise à l\'estomac avec envie de vomir'),
(42, 'Palpitations cardiaques', 'PAL', 'Sensation de battements irréguliers ou forts du cœur'),
(43, 'Perte d\'appétit', 'PAP', 'Diminution ou absence d\'envie de manger'),
(44, 'Perte de poids', 'PDW', 'Diminution de la masse corporelle'),
(45, 'Pic d\'HTA (hypertension artérielle)', 'PIC', 'Augmentation temporaire de la pression artérielle'),
(46, 'Protéinurie', 'PRO', 'Présence anormale de protéines dans les urines'),
(47, 'Pâleur de la peau', 'PAU', 'Teint pâle ou blanchâtre de la peau'),
(48, 'Problèmes de concentration et de mémoire', 'PCM', 'Difficultés à se concentrer ou à se souvenir des choses'),
(49, 'Sensation de brûlure en urinant', 'SBU', 'Sensation de brûlure ou de douleur lors de la miction'),
(50, 'Soif excessive', 'SOI', 'Besoin constant de boire'),
(51, 'Troubles du sommeil', 'TDS', 'Difficultés à s\'endormir ou à maintenir un sommeil régulier'),
(52, 'Urines fréquentes et abondantes ou, au contraire, diminution de la quantité d\'urine', 'URF', 'Volume urinaire anormal, soit augmenté, soit diminué'),
(53, 'Urines mousseuses ou présence de sang dans les urines', 'URM', 'Présence anormale de mousse ou de sang dans les urines'),
(54, 'Vertiges', 'VER', 'Sensation de rotation ou d\'instabilité'),
(55, 'Yeux rouges', 'YER', 'Rougeur des yeux'),
(56, 'Vision floue', 'VIF', 'Perte de netteté de la vision');

-- --------------------------------------------------------

--
-- Structure de la table `unite`
--

DROP TABLE IF EXISTS `unite`;
CREATE TABLE IF NOT EXISTS `unite` (
  `id_unite` int NOT NULL AUTO_INCREMENT,
  `nom_unite` enum('consultation','greffe rénale','hémodialyse') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id_service` int DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_unite`),
  KEY `id_service` (`id_service`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `unite`
--

INSERT INTO `unite` (`id_unite`, `nom_unite`, `id_service`, `description`) VALUES
(1, 'consultation', 1, NULL),
(2, 'greffe rénale', 1, NULL),
(3, 'hémodialyse', 1, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `sexe` enum('M','F','Autre') NOT NULL,
  `date_naissance` date NOT NULL,
  `email` varchar(150) NOT NULL,
  `telephone` int NOT NULL,
  `adresse` varchar(200) NOT NULL,
  `nom_utilisateur` varchar(100) NOT NULL,
  `mot_passe` varchar(100) NOT NULL,
  `confirm_mot_passe` varchar(100) NOT NULL,
  `date_inscription` datetime NOT NULL,
  `dernier_login` datetime DEFAULT NULL,
  `statut` enum('actif','inactif') NOT NULL DEFAULT 'actif',
  `role` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_utilisateur`),
  UNIQUE KEY `nom_utilisateur` (`nom_utilisateur`)
) ;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id_utilisateur`, `nom`, `prenom`, `sexe`, `date_naissance`, `email`, `telephone`, `adresse`, `nom_utilisateur`, `mot_passe`, `confirm_mot_passe`, `date_inscription`, `dernier_login`, `statut`, `role`) VALUES
(1, 'bouchakour', 'imene', '', '0000-00-00', 'bouchakourimene31@gmail.com', 792145384, 'st hubert, oran', 'ibouchakour', 'imene', 'imene', '2023-04-02 18:00:15', '2023-05-27 17:13:55', 'actif', NULL),
(2, 'bouchakour', 'ikram', '', '0000-00-00', 'ibouchakour@gmail.com', 712345689, 'st hubet, oran', 'ikram', 'ikram', 'ikram', '2023-04-24 00:52:14', '2023-04-24 00:52:14', 'actif', 'medecin'),
(4, 'bouchakour', 'imene', '', '0000-00-00', 'bouchakourimene31@gmail.com', 792145384, 'st hubert', 'bimene', 'imene', 'imene', '2023-04-24 14:59:07', '2023-04-24 14:59:07', 'actif', 'medecin'),
(5, 'fatiha', 'fatiha', 'F', '2003-05-27', 'fatiha@gmail.com', 556257004, 'canastel', 'fatiha', '$2b$12$H5cet1LHz3XRjkx7g6NlxOnwKwCCFLtv7AkZfgM/xwzgB5G0VbJ3u', '$2b$12$3pYuf6SLdzI/xuEBErFlw.sYQSzEb/fArB6DJGmeAs44dEVBCOTe6', '2023-05-27 12:09:04', '2023-05-27 17:11:58', 'actif', 'medecin'),
(10, 'meriem', 'meriem', 'F', '2023-05-27', 'ma@gmail.com', 5555, 'aaa', 'marie', '$2b$12$LZZWRyRVKQJhHtfgjUkdnu4//OSHm14EN8d5aloY1hhIgvtqgzOZi', '$2b$12$XwqoEmdHLsilxEc5v39g1OaqVWfyNWPK2WNrX/qRgPbPFElsK1T5i', '2023-05-27 19:59:26', '2023-05-27 19:59:26', 'actif', 'medecin'),
(11, 'babi', 'babi', 'M', '2023-05-27', 'babi@gmail.com', 55555, 'aaaa', 'babi', '$2b$12$wg3IQRcUVg1BBdQwe0d2X.HYe7JWM/USmM9giDD/EM6N8VGRWZ3J6', '$2b$12$ygwWsRjD5m.t8fAauKnVz.J86XM4Zu4WIsWh0vBUmr1s9/OGilcIy', '2023-05-27 20:01:42', '2023-05-27 20:01:42', 'actif', 'medecin'),
(12, 'salim', 'salim', 'M', '2023-05-27', 'salim@gmail.com', 55555, 'mmmm', 'salim', '$2b$12$407SYLp3t43VZtyQ84xtdu5hjPekGW3gWcnFDdzb07SCN6kderRCy', '$2b$12$xbCkdbI/sVaXVhqyufmqsu2LUqkS1t5aopYBhcwW8ttnTFQhWhqN6', '2023-05-27 20:04:43', '2023-05-27 20:04:43', 'actif', 'medecin'),
(13, 'zaki', 'zaki', 'M', '2023-05-27', 'zaki@gmail.com', 5555, 'mmmm', 'zaki', '1234', '1234', '2023-05-27 20:05:53', '2023-05-27 21:02:51', 'actif', 'medecin'),
(14, 'aaa', 'aa', 'M', '2023-05-27', 'aaa@gmail.com', 444, 'aaa', 'aa', '$2b$12$UZ7/qzMoHRqHhczovMMvz.4g23PKfuluvF8MqJPe1NOS8dxhDtxlq', '$2b$12$lg4a2KLOsbORyrH2xj7uROadbMxlwk8yGU65OWP0yDuii7xndzzgq', '2023-05-27 20:52:58', '2023-05-27 20:52:58', 'actif', 'medecin'),
(16, 'mohamed', 'mohamed', 'M', '2023-05-27', 'mohamed@gmail.com', 2222, 'aaaa', 'mohamed', '$2b$12$9FdcU45s1OiwD0dPPR.hZOllMjPk7KfGb7h6LphlCEZInMlPz5Ncm', '$2b$12$9btSs62zObvy1Ow0MgmhHe0sK3syTjF93i6kSV6f0SjKyK1Timlgu', '2023-05-27 21:27:29', '2023-05-27 21:27:29', 'actif', 'medecin'),
(18, 'linda', 'linda', 'M', '2023-05-27', 'aaa@gmail.com', 0, 'aaa', 'linda', '$2b$12$wFRZYLbTqiKEuslF3szjIeNU6yBWG.VpleSq8XyAov5aK5JLYzxn6', '$2b$12$2UxEh8v0lSZmBdZbdN6wGOmhYp6YchC0I977KkSEJLeggUj0Wejb6', '2023-05-27 21:33:38', '2023-05-27 21:33:38', 'actif', 'medecin'),
(20, 'houaria', 'houaria', 'M', '2023-05-27', 'aaa@gmail.com', 0, 'aaa', 'houaria', '$2b$12$8SC.qkfD/YNHAZIDmGKDz.W5sX.Etr/PD5O.TJXBzd8EAqA17QdHq', '$2b$12$X9vA6zv6pB49OWDEsNoJ1eCdioYBnrgAc9Yvk4N7amsK5AvV6Fec.', '2023-05-27 21:34:37', '2023-05-27 21:34:37', 'actif', 'medecin'),
(22, 'lili', 'lili', 'M', '2023-05-27', 'lll@gmail.com', 4444, 'mmmm', 'lili', '$2b$12$QO4LHBM5TQQWImySxN9pROcd6nMEiNhyYgdqW6isef6h.9Ua2WBt.', '$2b$12$igYv0QjVkJgfTmQn...MFu1Q5ENgcOsoYFmUB7sbPOUitSSVbxayK', '2023-05-27 21:35:32', '2023-05-27 21:35:32', 'actif', 'medecin'),
(24, 'meknasi', 'meknasi', 'M', '2023-05-27', 'maknasi@gmail.com', 55555, 'XXX', 'meknasi', '$2b$12$S9ByZNQl9pBpv.Rv1jeLsObadDZJ1mnLC.uVa8z/0MO/D8uzcDHZS', '$2b$12$luW73wmt9NtcPLCjluq.aek472KMGxFai.GgrbvTfHxKNHokixAG2', '2023-05-27 21:40:24', '2023-05-27 21:40:24', 'actif', 'medecin'),
(25, 'meknasi', 'meknsai', 'M', '2023-05-27', 'zzz@gmail.com', 55555, 'aaaaa', 'mek', '$2b$12$i7t9E2gSq67yrLDHaypqmeSnf/3Q0kq2DsCuikoWVkj7GS9fhp6sG', '$2b$12$S5fCmYolWXn7IVi3hwsXx.dYclDL.xpeuR5PEuKWypSvbrW9TRuS6', '2023-05-27 21:43:31', '2023-05-27 21:43:31', 'actif', 'medecin'),
(27, 'ahmed', 'ahmed', 'M', '2023-05-27', 'ahmed@gmail.com', 555555, 'aaaaaaa', 'ahmed', '$2b$12$AykxZVBtSEXDcoEehp/9jeLWy5IYW42mBYo3WY290UOdsTBNXcroe', '$2b$12$/UW4cCQeiop/V3qjix14ee4hTlEl06HhU5m5UYKHHX1qw2bVQnYaW', '2023-05-27 21:49:22', '2023-05-27 21:49:22', 'actif', 'medecin'),
(28, 'll', 'lll', 'M', '2023-05-27', 'lll@gmail.com', 55555, 'aaaaa', 'llllllllllll', '$2b$12$nx53MEVydR.x7U/3iYji7uDLyjrV5gn/tXr60BLSSvOhqklLLlbM.', '$2b$12$aRcmHIZxZki.I.ulYeY.EuQMOGNipZgezRQqUOZu4lYcyClCHOYwu', '2023-05-27 21:51:05', '2023-05-27 21:51:05', 'actif', 'medecin'),
(30, 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'M', '2023-05-27', 'aaaaaaaa@gmail.com', 2147483647, 'aaaaaaa', 'aaaaaaaaaaaaaaaaa', '$2b$12$JE2fWIFIT7OTREbYNfTlm.zvWvqhWhYh.U9r0j9Qsy6/g/PVoOgdG', '$2b$12$ZvbsyakXI8PsGSaIg8SdVuMb7DwfE40j0Wd6ig7rIpi9B13eKNg1m', '2023-05-27 21:53:11', '2023-05-27 21:53:11', 'actif', 'medecin'),
(34, 'amina', 'amina', 'M', '2023-05-27', 'amina@gmail.com', 6666666, 'Adresse', 'amina', '1234', '1234', '2023-05-27 21:59:04', '2023-06-10 20:14:50', 'actif', 'medecin'),
(36, 'makhlouf', 'kawther', 'F', '2000-01-26', 'kawther@gmail.com', 555555, 'xxxxx', 'kawther', '1234', '1234', '2023-05-27 22:38:31', '2023-06-20 01:27:52', 'actif', 'medecin'),
(37, 'ikhlas', 'ouasti', 'F', '1994-05-28', 'iklas@gmail.com', 55555555, 'xxxxxxxxx', 'ikhlas', '1234', '1234', '2023-05-28 21:21:40', '2023-06-12 23:03:58', 'actif', 'medecin'),
(38, 'ikhlasaa', 'ouasti', 'F', '1994-05-28', 'iklas@gmail.com', 55555555, 'xxxxxxxxx', 'ikhlasaaa', '1234', '1234', '2023-05-28 21:23:35', '2023-05-28 23:34:06', 'actif', 'medecin');

-- --------------------------------------------------------

--
-- Structure de la table `voie`
--

DROP TABLE IF EXISTS `voie`;
CREATE TABLE IF NOT EXISTS `voie` (
  `id_voie` int NOT NULL AUTO_INCREMENT,
  `nom_voie` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_voie`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `voie`
--

INSERT INTO `voie` (`id_voie`, `nom_voie`) VALUES
(1, 'Intraveineuse'),
(2, 'Orale'),
(3, 'Itramusculaire'),
(4, 'Rectale'),
(5, 'Sublinguale'),
(6, 'Sous-cutanée'),
(7, 'Transdermique');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `antecedentchirurgicaux`
--
ALTER TABLE `antecedentchirurgicaux`
  ADD CONSTRAINT `fk_consultation` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `antecedentfamiliaux`
--
ALTER TABLE `antecedentfamiliaux`
  ADD CONSTRAINT `fk2_consultation` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `antecedentmedicaux`
--
ALTER TABLE `antecedentmedicaux`
  ADD CONSTRAINT `fk1_consultation` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `examen_clinique`
--
ALTER TABLE `examen_clinique`
  ADD CONSTRAINT `fk1_examen_clinique` FOREIGN KEY (`id_nom_examen`) REFERENCES `nom_examen` (`id_nom_examen`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_examen_clinique` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `habitudevie`
--
ALTER TABLE `habitudevie`
  ADD CONSTRAINT `fk3_consultation` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `medecin`
--
ALTER TABLE `medecin`
  ADD CONSTRAINT `medecin_ibfk_1` FOREIGN KEY (`id_medecin`) REFERENCES `utilisateur` (`id_utilisateur`),
  ADD CONSTRAINT `medecin_ibfk_2` FOREIGN KEY (`id_grade`) REFERENCES `grade` (`id_grade`),
  ADD CONSTRAINT `medecin_ibfk_3` FOREIGN KEY (`id_unite`) REFERENCES `unite` (`id_unite`),
  ADD CONSTRAINT `medecin_ibfk_4` FOREIGN KEY (`id_specialite`) REFERENCES `specialite` (`id_specialite`);

--
-- Contraintes pour la table `symptome`
--
ALTER TABLE `symptome`
  ADD CONSTRAINT `fk1_gravite_sympthome` FOREIGN KEY (`id_gravite_symptome`) REFERENCES `gravite_sympthome` (`id_gravite_sympthome`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk1_type_symptome` FOREIGN KEY (`id_type_symptome`) REFERENCES `type_symptome` (`id_type_symptome`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk5_consultation` FOREIGN KEY (`id_consultation`) REFERENCES `consultation` (`id_consultation`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
