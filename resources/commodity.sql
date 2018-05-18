/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shop

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-05-15 14:38:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for commodity
-- ----------------------------
DROP TABLE IF EXISTS `commodity`;
CREATE TABLE `commodity` (
  `c_id` int(11) NOT NULL COMMENT '商品编号',
  `c_name` varchar(22) NOT NULL COMMENT '商品编号',
  `c_madein` varchar(50) NOT NULL COMMENT '商品产地',
  `c_type` int(11) NOT NULL COMMENT '商品种类',
  `c_inprice` int(11) NOT NULL COMMENT '商品进价',
  `c_outprice` int(11) DEFAULT NULL COMMENT '商品售价',
  `c_num` int(11) DEFAULT NULL COMMENT '商品售价',
  PRIMARY KEY (`c_id`),
  KEY `FK_commodity_type` (`c_type`),
  CONSTRAINT `FK_commodity_type` FOREIGN KEY (`c_type`) REFERENCES `commoditytype` (`ct_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of commodity
-- ----------------------------
INSERT INTO `commodity` VALUES ('1', 'IphoneX', '美国', '0', '7500', '8900', '300');
INSERT INTO `commodity` VALUES ('2', '香奈儿', '法国', '4', '1000', '1500', '250');
INSERT INTO `commodity` VALUES ('3', '瓷器', '中国', '2', '1000', '1500', '200');
INSERT INTO `commodity` VALUES ('4', '相机', '日本', '0', '3500', '4000', '120');
INSERT INTO `commodity` VALUES ('5', '移动硬盘', '日本', '0', '250', '275', '350');
INSERT INTO `commodity` VALUES ('6', 'mac', '美国', '0', '9800', '13000', '80');
INSERT INTO `commodity` VALUES ('7', '华为', '中国', '0', '4000', '6000', '500');
INSERT INTO `commodity` VALUES ('8', '旗袍', '中国', '3', '400', '600', null);
