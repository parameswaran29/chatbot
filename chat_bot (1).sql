-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 07, 2023 at 10:01 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `chat_bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `parent_details`
--

CREATE TABLE `parent_details` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nos` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parent_details`
--

INSERT INTO `parent_details` (`id`, `name`, `contact`, `address`, `gender`, `email`, `username`, `password`, `nos`) VALUES
(1, 'vimal', '7895123456', 'thillai nagar', 'Male', 'siva@gmail.com', 'vimal', '123', 'guru');

-- --------------------------------------------------------

--
-- Table structure for table `query_details`
--

CREATE TABLE `query_details` (
  `id` int(50) NOT NULL,
  `query` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `user` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `query_details`
--

INSERT INTO `query_details` (`id`, `query`, `answer`, `image`, `user`, `username`) VALUES
(1, 'f', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(2, 'placement of 2017', '', 'Untitled.png', 'Parent', 'vimal'),
(3, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(5, 'placement of 2017', '', 'Untitled.png', 'Student', 'guru'),
(6, 'placement of 2017', '', 'Untitled.png', 'Student', 'guru'),
(7, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(7, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'vimal'),
(8, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(9, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(10, 'placement of 2017', '', 'Untitled.png', 'Parent', 'vimal'),
(11, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(12, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(13, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(14, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(15, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(16, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(17, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(18, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(19, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(20, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(21, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(22, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(23, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(24, 'placement of 2017', '', 'Untitled.png', 'Student', 'guru'),
(25, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(26, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(27, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(28, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(29, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(30, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(31, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(32, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Student', 'guru'),
(33, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(34, 'dean of mcs', 'Priya mam', 'no_image.jpg', 'Parent', 'vimal'),
(35, 'hi', 'sargurunathan', 'no_image.jpg', 'Parent', 'vimal'),
(36, 'placement of 2017', '', 'Untitled.png', 'Parent', 'vimal');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `name`, `contact`, `dob`, `address`, `gender`, `email`, `department`, `year`, `semester`, `username`, `password`) VALUES
(1, 'guru', '7895123456', '16/06/2001', 'villupuram', 'Male', 'guru@gmail.com', 'dme', 'a', '3', 'guru', '123'),
(2, 'nancy', '9778655887', '16/06/2001', 'thillai nagar', 'Female', 'siva@gmail.com', 'dme', '5', '3', 'nancy', '123');

-- --------------------------------------------------------

--
-- Table structure for table `trained_set`
--

CREATE TABLE `trained_set` (
  `id` int(50) NOT NULL,
  `query` varchar(100) NOT NULL,
  `response` varchar(100) NOT NULL,
  `graphical` varchar(100) NOT NULL,
  `percen` float(50,0) NOT NULL,
  `print` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `trained_set`
--

INSERT INTO `trained_set` (`id`, `query`, `response`, `graphical`, `percen`, `print`) VALUES
(1, 'who is the dean of msc cs?', 'Priya mam', 'no_image.jpg', 1, ''),
(2, 'Placement from 2017 till now', '', 'Untitled.png', 0, ''),
(3, 'hi', 'sargurunathan', 'no_image.jpg', 0, ''),
(4, 'what a won', 'taj', 'no_image.jpg', 0, ''),
(5, 'best course to learn', 'python', 'no_image.jpg', 0, '');
