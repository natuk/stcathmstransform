-- phpMyAdmin SQL Dump
-- version 4.9.5deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 01, 2020 at 11:17 PM
-- Server version: 8.0.20-0ubuntu0.19.10.1
-- PHP Version: 7.3.11-0ubuntu0.19.10.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `catherine-no-lists`
--

-- --------------------------------------------------------

--
-- Table structure for table `1_0_BoxingLeavesDate`
--

CREATE TABLE `1_0_BoxingLeavesDate` (
  `msid` smallint NOT NULL DEFAULT '0',
  `msuuid` varchar(36) DEFAULT NULL,
  `measurementuuid` varchar(36) DEFAULT NULL,
  `height` smallint DEFAULT NULL,
  `heightuuid` varchar(36) DEFAULT NULL,
  `width` smallint DEFAULT NULL,
  `widthuuid` varchar(36) DEFAULT NULL,
  `thickness` smallint DEFAULT NULL,
  `thicknessuuid` varchar(36) DEFAULT NULL,
  `endleaves` smallint DEFAULT NULL,
  `leaves` smallint DEFAULT NULL,
  `boxingstatus` varchar(50) DEFAULT NULL,
  `boxingnotes` varchar(50) DEFAULT NULL,
  `surveyeventuuid` varchar(36) DEFAULT NULL,
  `surveytimespanuuid` varchar(36) DEFAULT NULL,
  `surveydate` datetime DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_00_Surveyors`
--

CREATE TABLE `1_00_Surveyors` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `surveyor` varchar(250) DEFAULT NULL,
  `surveyorrole` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_1_OpeningCharacteristics`
--

CREATE TABLE `1_1_OpeningCharacteristics` (
  `msid` smallint NOT NULL DEFAULT '0',
  `msuuid` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `hollowback` tinyint DEFAULT NULL,
  `measurementuuid` varchar(36) DEFAULT NULL,
  `leftofcentre` tinyint DEFAULT NULL,
  `leftofcentreuuid` varchar(36) DEFAULT NULL,
  `centre` tinyint DEFAULT NULL,
  `centreuuid` varchar(36) DEFAULT NULL,
  `rightofcentre` tinyint DEFAULT NULL,
  `rightofcentreuuid` varchar(36) DEFAULT NULL,
  `rightboard` smallint DEFAULT NULL,
  `rightboarduuid` varchar(36) DEFAULT NULL,
  `leftboard` smallint DEFAULT NULL,
  `leftboarduuid` varchar(36) DEFAULT NULL,
  `closedbook` tinyint DEFAULT NULL,
  `closedbookmeasurementuuid` varchar(36) DEFAULT NULL,
  `closedbookdimensionuuid` varchar(36) DEFAULT NULL,
  `textblockbreaks` tinyint DEFAULT NULL,
  `textblockbreaksmeasurementuuid` varchar(36) DEFAULT NULL,
  `textblockbreaksdimensionuuid` varchar(36) DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_2_PageMarkers`
--

CREATE TABLE `1_2_PageMarkers` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_3_LiftingTabs`
--

CREATE TABLE `1_3_LiftingTabs` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_4_Bookmarks`
--

CREATE TABLE `1_4_Bookmarks` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `1_5_InsertedMaterial`
--

CREATE TABLE `1_5_InsertedMaterial` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesno` varchar(250) DEFAULT NULL,
  `insertedmaterial` varchar(200) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `2_1_TextLeavesMaterial`
--

CREATE TABLE `2_1_TextLeavesMaterial` (
  `msid` smallint NOT NULL DEFAULT '0',
  `composite` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `2_2_TextLeavesCondition`
--

CREATE TABLE `2_2_TextLeavesCondition` (
  `flag` tinyint DEFAULT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `sounddamaged` tinyint NOT NULL DEFAULT '0',
  `thickness` varchar(250) DEFAULT NULL,
  `handle` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `2_3_TextLeavesOldRepairs`
--

CREATE TABLE `2_3_TextLeavesOldRepairs` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesno` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `2_4_TextLeavesNewRepairs`
--

CREATE TABLE `2_4_TextLeavesNewRepairs` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesno` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `4_0_Endleaves`
--

CREATE TABLE `4_0_Endleaves` (
  `id` smallint NOT NULL,
  `flag` tinyint DEFAULT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `leftboard` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `4_1_EndleavesType`
--

CREATE TABLE `4_1_EndleavesType` (
  `endleaves` varchar(250) NOT NULL,
  `attachment` varchar(250) DEFAULT NULL,
  `size` varchar(250) DEFAULT NULL,
  `deckles` tinyint DEFAULT NULL,
  `totalno` tinyint DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `4_2_EndleavesMaterials`
--

CREATE TABLE `4_2_EndleavesMaterials` (
  `endleaves` varchar(250) NOT NULL,
  `leavessameastext` tinyint DEFAULT NULL,
  `endleavesmaterial` varchar(250) DEFAULT NULL,
  `ruled` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL,
  `firstuse` tinyint DEFAULT NULL,
  `ruledsameastext` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `4_3_EndleavesConditions`
--

CREATE TABLE `4_3_EndleavesConditions` (
  `id` smallint NOT NULL,
  `endleaves` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `isadded` tinyint NOT NULL DEFAULT '0',
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `4_4_EndleavesAddedEndleaves`
--

CREATE TABLE `4_4_EndleavesAddedEndleaves` (
  `endleaves` varchar(250) NOT NULL,
  `yesnonk` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_1_SewingNoOfStations`
--

CREATE TABLE `5_1_SewingNoOfStations` (
  `msid` smallint NOT NULL DEFAULT '0',
  `noofstations` tinyint NOT NULL DEFAULT '0',
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_2_SewingGuards`
--

CREATE TABLE `5_2_SewingGuards` (
  `msid` smallint NOT NULL DEFAULT '0',
  `gatherings` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `location` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_3_SewingThread`
--

CREATE TABLE `5_3_SewingThread` (
  `msid` smallint NOT NULL DEFAULT '0',
  `waxed` tinyint DEFAULT NULL,
  `sameasendband` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_4_SewingSupported`
--

CREATE TABLE `5_4_SewingSupported` (
  `msid` smallint NOT NULL DEFAULT '0',
  `supported` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_5_SewingUnsupported`
--

CREATE TABLE `5_5_SewingUnsupported` (
  `msid` smallint NOT NULL DEFAULT '0',
  `unsupport` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_6_SewingSewingSupports`
--

CREATE TABLE `5_6_SewingSewingSupports` (
  `msid` smallint NOT NULL DEFAULT '0',
  `noofstation` tinyint DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_7_SewingSupportRoute`
--

CREATE TABLE `5_7_SewingSupportRoute` (
  `msid` smallint NOT NULL DEFAULT '0',
  `linked` varchar(250) DEFAULT NULL,
  `route` varchar(250) DEFAULT NULL,
  `routescan` varchar(250) DEFAULT NULL,
  `routex` smallint DEFAULT NULL,
  `routey` smallint DEFAULT NULL,
  `routew` smallint DEFAULT NULL,
  `routeh` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_8_SewingStationMeasurements`
--

CREATE TABLE `5_8_SewingStationMeasurements` (
  `msid` smallint NOT NULL DEFAULT '0',
  `firstsewing` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_9_SewingSewingCondition`
--

CREATE TABLE `5_9_SewingSewingCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `existingrepairs` tinyint NOT NULL DEFAULT '0',
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_10_SewingEdgesType`
--

CREATE TABLE `5_10_SewingEdgesType` (
  `msid` smallint NOT NULL DEFAULT '0',
  `type` varchar(250) DEFAULT NULL,
  `retrimmed` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `5_11_SewingEdgeCondition`
--

CREATE TABLE `5_11_SewingEdgeCondition` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `sound` tinyint DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_1_Boards`
--

CREATE TABLE `6_1_Boards` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_2_BoardsAttachment`
--

CREATE TABLE `6_2_BoardsAttachment` (
  `msid` smallint NOT NULL DEFAULT '0',
  `attachment` varchar(250) DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_3_BoardsMaterials`
--

CREATE TABLE `6_3_BoardsMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `boardsmaterial` varchar(250) DEFAULT NULL,
  `composite` tinyint DEFAULT NULL,
  `reused` tinyint DEFAULT NULL,
  `previoususe` varchar(50) DEFAULT NULL,
  `nonoriginal` tinyint DEFAULT NULL,
  `boardsize` varchar(250) DEFAULT NULL,
  `thickness` decimal(3,0) DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL,
  `same` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_4_BoardsEdgeTreatment`
--

CREATE TABLE `6_4_BoardsEdgeTreatment` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_5_BoardsCornerTreatment`
--

CREATE TABLE `6_5_BoardsCornerTreatment` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_6_BoardsSpineEdgeProfile`
--

CREATE TABLE `6_6_BoardsSpineEdgeProfile` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_7_BoardsLining`
--

CREATE TABLE `6_7_BoardsLining` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_8_BoardDamage`
--

CREATE TABLE `6_8_BoardDamage` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_9_a_BoardAttachmentCondition`
--

CREATE TABLE `6_9_a_BoardAttachmentCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `6_9_b_BoardCondition`
--

CREATE TABLE `6_9_b_BoardCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_1_Spine`
--

CREATE TABLE `7_1_Spine` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `adhesivetype` varchar(250) DEFAULT NULL,
  `originalshape` varchar(250) DEFAULT NULL,
  `joints` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_2_SpineJointProfile`
--

CREATE TABLE `7_2_SpineJointProfile` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_3_SpineCondition`
--

CREATE TABLE `7_3_SpineCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `na` tinyint DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_4_SpineLining`
--

CREATE TABLE `7_4_SpineLining` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_5_SpineLiningCondition`
--

CREATE TABLE `7_5_SpineLiningCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_6_SpineEndband`
--

CREATE TABLE `7_6_SpineEndband` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `alternative` tinyint DEFAULT NULL,
  `noofcores` tinyint DEFAULT NULL,
  `nooftiedowns` varchar(250) DEFAULT NULL,
  `secondaryexists` tinyint DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `7_7_SpineEndbandCondition`
--

CREATE TABLE `7_7_SpineEndbandCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `8_1_Covering`
--

CREATE TABLE `8_1_Covering` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `sequence` tinyint NOT NULL DEFAULT '0',
  `capcore` tinyint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `8_2_CoveringTooling`
--

CREATE TABLE `8_2_CoveringTooling` (
  `covering` varchar(250) NOT NULL,
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `8_3_CoveringCondition`
--

CREATE TABLE `8_3_CoveringCondition` (
  `covering` varchar(250) NOT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `8_4_CoveringCondition`
--

CREATE TABLE `8_4_CoveringCondition` (
  `covering` varchar(250) NOT NULL,
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `9_1_FurnitureConstruction`
--

CREATE TABLE `9_1_FurnitureConstruction` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `9_2_FurnitureConstructionDetails`
--

CREATE TABLE `9_2_FurnitureConstructionDetails` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `9_3_FurnitureDrawings`
--

CREATE TABLE `9_3_FurnitureDrawings` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `9_4_FurnitureCondition`
--

CREATE TABLE `9_4_FurnitureCondition` (
  `msid` smallint NOT NULL DEFAULT '0',
  `flag` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `10_1_NotesReexamination`
--

CREATE TABLE `10_1_NotesReexamination` (
  `msid` smallint NOT NULL DEFAULT '0',
  `reexamination` varchar(200) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `10_3_NotesRepairs`
--

CREATE TABLE `10_3_NotesRepairs` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesnonk` varchar(250) DEFAULT NULL,
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `10_4_NotesRandom`
--

CREATE TABLE `10_4_NotesRandom` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0',
  `flag` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `10_5_NoteClass`
--

CREATE TABLE `10_5_NoteClass` (
  `id` int NOT NULL,
  `msid` int NOT NULL DEFAULT '0',
  `section` varchar(50) NOT NULL DEFAULT '',
  `type` varchar(20) NOT NULL DEFAULT '',
  `notes` varchar(200) NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Bibliographic`
--

CREATE TABLE `Bibliographic` (
  `msid` smallint NOT NULL DEFAULT '0',
  `century` tinyint DEFAULT NULL,
  `note` text,
  `kamil` varchar(50) DEFAULT NULL,
  `author` varchar(120) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `title` varchar(130) DEFAULT NULL,
  `dated` varchar(50) DEFAULT NULL,
  `gardthausen` smallint DEFAULT NULL,
  `atiya` varchar(50) DEFAULT NULL,
  `weizmann` smallint DEFAULT NULL,
  `provenance` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsBoardAttachmentConditionAdditionals`
--

CREATE TABLE `BoardsBoardAttachmentConditionAdditionals` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `repaired` tinyint DEFAULT NULL,
  `stiffness` tinyint DEFAULT NULL,
  `replacementboards` tinyint DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsBoardAttachmentConditionAttachments`
--

CREATE TABLE `BoardsBoardAttachmentConditionAttachments` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `attachmenttype` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `severity` tinyint DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsBoardConditionAdditionals`
--

CREATE TABLE `BoardsBoardConditionAdditionals` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `leftboard` tinyint NOT NULL DEFAULT '0',
  `oldrepair` tinyint DEFAULT NULL,
  `sound` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsBoardConditionConditions`
--

CREATE TABLE `BoardsBoardConditionConditions` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `severity` tinyint DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsCornerTreatments`
--

CREATE TABLE `BoardsCornerTreatments` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `groove` varchar(250) DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsEdgeTreatmentBevels`
--

CREATE TABLE `BoardsEdgeTreatmentBevels` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `bevel` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsEdgeTreatmentGrooves`
--

CREATE TABLE `BoardsEdgeTreatmentGrooves` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `groove` varchar(250) DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningMaterials`
--

CREATE TABLE `BoardsLiningMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `material` varchar(250) DEFAULT NULL,
  `colour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningPaperBurnished`
--

CREATE TABLE `BoardsLiningPaperBurnished` (
  `liningmaterial` varchar(250) NOT NULL,
  `burnished` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningPaperOrigins`
--

CREATE TABLE `BoardsLiningPaperOrigins` (
  `id` smallint NOT NULL,
  `liningmaterial` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningPaperTypes`
--

CREATE TABLE `BoardsLiningPaperTypes` (
  `id` smallint NOT NULL,
  `liningmaterial` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningParchmentTypes`
--

CREATE TABLE `BoardsLiningParchmentTypes` (
  `id` smallint NOT NULL,
  `liningmaterial` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningScripts`
--

CREATE TABLE `BoardsLiningScripts` (
  `id` smallint NOT NULL,
  `liningmaterial` varchar(250) DEFAULT NULL,
  `script` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsLiningTextileDecorations`
--

CREATE TABLE `BoardsLiningTextileDecorations` (
  `id` smallint NOT NULL,
  `liningmaterial` varchar(250) DEFAULT NULL,
  `decoration` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsMaterialMaterialPapers`
--

CREATE TABLE `BoardsMaterialMaterialPapers` (
  `id` smallint NOT NULL,
  `materialid` varchar(250) DEFAULT NULL,
  `formation` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BoardsMaterialMaterialWoods`
--

CREATE TABLE `BoardsMaterialMaterialWoods` (
  `id` smallint NOT NULL,
  `material` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  `grain` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BookmarkColours`
--

CREATE TABLE `BookmarkColours` (
  `id` smallint NOT NULL,
  `bookmarkid` varchar(250) DEFAULT NULL,
  `bookmarkcolour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `BookmarkMaterials`
--

CREATE TABLE `BookmarkMaterials` (
  `id` smallint NOT NULL,
  `bookmarkid` varchar(250) DEFAULT NULL,
  `bookmarkmaterial` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Bookmarks`
--

CREATE TABLE `Bookmarks` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `type` varchar(250) DEFAULT NULL,
  `primarytype` varchar(250) DEFAULT NULL,
  `secondarytype` varchar(250) DEFAULT NULL,
  `primaryattachmenttype` varchar(250) DEFAULT NULL,
  `decorationtype` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ColourCharts`
--

CREATE TABLE `ColourCharts` (
  `filmroll` int NOT NULL DEFAULT '0',
  `scan` varchar(100) DEFAULT NULL,
  `xmlmetadata` longtext
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringAdditionalConditions`
--

CREATE TABLE `CoveringAdditionalConditions` (
  `id` smallint NOT NULL,
  `coveringid` varchar(250) DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringColours`
--

CREATE TABLE `CoveringColours` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `colour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringConditions`
--

CREATE TABLE `CoveringConditions` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringCorners`
--

CREATE TABLE `CoveringCorners` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `corner` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringMaterials`
--

CREATE TABLE `CoveringMaterials` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `hairsideout` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringRepairs`
--

CREATE TABLE `CoveringRepairs` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `repair` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringSources`
--

CREATE TABLE `CoveringSources` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `source` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringStatuses`
--

CREATE TABLE `CoveringStatuses` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringToolingDrawing`
--

CREATE TABLE `CoveringToolingDrawing` (
  `covering` varchar(250) NOT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringToolingRubbingQualities`
--

CREATE TABLE `CoveringToolingRubbingQualities` (
  `covering` varchar(250) NOT NULL,
  `rubbingquality` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringToolingTools`
--

CREATE TABLE `CoveringToolingTools` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `tool` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringToolingTypes`
--

CREATE TABLE `CoveringToolingTypes` (
  `id` smallint NOT NULL,
  `covering` varchar(250) DEFAULT NULL,
  `toolingtype` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringToolNumbers`
--

CREATE TABLE `CoveringToolNumbers` (
  `covering` varchar(250) NOT NULL,
  `noofrolls` tinyint DEFAULT NULL,
  `noofsmalltools` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `CoveringTypes`
--

CREATE TABLE `CoveringTypes` (
  `covering` varchar(250) NOT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `EndleavesAddedEndleavesPaperDetails`
--

CREATE TABLE `EndleavesAddedEndleavesPaperDetails` (
  `id` smallint NOT NULL,
  `papertype` varchar(250) DEFAULT NULL,
  `burnished` tinyint DEFAULT NULL,
  `endleaves` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `EndleavesMaterialsPaperDetails`
--

CREATE TABLE `EndleavesMaterialsPaperDetails` (
  `id` smallint NOT NULL,
  `endleaves` varchar(250) DEFAULT NULL,
  `papertype` varchar(250) DEFAULT NULL,
  `watermark` tinyint DEFAULT NULL,
  `polished` varchar(250) DEFAULT NULL,
  `decoratedpaper` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `EndleavesMaterialsRuling`
--

CREATE TABLE `EndleavesMaterialsRuling` (
  `id` smallint NOT NULL,
  `endleaves` varchar(250) DEFAULT NULL,
  `rulingtype` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `EndleavesMaterialWasteTypes`
--

CREATE TABLE `EndleavesMaterialWasteTypes` (
  `id` smallint NOT NULL,
  `endleaves` varchar(250) DEFAULT NULL,
  `wastetype` varchar(250) DEFAULT NULL,
  `wastescript` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConditions`
--

CREATE TABLE `FurnitureConditions` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `fastening` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionCatchplateDetails`
--

CREATE TABLE `FurnitureConstructionCatchplateDetails` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `catchplatedetail` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionClaspDetails`
--

CREATE TABLE `FurnitureConstructionClaspDetails` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `claspdetail` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionMaterials`
--

CREATE TABLE `FurnitureConstructionMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `material` varchar(250) DEFAULT NULL,
  `fastening` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionProcesses`
--

CREATE TABLE `FurnitureConstructionProcesses` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `process` varchar(250) DEFAULT NULL,
  `fastening` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionStrapFormations`
--

CREATE TABLE `FurnitureConstructionStrapFormations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `strapformation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionStrapLocations`
--

CREATE TABLE `FurnitureConstructionStrapLocations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `straplocation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionStrapMaterials`
--

CREATE TABLE `FurnitureConstructionStrapMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `strapmaterial` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionTieColours`
--

CREATE TABLE `FurnitureConstructionTieColours` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `tiecolour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureConstructionTieMaterials`
--

CREATE TABLE `FurnitureConstructionTieMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `tiematerial` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureDrawingsBosses`
--

CREATE TABLE `FurnitureDrawingsBosses` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureDrawingsLocations`
--

CREATE TABLE `FurnitureDrawingsLocations` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FurnitureDrawingsPins`
--

CREATE TABLE `FurnitureDrawingsPins` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `LiftingTabs`
--

CREATE TABLE `LiftingTabs` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `location` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `attachment` varchar(250) DEFAULT NULL,
  `turnin` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `LiftingTabsCondition`
--

CREATE TABLE `LiftingTabsCondition` (
  `id` smallint NOT NULL,
  `liftingtabid` varchar(250) DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `leftboard` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `MSs`
--

CREATE TABLE `MSs` (
  `id` smallint NOT NULL DEFAULT '0',
  `msuuid` varchar(36) DEFAULT NULL,
  `collection` varchar(250) DEFAULT NULL,
  `collectionuuid` varchar(36) DEFAULT NULL,
  `msno` smallint DEFAULT NULL,
  `cataloguename` varchar(30) NOT NULL DEFAULT '',
  `cataloguenameuuid` varchar(36) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `NotesEdgeDecorations`
--

CREATE TABLE `NotesEdgeDecorations` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `NotesRepairs`
--

CREATE TABLE `NotesRepairs` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `repair` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `NotesTitling`
--

CREATE TABLE `NotesTitling` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PageMarkers`
--

CREATE TABLE `PageMarkers` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `type` varchar(250) DEFAULT NULL,
  `attachment` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `scanid` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PageMarkersColour`
--

CREATE TABLE `PageMarkersColour` (
  `id` smallint NOT NULL,
  `pagemarker` varchar(250) DEFAULT NULL,
  `pagemarkercolour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PageMarkersCondition`
--

CREATE TABLE `PageMarkersCondition` (
  `id` smallint NOT NULL,
  `pagemarker` varchar(250) DEFAULT NULL,
  `condition` varchar(250) DEFAULT NULL,
  `conditionno` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PageMarkersLocation`
--

CREATE TABLE `PageMarkersLocation` (
  `id` smallint NOT NULL,
  `pagemarker` varchar(250) DEFAULT NULL,
  `pagemarkerlocation` varchar(250) DEFAULT NULL,
  `locationno` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Rubbings`
--

CREATE TABLE `Rubbings` (
  `id` smallint NOT NULL,
  `msid` smallint DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `rubinms` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Scans`
--

CREATE TABLE `Scans` (
  `id` int NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `pageno` varchar(3) NOT NULL DEFAULT '',
  `scan` varchar(100) NOT NULL DEFAULT '',
  `ispage` tinyint DEFAULT NULL,
  `isslide` tinyint DEFAULT NULL,
  `isrubbing` tinyint DEFAULT NULL,
  `xmlmetadata` longtext,
  `caption` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingEdgesColours`
--

CREATE TABLE `SewingEdgesColours` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `colour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingEdgesDecorations`
--

CREATE TABLE `SewingEdgesDecorations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `decoration` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingEdgesMethods`
--

CREATE TABLE `SewingEdgesMethods` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `method` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingPreparations`
--

CREATE TABLE `SewingPreparations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `preparation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingSewingConditionStructure`
--

CREATE TABLE `SewingSewingConditionStructure` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingSewingConditionThread`
--

CREATE TABLE `SewingSewingConditionThread` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingSupportsFormations`
--

CREATE TABLE `SewingSupportsFormations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `formation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingSupportsMaterials`
--

CREATE TABLE `SewingSupportsMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `material` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadColours`
--

CREATE TABLE `SewingThreadColours` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `colour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadMaterials`
--

CREATE TABLE `SewingThreadMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `material` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadPlys`
--

CREATE TABLE `SewingThreadPlys` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `ply` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadThicknesses`
--

CREATE TABLE `SewingThreadThicknesses` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `thickness` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadTwists`
--

CREATE TABLE `SewingThreadTwists` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `twist` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SewingThreadTypes`
--

CREATE TABLE `SewingThreadTypes` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandBoardAttachments`
--

CREATE TABLE `SpineEndbandBoardAttachments` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `boardattchment` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandColours`
--

CREATE TABLE `SpineEndbandColours` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `colour` varchar(250) DEFAULT NULL,
  `secondary` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandConditions`
--

CREATE TABLE `SpineEndbandConditions` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `head` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandConditionsAtBoard`
--

CREATE TABLE `SpineEndbandConditionsAtBoard` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL,
  `head` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandCoreMaterials`
--

CREATE TABLE `SpineEndbandCoreMaterials` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandDrawings`
--

CREATE TABLE `SpineEndbandDrawings` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL,
  `secondary` tinyint DEFAULT NULL,
  `front` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandMaterials`
--

CREATE TABLE `SpineEndbandMaterials` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `secondary` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandSewingRoutes`
--

CREATE TABLE `SpineEndbandSewingRoutes` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `sewingroute` varchar(250) DEFAULT NULL,
  `secondary` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineEndbandTypes`
--

CREATE TABLE `SpineEndbandTypes` (
  `id` smallint NOT NULL,
  `endband` varchar(250) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineLiningConditionAtBoards`
--

CREATE TABLE `SpineLiningConditionAtBoards` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `leftboard` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineLiningConditions`
--

CREATE TABLE `SpineLiningConditions` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `severity` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineLiningDrawings`
--

CREATE TABLE `SpineLiningDrawings` (
  `msid` smallint NOT NULL DEFAULT '0',
  `scanid` int DEFAULT NULL,
  `x` smallint DEFAULT NULL,
  `y` smallint DEFAULT NULL,
  `w` smallint DEFAULT NULL,
  `h` smallint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineLinings`
--

CREATE TABLE `SpineLinings` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `layersequence` tinyint DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  `location` varchar(250) DEFAULT NULL,
  `material` varchar(250) DEFAULT NULL,
  `materialtype` varchar(250) DEFAULT NULL,
  `liningjoints` varchar(250) DEFAULT NULL,
  `colour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineSpineConditionAdhesives`
--

CREATE TABLE `SpineSpineConditionAdhesives` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `condition` varchar(250) DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL,
  `extent` tinyint DEFAULT NULL,
  `severity` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpineSpineConditionExtraApplications`
--

CREATE TABLE `SpineSpineConditionExtraApplications` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `adhesive` varchar(250) DEFAULT NULL,
  `extent` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesConditionDepositText`
--

CREATE TABLE `TextLeavesConditionDepositText` (
  `msid` smallint NOT NULL DEFAULT '0',
  `depositetext` varchar(60) NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesConditionLostRemovedQuiresText`
--

CREATE TABLE `TextLeavesConditionLostRemovedQuiresText` (
  `msid` smallint NOT NULL DEFAULT '0',
  `yesno` varchar(250) DEFAULT NULL,
  `quiretext` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesConditions`
--

CREATE TABLE `TextLeavesConditions` (
  `msid` smallint NOT NULL DEFAULT '0',
  `id` int NOT NULL,
  `textleavescondition` varchar(250) DEFAULT NULL,
  `extendstart` tinyint DEFAULT NULL,
  `extendend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL,
  `marginal` tinyint DEFAULT NULL,
  `textarea` tinyint DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `emergency` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesMaterialColours`
--

CREATE TABLE `TextLeavesMaterialColours` (
  `id` smallint NOT NULL,
  `textleavesmaterial` varchar(250) DEFAULT NULL,
  `textleavesmaterialcolour` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesMaterials`
--

CREATE TABLE `TextLeavesMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `height` smallint DEFAULT NULL,
  `width` smallint DEFAULT NULL,
  `textleavesmaterial` varchar(250) DEFAULT NULL,
  `ruledyesno` tinyint DEFAULT NULL,
  `pph` smallint DEFAULT NULL,
  `ppw` smallint DEFAULT NULL,
  `ppy` smallint DEFAULT NULL,
  `ppx` smallint DEFAULT NULL,
  `ppscan` varchar(250) DEFAULT NULL,
  `paperwatermark` tinyint DEFAULT NULL,
  `paperburnishedlocation` varchar(250) DEFAULT NULL,
  `paperburnished` tinyint DEFAULT NULL,
  `papertype` varchar(250) DEFAULT NULL,
  `parchmentarrangement` varchar(250) DEFAULT NULL,
  `parchmentanimal` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesMaterialsRuling`
--

CREATE TABLE `TextLeavesMaterialsRuling` (
  `id` smallint NOT NULL,
  `textleavesmaterial` varchar(250) DEFAULT NULL,
  `rulingtype` varchar(250) DEFAULT NULL,
  `rulinglocation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesMaterialsRulingTool`
--

CREATE TABLE `TextLeavesMaterialsRulingTool` (
  `id` smallint NOT NULL,
  `textleaves` varchar(250) DEFAULT NULL,
  `scanid` int NOT NULL DEFAULT '0',
  `x` smallint NOT NULL DEFAULT '0',
  `y` smallint NOT NULL DEFAULT '0',
  `w` smallint NOT NULL DEFAULT '0',
  `h` smallint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesNewRepairsLocation`
--

CREATE TABLE `TextLeavesNewRepairsLocation` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `newrepairslocation` varchar(250) DEFAULT NULL,
  `newrepairsmaterial` varchar(250) DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL,
  `emergency` tinyint NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesNewRepairsType`
--

CREATE TABLE `TextLeavesNewRepairsType` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `newrepairstype` varchar(250) DEFAULT NULL,
  `newrepairsmaterial` varchar(250) DEFAULT NULL,
  `extentstart` tinyint DEFAULT NULL,
  `extentend` tinyint DEFAULT NULL,
  `severitystart` tinyint DEFAULT NULL,
  `severityend` tinyint DEFAULT NULL,
  `emergency` tinyint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesOldRepairsLocations`
--

CREATE TABLE `TextLeavesOldRepairsLocations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `oldrepairslocation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesOldRepairsMaterials`
--

CREATE TABLE `TextLeavesOldRepairsMaterials` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `oldrepairmaterial` varchar(250) DEFAULT NULL,
  `oldrepairtype` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesOldRepairsOvercastingLocations`
--

CREATE TABLE `TextLeavesOldRepairsOvercastingLocations` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `overcastinglocation` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `TextLeavesOldRepairsTechniques`
--

CREATE TABLE `TextLeavesOldRepairsTechniques` (
  `id` smallint NOT NULL,
  `msid` smallint NOT NULL DEFAULT '0',
  `oldrepairstechnique` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `1_0_BoxingLeavesDate`
--
ALTER TABLE `1_0_BoxingLeavesDate`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `1_00_Surveyors`
--
ALTER TABLE `1_00_Surveyors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `1_1_OpeningCharacteristics`
--
ALTER TABLE `1_1_OpeningCharacteristics`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `1_2_PageMarkers`
--
ALTER TABLE `1_2_PageMarkers`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `1_3_LiftingTabs`
--
ALTER TABLE `1_3_LiftingTabs`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `1_4_Bookmarks`
--
ALTER TABLE `1_4_Bookmarks`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `1_5_InsertedMaterial`
--
ALTER TABLE `1_5_InsertedMaterial`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `2_1_TextLeavesMaterial`
--
ALTER TABLE `2_1_TextLeavesMaterial`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `2_2_TextLeavesCondition`
--
ALTER TABLE `2_2_TextLeavesCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `2_3_TextLeavesOldRepairs`
--
ALTER TABLE `2_3_TextLeavesOldRepairs`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `2_4_TextLeavesNewRepairs`
--
ALTER TABLE `2_4_TextLeavesNewRepairs`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `4_0_Endleaves`
--
ALTER TABLE `4_0_Endleaves`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `4_1_EndleavesType`
--
ALTER TABLE `4_1_EndleavesType`
  ADD PRIMARY KEY (`endleaves`);

--
-- Indexes for table `4_2_EndleavesMaterials`
--
ALTER TABLE `4_2_EndleavesMaterials`
  ADD PRIMARY KEY (`endleaves`);

--
-- Indexes for table `4_3_EndleavesConditions`
--
ALTER TABLE `4_3_EndleavesConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `4_4_EndleavesAddedEndleaves`
--
ALTER TABLE `4_4_EndleavesAddedEndleaves`
  ADD PRIMARY KEY (`endleaves`);

--
-- Indexes for table `5_1_SewingNoOfStations`
--
ALTER TABLE `5_1_SewingNoOfStations`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_2_SewingGuards`
--
ALTER TABLE `5_2_SewingGuards`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_3_SewingThread`
--
ALTER TABLE `5_3_SewingThread`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_4_SewingSupported`
--
ALTER TABLE `5_4_SewingSupported`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_5_SewingUnsupported`
--
ALTER TABLE `5_5_SewingUnsupported`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_6_SewingSewingSupports`
--
ALTER TABLE `5_6_SewingSewingSupports`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_7_SewingSupportRoute`
--
ALTER TABLE `5_7_SewingSupportRoute`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_8_SewingStationMeasurements`
--
ALTER TABLE `5_8_SewingStationMeasurements`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_9_SewingSewingCondition`
--
ALTER TABLE `5_9_SewingSewingCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_10_SewingEdgesType`
--
ALTER TABLE `5_10_SewingEdgesType`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `5_11_SewingEdgeCondition`
--
ALTER TABLE `5_11_SewingEdgeCondition`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `6_1_Boards`
--
ALTER TABLE `6_1_Boards`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_2_BoardsAttachment`
--
ALTER TABLE `6_2_BoardsAttachment`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_3_BoardsMaterials`
--
ALTER TABLE `6_3_BoardsMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `6_4_BoardsEdgeTreatment`
--
ALTER TABLE `6_4_BoardsEdgeTreatment`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_5_BoardsCornerTreatment`
--
ALTER TABLE `6_5_BoardsCornerTreatment`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_6_BoardsSpineEdgeProfile`
--
ALTER TABLE `6_6_BoardsSpineEdgeProfile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `6_7_BoardsLining`
--
ALTER TABLE `6_7_BoardsLining`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_8_BoardDamage`
--
ALTER TABLE `6_8_BoardDamage`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_9_a_BoardAttachmentCondition`
--
ALTER TABLE `6_9_a_BoardAttachmentCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `6_9_b_BoardCondition`
--
ALTER TABLE `6_9_b_BoardCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_1_Spine`
--
ALTER TABLE `7_1_Spine`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_2_SpineJointProfile`
--
ALTER TABLE `7_2_SpineJointProfile`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_3_SpineCondition`
--
ALTER TABLE `7_3_SpineCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_4_SpineLining`
--
ALTER TABLE `7_4_SpineLining`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_5_SpineLiningCondition`
--
ALTER TABLE `7_5_SpineLiningCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `7_6_SpineEndband`
--
ALTER TABLE `7_6_SpineEndband`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `7_7_SpineEndbandCondition`
--
ALTER TABLE `7_7_SpineEndbandCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `8_1_Covering`
--
ALTER TABLE `8_1_Covering`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `8_2_CoveringTooling`
--
ALTER TABLE `8_2_CoveringTooling`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `8_3_CoveringCondition`
--
ALTER TABLE `8_3_CoveringCondition`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `8_4_CoveringCondition`
--
ALTER TABLE `8_4_CoveringCondition`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `9_1_FurnitureConstruction`
--
ALTER TABLE `9_1_FurnitureConstruction`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `9_2_FurnitureConstructionDetails`
--
ALTER TABLE `9_2_FurnitureConstructionDetails`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `9_3_FurnitureDrawings`
--
ALTER TABLE `9_3_FurnitureDrawings`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `9_4_FurnitureCondition`
--
ALTER TABLE `9_4_FurnitureCondition`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `10_1_NotesReexamination`
--
ALTER TABLE `10_1_NotesReexamination`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `10_3_NotesRepairs`
--
ALTER TABLE `10_3_NotesRepairs`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `10_4_NotesRandom`
--
ALTER TABLE `10_4_NotesRandom`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `10_5_NoteClass`
--
ALTER TABLE `10_5_NoteClass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Bibliographic`
--
ALTER TABLE `Bibliographic`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `BoardsBoardAttachmentConditionAdditionals`
--
ALTER TABLE `BoardsBoardAttachmentConditionAdditionals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsBoardAttachmentConditionAttachments`
--
ALTER TABLE `BoardsBoardAttachmentConditionAttachments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsBoardConditionAdditionals`
--
ALTER TABLE `BoardsBoardConditionAdditionals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsBoardConditionConditions`
--
ALTER TABLE `BoardsBoardConditionConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsCornerTreatments`
--
ALTER TABLE `BoardsCornerTreatments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsEdgeTreatmentBevels`
--
ALTER TABLE `BoardsEdgeTreatmentBevels`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsEdgeTreatmentGrooves`
--
ALTER TABLE `BoardsEdgeTreatmentGrooves`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningMaterials`
--
ALTER TABLE `BoardsLiningMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningPaperBurnished`
--
ALTER TABLE `BoardsLiningPaperBurnished`
  ADD PRIMARY KEY (`liningmaterial`);

--
-- Indexes for table `BoardsLiningPaperOrigins`
--
ALTER TABLE `BoardsLiningPaperOrigins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningPaperTypes`
--
ALTER TABLE `BoardsLiningPaperTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningParchmentTypes`
--
ALTER TABLE `BoardsLiningParchmentTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningScripts`
--
ALTER TABLE `BoardsLiningScripts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsLiningTextileDecorations`
--
ALTER TABLE `BoardsLiningTextileDecorations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsMaterialMaterialPapers`
--
ALTER TABLE `BoardsMaterialMaterialPapers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BoardsMaterialMaterialWoods`
--
ALTER TABLE `BoardsMaterialMaterialWoods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BookmarkColours`
--
ALTER TABLE `BookmarkColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BookmarkMaterials`
--
ALTER TABLE `BookmarkMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Bookmarks`
--
ALTER TABLE `Bookmarks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ColourCharts`
--
ALTER TABLE `ColourCharts`
  ADD PRIMARY KEY (`filmroll`);

--
-- Indexes for table `CoveringAdditionalConditions`
--
ALTER TABLE `CoveringAdditionalConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringColours`
--
ALTER TABLE `CoveringColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringConditions`
--
ALTER TABLE `CoveringConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringCorners`
--
ALTER TABLE `CoveringCorners`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringMaterials`
--
ALTER TABLE `CoveringMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringRepairs`
--
ALTER TABLE `CoveringRepairs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringSources`
--
ALTER TABLE `CoveringSources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringStatuses`
--
ALTER TABLE `CoveringStatuses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringToolingDrawing`
--
ALTER TABLE `CoveringToolingDrawing`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `CoveringToolingRubbingQualities`
--
ALTER TABLE `CoveringToolingRubbingQualities`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `CoveringToolingTools`
--
ALTER TABLE `CoveringToolingTools`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringToolingTypes`
--
ALTER TABLE `CoveringToolingTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CoveringToolNumbers`
--
ALTER TABLE `CoveringToolNumbers`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `CoveringTypes`
--
ALTER TABLE `CoveringTypes`
  ADD PRIMARY KEY (`covering`);

--
-- Indexes for table `EndleavesAddedEndleavesPaperDetails`
--
ALTER TABLE `EndleavesAddedEndleavesPaperDetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `EndleavesMaterialsPaperDetails`
--
ALTER TABLE `EndleavesMaterialsPaperDetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `EndleavesMaterialsRuling`
--
ALTER TABLE `EndleavesMaterialsRuling`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `EndleavesMaterialWasteTypes`
--
ALTER TABLE `EndleavesMaterialWasteTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConditions`
--
ALTER TABLE `FurnitureConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionCatchplateDetails`
--
ALTER TABLE `FurnitureConstructionCatchplateDetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionClaspDetails`
--
ALTER TABLE `FurnitureConstructionClaspDetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionMaterials`
--
ALTER TABLE `FurnitureConstructionMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionProcesses`
--
ALTER TABLE `FurnitureConstructionProcesses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionStrapFormations`
--
ALTER TABLE `FurnitureConstructionStrapFormations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionStrapLocations`
--
ALTER TABLE `FurnitureConstructionStrapLocations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionStrapMaterials`
--
ALTER TABLE `FurnitureConstructionStrapMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionTieColours`
--
ALTER TABLE `FurnitureConstructionTieColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureConstructionTieMaterials`
--
ALTER TABLE `FurnitureConstructionTieMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FurnitureDrawingsBosses`
--
ALTER TABLE `FurnitureDrawingsBosses`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `FurnitureDrawingsLocations`
--
ALTER TABLE `FurnitureDrawingsLocations`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `FurnitureDrawingsPins`
--
ALTER TABLE `FurnitureDrawingsPins`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `LiftingTabs`
--
ALTER TABLE `LiftingTabs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `LiftingTabsCondition`
--
ALTER TABLE `LiftingTabsCondition`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `MSs`
--
ALTER TABLE `MSs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `NotesEdgeDecorations`
--
ALTER TABLE `NotesEdgeDecorations`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `NotesRepairs`
--
ALTER TABLE `NotesRepairs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `NotesTitling`
--
ALTER TABLE `NotesTitling`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `PageMarkers`
--
ALTER TABLE `PageMarkers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PageMarkersColour`
--
ALTER TABLE `PageMarkersColour`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PageMarkersCondition`
--
ALTER TABLE `PageMarkersCondition`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PageMarkersLocation`
--
ALTER TABLE `PageMarkersLocation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Rubbings`
--
ALTER TABLE `Rubbings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Scans`
--
ALTER TABLE `Scans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingEdgesColours`
--
ALTER TABLE `SewingEdgesColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingEdgesDecorations`
--
ALTER TABLE `SewingEdgesDecorations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingEdgesMethods`
--
ALTER TABLE `SewingEdgesMethods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingPreparations`
--
ALTER TABLE `SewingPreparations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingSewingConditionStructure`
--
ALTER TABLE `SewingSewingConditionStructure`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingSewingConditionThread`
--
ALTER TABLE `SewingSewingConditionThread`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingSupportsFormations`
--
ALTER TABLE `SewingSupportsFormations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingSupportsMaterials`
--
ALTER TABLE `SewingSupportsMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadColours`
--
ALTER TABLE `SewingThreadColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadMaterials`
--
ALTER TABLE `SewingThreadMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadPlys`
--
ALTER TABLE `SewingThreadPlys`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadThicknesses`
--
ALTER TABLE `SewingThreadThicknesses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadTwists`
--
ALTER TABLE `SewingThreadTwists`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SewingThreadTypes`
--
ALTER TABLE `SewingThreadTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandBoardAttachments`
--
ALTER TABLE `SpineEndbandBoardAttachments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandColours`
--
ALTER TABLE `SpineEndbandColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandConditions`
--
ALTER TABLE `SpineEndbandConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandConditionsAtBoard`
--
ALTER TABLE `SpineEndbandConditionsAtBoard`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandCoreMaterials`
--
ALTER TABLE `SpineEndbandCoreMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandDrawings`
--
ALTER TABLE `SpineEndbandDrawings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandMaterials`
--
ALTER TABLE `SpineEndbandMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandSewingRoutes`
--
ALTER TABLE `SpineEndbandSewingRoutes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineEndbandTypes`
--
ALTER TABLE `SpineEndbandTypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineLiningConditionAtBoards`
--
ALTER TABLE `SpineLiningConditionAtBoards`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineLiningConditions`
--
ALTER TABLE `SpineLiningConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineLiningDrawings`
--
ALTER TABLE `SpineLiningDrawings`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `SpineLinings`
--
ALTER TABLE `SpineLinings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineSpineConditionAdhesives`
--
ALTER TABLE `SpineSpineConditionAdhesives`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SpineSpineConditionExtraApplications`
--
ALTER TABLE `SpineSpineConditionExtraApplications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesConditionDepositText`
--
ALTER TABLE `TextLeavesConditionDepositText`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `TextLeavesConditionLostRemovedQuiresText`
--
ALTER TABLE `TextLeavesConditionLostRemovedQuiresText`
  ADD PRIMARY KEY (`msid`);

--
-- Indexes for table `TextLeavesConditions`
--
ALTER TABLE `TextLeavesConditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesMaterialColours`
--
ALTER TABLE `TextLeavesMaterialColours`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesMaterials`
--
ALTER TABLE `TextLeavesMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesMaterialsRuling`
--
ALTER TABLE `TextLeavesMaterialsRuling`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesMaterialsRulingTool`
--
ALTER TABLE `TextLeavesMaterialsRulingTool`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesNewRepairsLocation`
--
ALTER TABLE `TextLeavesNewRepairsLocation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesNewRepairsType`
--
ALTER TABLE `TextLeavesNewRepairsType`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesOldRepairsLocations`
--
ALTER TABLE `TextLeavesOldRepairsLocations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesOldRepairsMaterials`
--
ALTER TABLE `TextLeavesOldRepairsMaterials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesOldRepairsOvercastingLocations`
--
ALTER TABLE `TextLeavesOldRepairsOvercastingLocations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `TextLeavesOldRepairsTechniques`
--
ALTER TABLE `TextLeavesOldRepairsTechniques`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `1_00_Surveyors`
--
ALTER TABLE `1_00_Surveyors`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `4_0_Endleaves`
--
ALTER TABLE `4_0_Endleaves`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `4_3_EndleavesConditions`
--
ALTER TABLE `4_3_EndleavesConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `5_11_SewingEdgeCondition`
--
ALTER TABLE `5_11_SewingEdgeCondition`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `6_3_BoardsMaterials`
--
ALTER TABLE `6_3_BoardsMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `6_6_BoardsSpineEdgeProfile`
--
ALTER TABLE `6_6_BoardsSpineEdgeProfile`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `7_6_SpineEndband`
--
ALTER TABLE `7_6_SpineEndband`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `8_1_Covering`
--
ALTER TABLE `8_1_Covering`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `10_5_NoteClass`
--
ALTER TABLE `10_5_NoteClass`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsBoardAttachmentConditionAdditionals`
--
ALTER TABLE `BoardsBoardAttachmentConditionAdditionals`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsBoardAttachmentConditionAttachments`
--
ALTER TABLE `BoardsBoardAttachmentConditionAttachments`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsBoardConditionAdditionals`
--
ALTER TABLE `BoardsBoardConditionAdditionals`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsBoardConditionConditions`
--
ALTER TABLE `BoardsBoardConditionConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsCornerTreatments`
--
ALTER TABLE `BoardsCornerTreatments`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsEdgeTreatmentBevels`
--
ALTER TABLE `BoardsEdgeTreatmentBevels`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsEdgeTreatmentGrooves`
--
ALTER TABLE `BoardsEdgeTreatmentGrooves`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningMaterials`
--
ALTER TABLE `BoardsLiningMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningPaperOrigins`
--
ALTER TABLE `BoardsLiningPaperOrigins`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningPaperTypes`
--
ALTER TABLE `BoardsLiningPaperTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningParchmentTypes`
--
ALTER TABLE `BoardsLiningParchmentTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningScripts`
--
ALTER TABLE `BoardsLiningScripts`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsLiningTextileDecorations`
--
ALTER TABLE `BoardsLiningTextileDecorations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsMaterialMaterialPapers`
--
ALTER TABLE `BoardsMaterialMaterialPapers`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BoardsMaterialMaterialWoods`
--
ALTER TABLE `BoardsMaterialMaterialWoods`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BookmarkColours`
--
ALTER TABLE `BookmarkColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BookmarkMaterials`
--
ALTER TABLE `BookmarkMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Bookmarks`
--
ALTER TABLE `Bookmarks`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringAdditionalConditions`
--
ALTER TABLE `CoveringAdditionalConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringColours`
--
ALTER TABLE `CoveringColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringConditions`
--
ALTER TABLE `CoveringConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringCorners`
--
ALTER TABLE `CoveringCorners`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringMaterials`
--
ALTER TABLE `CoveringMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringRepairs`
--
ALTER TABLE `CoveringRepairs`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringSources`
--
ALTER TABLE `CoveringSources`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringStatuses`
--
ALTER TABLE `CoveringStatuses`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringToolingTools`
--
ALTER TABLE `CoveringToolingTools`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CoveringToolingTypes`
--
ALTER TABLE `CoveringToolingTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EndleavesAddedEndleavesPaperDetails`
--
ALTER TABLE `EndleavesAddedEndleavesPaperDetails`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EndleavesMaterialsPaperDetails`
--
ALTER TABLE `EndleavesMaterialsPaperDetails`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EndleavesMaterialsRuling`
--
ALTER TABLE `EndleavesMaterialsRuling`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EndleavesMaterialWasteTypes`
--
ALTER TABLE `EndleavesMaterialWasteTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConditions`
--
ALTER TABLE `FurnitureConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionCatchplateDetails`
--
ALTER TABLE `FurnitureConstructionCatchplateDetails`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionClaspDetails`
--
ALTER TABLE `FurnitureConstructionClaspDetails`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionMaterials`
--
ALTER TABLE `FurnitureConstructionMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionProcesses`
--
ALTER TABLE `FurnitureConstructionProcesses`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionStrapFormations`
--
ALTER TABLE `FurnitureConstructionStrapFormations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionStrapLocations`
--
ALTER TABLE `FurnitureConstructionStrapLocations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionStrapMaterials`
--
ALTER TABLE `FurnitureConstructionStrapMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionTieColours`
--
ALTER TABLE `FurnitureConstructionTieColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FurnitureConstructionTieMaterials`
--
ALTER TABLE `FurnitureConstructionTieMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `LiftingTabs`
--
ALTER TABLE `LiftingTabs`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `LiftingTabsCondition`
--
ALTER TABLE `LiftingTabsCondition`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `NotesRepairs`
--
ALTER TABLE `NotesRepairs`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PageMarkers`
--
ALTER TABLE `PageMarkers`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PageMarkersColour`
--
ALTER TABLE `PageMarkersColour`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PageMarkersCondition`
--
ALTER TABLE `PageMarkersCondition`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PageMarkersLocation`
--
ALTER TABLE `PageMarkersLocation`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Rubbings`
--
ALTER TABLE `Rubbings`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Scans`
--
ALTER TABLE `Scans`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingEdgesColours`
--
ALTER TABLE `SewingEdgesColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingEdgesDecorations`
--
ALTER TABLE `SewingEdgesDecorations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingEdgesMethods`
--
ALTER TABLE `SewingEdgesMethods`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingPreparations`
--
ALTER TABLE `SewingPreparations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingSewingConditionStructure`
--
ALTER TABLE `SewingSewingConditionStructure`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingSewingConditionThread`
--
ALTER TABLE `SewingSewingConditionThread`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingSupportsFormations`
--
ALTER TABLE `SewingSupportsFormations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingSupportsMaterials`
--
ALTER TABLE `SewingSupportsMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadColours`
--
ALTER TABLE `SewingThreadColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadMaterials`
--
ALTER TABLE `SewingThreadMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadPlys`
--
ALTER TABLE `SewingThreadPlys`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadThicknesses`
--
ALTER TABLE `SewingThreadThicknesses`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadTwists`
--
ALTER TABLE `SewingThreadTwists`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SewingThreadTypes`
--
ALTER TABLE `SewingThreadTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandBoardAttachments`
--
ALTER TABLE `SpineEndbandBoardAttachments`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandColours`
--
ALTER TABLE `SpineEndbandColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandConditions`
--
ALTER TABLE `SpineEndbandConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandConditionsAtBoard`
--
ALTER TABLE `SpineEndbandConditionsAtBoard`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandCoreMaterials`
--
ALTER TABLE `SpineEndbandCoreMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandDrawings`
--
ALTER TABLE `SpineEndbandDrawings`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandMaterials`
--
ALTER TABLE `SpineEndbandMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandSewingRoutes`
--
ALTER TABLE `SpineEndbandSewingRoutes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineEndbandTypes`
--
ALTER TABLE `SpineEndbandTypes`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineLiningConditionAtBoards`
--
ALTER TABLE `SpineLiningConditionAtBoards`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineLiningConditions`
--
ALTER TABLE `SpineLiningConditions`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineLinings`
--
ALTER TABLE `SpineLinings`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineSpineConditionAdhesives`
--
ALTER TABLE `SpineSpineConditionAdhesives`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SpineSpineConditionExtraApplications`
--
ALTER TABLE `SpineSpineConditionExtraApplications`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesConditions`
--
ALTER TABLE `TextLeavesConditions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesMaterialColours`
--
ALTER TABLE `TextLeavesMaterialColours`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesMaterials`
--
ALTER TABLE `TextLeavesMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesMaterialsRuling`
--
ALTER TABLE `TextLeavesMaterialsRuling`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesMaterialsRulingTool`
--
ALTER TABLE `TextLeavesMaterialsRulingTool`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesNewRepairsLocation`
--
ALTER TABLE `TextLeavesNewRepairsLocation`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesNewRepairsType`
--
ALTER TABLE `TextLeavesNewRepairsType`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesOldRepairsLocations`
--
ALTER TABLE `TextLeavesOldRepairsLocations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesOldRepairsMaterials`
--
ALTER TABLE `TextLeavesOldRepairsMaterials`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesOldRepairsOvercastingLocations`
--
ALTER TABLE `TextLeavesOldRepairsOvercastingLocations`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TextLeavesOldRepairsTechniques`
--
ALTER TABLE `TextLeavesOldRepairsTechniques`
  MODIFY `id` smallint NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
