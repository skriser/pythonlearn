/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : myschool

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-05-15 13:13:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stu_no` int(11) NOT NULL AUTO_INCREMENT,
  `stu_pwd` varchar(20) NOT NULL DEFAULT '123456',
  `stu_name` varchar(50) NOT NULL,
  `stu_sex` char(2) NOT NULL,
  `stu_grade_id` int(11) NOT NULL,
  `stu_phone` varchar(255) NOT NULL,
  `stu_address` varchar(255) NOT NULL DEFAULT '学生宿舍',
  `stu_borndate` date DEFAULT NULL,
  `stu_email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stu_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '123456', 'Jack', '男', '1', '13022222222', '学生宿舍', '1995-03-01', 'aab@qq.com');
INSERT INTO `student` VALUES ('2', '123456', 'Mary', '女', '2', '180324567889', '公寓', '1994-06-08', 'ccc@gmail.com');
INSERT INTO `student` VALUES ('3', '123456', '张三丰', '男', '2', '18734678902', '学生宿舍', '1996-05-08', 'ddd@sina.com');
INSERT INTO `student` VALUES ('4', '123456', '张杰', '男', '4', '17023458898', '教师公寓', '1988-09-12', 'eee@163.com');
