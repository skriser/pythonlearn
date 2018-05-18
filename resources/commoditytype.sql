/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shop

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-05-15 14:39:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for commoditytype
-- ----------------------------
DROP TABLE IF EXISTS `commoditytype`;
CREATE TABLE `commoditytype` (
  `ct_id` int(11) NOT NULL COMMENT '商品种类编号',
  `ct_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '商品种类名称',
  PRIMARY KEY (`ct_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of commoditytype
-- ----------------------------
INSERT INTO `commoditytype` VALUES ('0', '数码产品');
INSERT INTO `commoditytype` VALUES ('1', '家电');
INSERT INTO `commoditytype` VALUES ('2', '日用品');
INSERT INTO `commoditytype` VALUES ('3', '服饰');
INSERT INTO `commoditytype` VALUES ('4', '化妆品');
