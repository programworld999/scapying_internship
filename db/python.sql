-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 09, 2019 at 08:50 AM
-- Server version: 5.7.27-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `eventshigh_com`
--

CREATE TABLE `eventshigh_com` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` text NOT NULL,
  `organizer` varchar(300) NOT NULL,
  `url` varchar(1000) NOT NULL,
  `address` varchar(500) NOT NULL,
  `price` varchar(100) NOT NULL,
  `starting_date_time` varchar(100) NOT NULL,
  `ending_date_time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eventshigh_com`
--

INSERT INTO `eventshigh_com` (`id`, `title`, `organizer`, `url`, `address`, `price`, `starting_date_time`, `ending_date_time`) VALUES
(1, 'Self-Actualized Leadership Development Workshop', 'Defined Values Consultants', 'https://www.eventshigh.com/detail/Kolkata/db0e3551f9b5ba73a7a27f75e89ce145-self-actualized-leadership-development-workshop', 'Hotel Hindusthan International', ' 3500.0 ', '2019-11-10T09:00:00+05:30', '2019-11-10T18:00:00+05:30'),
(2, 'Devi Pokkhe Durga Darshan - Durga Puja Parikrama Bonedibari Durga Darshan 2019', 'RHYTHM GALAXY GROUP', 'https://www.eventshigh.com/detail/Kolkata/ca1a92aac5234ecdd91c23f7c740e1d8-devi-pokkhe-durga-darshan-durga', 'The LaLiT Great Eastern Kolkata', ' 3000.0 ', '2019-10-07T07:00:00+05:30', '2019-10-07T17:00:00+05:30'),
(3, 'Top Sales Training in Kolkata', 'Amit Sharma Sales Leader', 'https://www.eventshigh.com/detail/Kolkata/6c13b5361c752c34dd5489279438a19a-top-sales-training-in-kolkata', 'Live Online Trainer Led Sales Training Workshop', ' 2999.0 ', '2019-08-03T10:00:00+05:30', '2019-08-03T16:30:00+05:30'),
(4, 'Belur Math &amp; Sabeki Barir Puja Parikrama', 'Niladri Roy', 'https://www.eventshigh.com/detail/Kolkata/4d090f5de169fcbdc12e72479f6b5dcb-belur-math-sabeki-barir-puja', 'Pantaloons Garia Bazaar', ' 2150.0 ', '2019-10-06T07:30:00+05:30', '2019-10-06T17:00:00+05:30'),
(5, 'One day Workshop on Advanced Excel', 'Infidea Trainings', 'https://www.eventshigh.com/detail/Kolkata/a5421c0a90650ed9c3ea5ec1465e0481-one-day-workshop-on-advanced', 'The Senator Hotel', ' 1950.0 ', '2019-11-16T10:00:00+05:30', '2019-11-16T17:30:00+05:30'),
(6, 'How to Start your Startups-A Complete Guidance &amp; Mentoring Program', 'The Inspire India', 'https://www.eventshigh.com/detail/Kolkata/f897bc3b3ed93cedf79582fbb86027b8-how-to-start-your-startups', 'OYO Townhouse 011 Esplanade', ' 3000.0 ', '2019-10-19T10:00:00+05:30', '2019-10-19T17:00:00+05:30'),
(7, 'KPMG Lean Six Sigma Green Belt Training in Kolkata', 'Lean Six Sigma', 'https://www.eventshigh.com/detail/Kolkata/ec39ee8ddb515eea1903451835b570f3-kpmg-lean-six-sigma-green', 'KPMG', ' 23600.0 ', '2019-11-18T09:00:00+05:30', '2019-11-21T17:00:00+05:30'),
(8, 'Big Data- Machine Learning and it&#x27;s Applications Workshop', 'Foito', 'https://www.eventshigh.com/detail/Kolkata/42c170f38c2fb885b545bd34dab6f0d7-big-data-machine-learning-and', 'Online On Demand', ' 5000.0 ', '2019-10-12T10:00:00+05:30', '2019-10-12T15:00:00+05:30'),
(9, 'Travel Amigo Bonedi Barir  Durga Puja Parikrama 2019', 'Niladri Roy', 'https://www.eventshigh.com/detail/Kolkata/c63b5d8bda54fa8810701093aa54ca55-travel-amigo-bonedi-barir-durga', 'Tollygunge Tram Depot Bus Stand', ' 2200.0 ', '2019-10-07T07:30:00+05:30', '2019-10-07T18:30:00+05:30'),
(10, 'DUGGA DUGGA - Durga Puja Parikrama Bonedibari Durga Darshan 2019', 'RHYTHM GALAXY GROUP', 'https://www.eventshigh.com/detail/Kolkata/93368d1bcf349d6bedf111250bb7cb23-dugga-dugga-durga-puja-parikrama', 'The LaLiT Great Eastern Kolkata', ' 3250.0 ', '2019-10-07T07:00:00+05:30', '2019-10-07T17:00:00+05:30');

-- --------------------------------------------------------

--
-- Table structure for table `insider_in`
--

CREATE TABLE `insider_in` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` text NOT NULL,
  `organizer` varchar(300) NOT NULL,
  `url` varchar(1000) NOT NULL,
  `address` varchar(500) NOT NULL,
  `price` varchar(100) NOT NULL,
  `starting_date_time` varchar(100) NOT NULL,
  `ending_date_time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `insider_in`
--

INSERT INTO `insider_in` (`id`, `title`, `organizer`, `url`, `address`, `price`, `starting_date_time`, `ending_date_time`) VALUES
(1, 'OnePlus Music Festival, 2019', 'OnePlus', 'https://insider.in/oneplus-music-festival-nov16-2019/event', 'D.Y. Patil Stadium', '5000', '2019-11-16T08:30:00.000Z', '2019-11-16T16:30:00.000Z'),
(2, 'Bacardi NH7 Weekender 2019, Pune', 'OML', 'https://insider.in/bacardi-nh7-weekender-pune-2019-112919/event', 'Mahalakshmi Lawns, Pune, Airport Area', '2750', '2019-11-29T09:30:00.000Z', '2019-12-01T16:30:00.000Z'),
(3, 'Jodhpur RIFF', 'MEHRAN GARH MUSEUM TRUST', 'https://insider.in/jodhpur-riff-oct10-2019/event', 'Mehrangarh Fort and Museum', '5000', '2019-10-10T03:00:00.000Z', '2019-10-14T13:30:00.000Z'),
(4, 'Mumbai Oktoberfest & Family Fun Carnival 2019', 'Indo-German Chamber of Commerce', 'https://insider.in/mumbai-oktoberfest-and-family-fun-carnival-oct11-13-2019/event', 'Member\'s Enclosure - Mahalaxmi Racecourse', '1399', '2019-10-11T12:30:00.000Z', '2019-10-13T17:30:00.000Z'),
(5, 'Radiance Dandiya', 'Purple Blue Events', 'https://insider.in/radiance-dandiya-sept29-oct8-2019/event', 'Hotel Sahara Star', '800', '2019-10-08T15:00:00.000Z', '2019-10-08T20:30:00.000Z'),
(6, 'Thane Raas Rang 2019', 'Credai Mchi Thane', 'https://insider.in/thane-raas-rang-sept29-2019/event', 'Modella Mill Compound', '1770', '2019-09-29T13:30:00.000Z', '2019-10-08T16:30:00.000Z'),
(7, 'Salt Rock Food Festival', 'Rices Obliquity', 'https://insider.in/salt-rock-food-festival-oct12-2019/event', 'Phoenix Marketcity, Mumbai', '149', '2019-10-12T07:30:00.000Z', '2019-10-12T18:29:00.000Z'),
(8, 'OnePlus Music Festival Presents - Kohinoor Album Launch Mumbai', 'Insider', 'https://insider.in/oneplus-music-festival-presents-kohinoor-album-launch-mumbai-2019/event', 'Mahalaxmi Racecourse', '499', '2019-10-12T12:30:00.000Z', '2019-10-12T16:30:00.000Z'),
(9, 'Mosambi Narangi', 'Fountainhead Entertainment Pvt. Ltd', 'https://insider.in/mosambi-narangi-oct12-13-2019/event', 'St. Andrew\'s Auditorium, Mumbai', '1250', '2019-10-12T14:00:00.000Z', '2019-10-12T16:30:00.000Z'),
(10, 'Joke Lab: Your Favourite Comedians Try New Stuff!', 'Alt Culture Ent Pvt Ltd - The HIVE', 'https://insider.in/joke-lab-feb5-2019/event', 'The Cuckoo Club, Mumbai', '299', '2019-10-08T15:00:00.000Z', '2019-10-08T17:30:00.000Z'),
(11, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/', 'Buddha on a Bicycle', '£5', '2019-10-04T17:00:00+02:00', '2019-10-04T18:00:00+02:00'),
(12, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-3/', 'Buddha on a Bicycle', '£5', '2019-10-18T17:00:00+02:00', '2019-10-18T18:00:00+02:00'),
(13, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-4/', 'Buddha on a Bicycle', '£5', '2019-11-01T17:00:00+02:00', '2019-11-01T18:00:00+02:00'),
(14, 'Naad Yoga Teacher Training Hamburg with Veer Kaur', 'Veer Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-veer-kaur/', 'Hamburg', 'N/A', '2019-10-05T00:00:00+02:00', '2019-10-06T23:59:59+02:00'),
(15, 'Naad Yoga Teacher Training Germany with Sidak Kaur', 'Sidak Kaur Khalsa', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-2/', 'Zentrum Naadyogaklang', 'N/A', '2019-10-12T00:00:00+02:00', '2019-10-13T23:59:59+02:00'),
(16, 'Naad Yoga Teacher Training UK', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-uk-prof-surinder-singh/', 'Raj Academy', 'N/A', '2019-11-24T10:00:00+02:00', '2019-11-24T14:00:00+02:00'),
(17, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'),
(18, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/', 'Buddha on a Bicycle', '£5', '2019-10-04T17:00:00+02:00', '2019-10-04T18:00:00+02:00'),
(19, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-3/', 'Buddha on a Bicycle', '£5', '2019-10-18T17:00:00+02:00', '2019-10-18T18:00:00+02:00'),
(20, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-4/', 'Buddha on a Bicycle', '£5', '2019-11-01T17:00:00+02:00', '2019-11-01T18:00:00+02:00'),
(21, 'Naad Yoga Teacher Training Hamburg with Veer Kaur', 'Veer Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-veer-kaur/', 'Hamburg', 'N/A', '2019-10-05T00:00:00+02:00', '2019-10-06T23:59:59+02:00'),
(22, 'Naad Yoga Teacher Training Germany with Sidak Kaur', 'Sidak Kaur Khalsa', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-2/', 'Zentrum Naadyogaklang', 'N/A', '2019-10-12T00:00:00+02:00', '2019-10-13T23:59:59+02:00'),
(23, 'Naad Yoga Teacher Training UK', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-uk-prof-surinder-singh/', 'Raj Academy', 'N/A', '2019-11-24T10:00:00+02:00', '2019-11-24T14:00:00+02:00'),
(24, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A');

-- --------------------------------------------------------

--
-- Table structure for table `interesting_url`
--

CREATE TABLE `interesting_url` (
  `id` int(10) UNSIGNED NOT NULL,
  `url` varchar(1000) NOT NULL,
  `website` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `interesting_url`
--

INSERT INTO `interesting_url` (`id`, `url`, `website`) VALUES
(1, 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/', 'insider.in'),
(2, 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-3/', 'insider.in'),
(3, 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-4/', 'insider.in'),
(4, 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-veer-kaur/', 'insider.in'),
(5, 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-2/', 'insider.in'),
(6, 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-uk-prof-surinder-singh/', 'insider.in'),
(7, 'N/A', 'insider.in');

-- --------------------------------------------------------

--
-- Table structure for table `naadyogacouncil_com`
--

CREATE TABLE `naadyogacouncil_com` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` text NOT NULL,
  `organizer` varchar(300) NOT NULL,
  `url` varchar(1000) NOT NULL,
  `address` varchar(500) NOT NULL,
  `price` varchar(100) NOT NULL,
  `starting_date_time` varchar(100) NOT NULL,
  `ending_date_time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `naadyogacouncil_com`
--

INSERT INTO `naadyogacouncil_com` (`id`, `title`, `organizer`, `url`, `address`, `price`, `starting_date_time`, `ending_date_time`) VALUES
(1, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/', 'Buddha on a Bicycle', '£5', '2019-10-04T17:00:00+02:00', '2019-10-04T18:00:00+02:00'),
(2, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-3/', 'Buddha on a Bicycle', '£5', '2019-10-18T17:00:00+02:00', '2019-10-18T18:00:00+02:00'),
(3, 'HeartSpace &#8211; Sound Meditation &#038; Naad Yoga', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-4/', 'Buddha on a Bicycle', '£5', '2019-11-01T17:00:00+02:00', '2019-11-01T18:00:00+02:00'),
(4, 'Naad Yoga Teacher Training Hamburg with Veer Kaur', 'Veer Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-veer-kaur/', 'Hamburg', 'N/A', '2019-10-05T00:00:00+02:00', '2019-10-06T23:59:59+02:00'),
(5, 'Naad Yoga Teacher Training Germany with Sidak Kaur', 'Sidak Kaur Khalsa', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-2/', 'Zentrum Naadyogaklang', 'N/A', '2019-10-12T00:00:00+02:00', '2019-10-13T23:59:59+02:00'),
(6, 'Naad Yoga Teacher Training UK', 'Satpurakh Kaur', 'https://naadyogacouncil.com/event/naad-yoga-teacher-training-uk-prof-surinder-singh/', 'Raj Academy', 'N/A', '2019-11-24T10:00:00+02:00', '2019-11-24T14:00:00+02:00'),
(7, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A');

-- --------------------------------------------------------

--
-- Table structure for table `non_interesting_url`
--

CREATE TABLE `non_interesting_url` (
  `id` int(10) UNSIGNED NOT NULL,
  `url` varchar(1000) NOT NULL,
  `website` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `eventshigh_com`
--
ALTER TABLE `eventshigh_com`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `insider_in`
--
ALTER TABLE `insider_in`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `interesting_url`
--
ALTER TABLE `interesting_url`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `naadyogacouncil_com`
--
ALTER TABLE `naadyogacouncil_com`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `non_interesting_url`
--
ALTER TABLE `non_interesting_url`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eventshigh_com`
--
ALTER TABLE `eventshigh_com`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `insider_in`
--
ALTER TABLE `insider_in`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `interesting_url`
--
ALTER TABLE `interesting_url`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `naadyogacouncil_com`
--
ALTER TABLE `naadyogacouncil_com`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `non_interesting_url`
--
ALTER TABLE `non_interesting_url`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
