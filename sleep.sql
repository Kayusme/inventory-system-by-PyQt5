/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : sleep

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 03/01/2019 17:30:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 产品信息表
-- ----------------------------
DROP TABLE IF EXISTS `产品信息表`;
CREATE TABLE `产品信息表`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品等级` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产地` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `进价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `包装物` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 产品信息表
-- ----------------------------
INSERT INTO `产品信息表` VALUES ('GK074', '次节瓜', '4', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('10101', '次节瓜', '4', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('0K434', '电次炮椒', '4', '电白', '2', '箱');
INSERT INTO `产品信息表` VALUES ('44444', '次节瓜', '4', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('GK073', '包节瓜', '3', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('GK075', '次节瓜', '4', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('GK01', '包节瓜', '3', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('GK033', '包节瓜', '3', '下桥', '2', '箱');
INSERT INTO `产品信息表` VALUES ('GK44', '45', '452', '54', '452', '542');
INSERT INTO `产品信息表` VALUES ('DAS', 'ASD', 'SAD', 'SAD', 'SAD', 'SAD');
INSERT INTO `产品信息表` VALUES ('74', '74', '74', '74', '74', '74');
INSERT INTO `产品信息表` VALUES ('2', '3', '3', '3', '3', '3');
INSERT INTO `产品信息表` VALUES ('3', '3', '2', '2', '2', '3');
INSERT INTO `产品信息表` VALUES ('GK110', '次节瓜', '4', '下桥', '2', '箱');

-- ----------------------------
-- Table structure for 产品品种编码表
-- ----------------------------
DROP TABLE IF EXISTS `产品品种编码表`;
CREATE TABLE `产品品种编码表`  (
  `编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 产品品种编码表
-- ----------------------------
INSERT INTO `产品品种编码表` VALUES ('JN001', '101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN002', 'A箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN003', 'A箱尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN004', 'B箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN005', '包101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN001', '101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN002', 'A箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN003', 'A箱尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN004', 'B箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN005', '包101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN006', '包白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN007', '包扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN008', '包大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN009', '包海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN010', '包荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN011', '包红茄');
INSERT INTO `产品品种编码表` VALUES ('JN012', '包尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN013', '包节瓜');
INSERT INTO `产品品种编码表` VALUES ('JN014', '包炮椒');
INSERT INTO `产品品种编码表` VALUES ('JN015', '包青瓜');
INSERT INTO `产品品种编码表` VALUES ('JN016', '包四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN017', '包西葫芦');
INSERT INTO `产品品种编码表` VALUES ('JN018', '包以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN019', '包圆瓜');
INSERT INTO `产品品种编码表` VALUES ('JN020', '包圆椒');
INSERT INTO `产品品种编码表` VALUES ('JN021', '包长南瓜');
INSERT INTO `产品品种编码表` VALUES ('JN022', '包长三角');
INSERT INTO `产品品种编码表` VALUES ('JN023', '次101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN024', '次白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN025', '次扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN026', '次大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN027', '次海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN028', '次荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN029', '次红茄');
INSERT INTO `产品品种编码表` VALUES ('JN030', '次尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN031', '次苦瓜');
INSERT INTO `产品品种编码表` VALUES ('JN032', '电刺红茄');
INSERT INTO `产品品种编码表` VALUES ('JN033', '电条红茄');
INSERT INTO `产品品种编码表` VALUES ('JN034', '次以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN035', '电包红茄');
INSERT INTO `产品品种编码表` VALUES ('JN001', '101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN002', 'A箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN003', 'A箱尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN004', 'B箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN005', '包101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN006', '包白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN007', '包扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN008', '包大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN009', '包海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN010', '包荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN011', '包红茄');
INSERT INTO `产品品种编码表` VALUES ('JN012', '包尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN013', '包节瓜');
INSERT INTO `产品品种编码表` VALUES ('JN014', '包炮椒');
INSERT INTO `产品品种编码表` VALUES ('JN015', '包青瓜');
INSERT INTO `产品品种编码表` VALUES ('JN016', '包四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN017', '包西葫芦');
INSERT INTO `产品品种编码表` VALUES ('JN018', '包以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN019', '包圆瓜');
INSERT INTO `产品品种编码表` VALUES ('JN020', '包圆椒');
INSERT INTO `产品品种编码表` VALUES ('JN021', '包长南瓜');
INSERT INTO `产品品种编码表` VALUES ('JN022', '包长三角');
INSERT INTO `产品品种编码表` VALUES ('JN023', '次101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN024', '次白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN025', '次扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN026', '次大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN027', '次海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN028', '次荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN029', '次红茄');
INSERT INTO `产品品种编码表` VALUES ('JN030', '次尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN031', '次苦瓜');
INSERT INTO `产品品种编码表` VALUES ('JN032', '电刺红茄');
INSERT INTO `产品品种编码表` VALUES ('JN033', '电条红茄');
INSERT INTO `产品品种编码表` VALUES ('JN034', '次以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN035', '电包红茄');
INSERT INTO `产品品种编码表` VALUES ('JN001', '101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN002', 'A箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN003', 'A箱尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN004', 'B箱番茄');
INSERT INTO `产品品种编码表` VALUES ('JN005', '包101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN006', '包白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN007', '包扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN008', '包大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN009', '包海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN010', '包荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN011', '包红茄');
INSERT INTO `产品品种编码表` VALUES ('JN012', '包尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN013', '包节瓜');
INSERT INTO `产品品种编码表` VALUES ('JN014', '包炮椒');
INSERT INTO `产品品种编码表` VALUES ('JN015', '包青瓜');
INSERT INTO `产品品种编码表` VALUES ('JN016', '包四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN017', '包西葫芦');
INSERT INTO `产品品种编码表` VALUES ('JN018', '包以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN019', '包圆瓜');
INSERT INTO `产品品种编码表` VALUES ('JN020', '包圆椒');
INSERT INTO `产品品种编码表` VALUES ('JN021', '包长南瓜');
INSERT INTO `产品品种编码表` VALUES ('JN022', '包长三角');
INSERT INTO `产品品种编码表` VALUES ('JN023', '次101番茄');
INSERT INTO `产品品种编码表` VALUES ('JN024', '次白四季豆');
INSERT INTO `产品品种编码表` VALUES ('JN025', '次扁豆');
INSERT INTO `产品品种编码表` VALUES ('JN026', '次大红尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN027', '次海花红椒');
INSERT INTO `产品品种编码表` VALUES ('JN028', '次荷豆');
INSERT INTO `产品品种编码表` VALUES ('JN029', '次红茄');
INSERT INTO `产品品种编码表` VALUES ('JN030', '次尖椒');
INSERT INTO `产品品种编码表` VALUES ('JN031', '次苦瓜');
INSERT INTO `产品品种编码表` VALUES ('JN032', '电刺红茄');
INSERT INTO `产品品种编码表` VALUES ('JN033', '电条红茄');
INSERT INTO `产品品种编码表` VALUES ('JN034', '次以色列番茄');
INSERT INTO `产品品种编码表` VALUES ('JN035', '电包红茄');

-- ----------------------------
-- Table structure for 产品库存表
-- ----------------------------
DROP TABLE IF EXISTS `产品库存表`;
CREATE TABLE `产品库存表`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `等级` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `条码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 产品库存表
-- ----------------------------
INSERT INTO `产品库存表` VALUES ('0F011', '刺红茄', '1', '122', '123', 'E122', '');
INSERT INTO `产品库存表` VALUES ('0F012', '条红茄', '2', '252', '132', 'E123', NULL);
INSERT INTO `产品库存表` VALUES ('0F013', '次结瓜', '1', '133', '134', 'E134', NULL);
INSERT INTO `产品库存表` VALUES ('0F014', '电刺红茄', '2', '234', '141', 'E251', NULL);
INSERT INTO `产品库存表` VALUES ('0F015', '包节瓜', '3', '99', '175', 'E162', NULL);
INSERT INTO `产品库存表` VALUES ('1', '1', '1', '1', '1', '1', '1');

-- ----------------------------
-- Table structure for 产品收购表
-- ----------------------------
DROP TABLE IF EXISTS `产品收购表`;
CREATE TABLE `产品收购表`  (
  `单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `金额` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `检验人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `经手人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `入库时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `片名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `农户编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 产品收购表
-- ----------------------------
INSERT INTO `产品收购表` VALUES ('1', '0K011', '电刺红茄', '2.5', '10000', '25000', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('2', '0K012', '电条红茄', '2.2', '30000', '66000', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('3', '0K013', '电包红茄', '1.5', '5000', '7500', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('4', '0K014', '电次红茄', '1.5', '9000', '13500', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('5', '0K021', '电刺青', '1.2', '4000', '4800', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('6', '0K011', '电刺红茄', '2.5', '12514', '31285', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('7', '0K012', '电条红茄', '2.2', '26310', '57882', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('8', '0K013', '电包红茄', '1.5', '5785', '8677.5', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ002', NULL);
INSERT INTO `产品收购表` VALUES ('9', '0K014', '电次红茄', '1.5', '9271', '13906.5', '1', '1', '2006-04-17 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('10', '0K021', '电刺青', '1.2', '3434', '4120.799805', NULL, '1', '2006-04-17 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('11', '0K011', '电刺红茄', '2.5', '10000', '25000', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('12', '0K012', '电条红茄', '2.2', '18000', '39600', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('13', '0K013', '电包红茄', '1.5', '19000', '28500', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('14', '0K014', '电次红茄', '1.5', '8000', '12000', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ001', NULL);
INSERT INTO `产品收购表` VALUES ('15', '0k021', '电刺青', '1.2', '12883', '15459.599609', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('16', '0K011', '电刺红茄', '2.5', '7753', '19382.5', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('17', '0k012', '电条红茄', '2.2', '20820', '45804', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('18', '0K013', '电包红茄', '1.5', '20029', '30043.5', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('19', '0K014', '电次红茄', '1.5', '9984', '14976', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('20', '0k021', '电刺青', '1.2', '14120', '16944', '1', '1', '2006-04-18 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('21', '0K032', '电条尖椒', '2', '10', '20', '1', '1', '2006-04-28 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('22', '0K033', '电包尖椒', '2', '10', '20', '1', '1', '2006-04-28 00:00:00', '观珠', 'GZ002', '1');
INSERT INTO `产品收购表` VALUES ('23', 'KK012', '条红茄', '2', '10', '20', '1', '1', '2006-04-29 00:00:00', '观珠', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('24', '0k011', '电刺红茄', '2.5', '12', '30.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('25', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123');
INSERT INTO `产品收购表` VALUES ('26', '12', '123', '123123', '123', '213', '123', '213', '1', '1', '1', '1');
INSERT INTO `产品收购表` VALUES ('27', '121', '1', '1', '1', '11', '1', '1', '1', '1', '1', '1');
INSERT INTO `产品收购表` VALUES ('28', '121', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12');
INSERT INTO `产品收购表` VALUES ('29', '0K011', '电刺红茄', '2.5', '10', '25.0', '11', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('30', '0K011', '电刺红茄', '2.5', '10', '25.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('31', '0K011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '11', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('32', '0K011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('33', '0K011', '电刺红茄', '2.5', '10', '25.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('34', '0K011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('35', '0K011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('36', '0k011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '1', '1', 'GZ001', '1');
INSERT INTO `产品收购表` VALUES ('37', '0K011', '电刺红茄', '2.5', '100', '250.0', '1', '1', '1', '1', 'GZ001', '1');

-- ----------------------------
-- Table structure for 代购点产品出库
-- ----------------------------
DROP TABLE IF EXISTS `代购点产品出库`;
CREATE TABLE `代购点产品出库`  (
  `单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 代购点产品出库
-- ----------------------------
INSERT INTO `代购点产品出库` VALUES ('1', '121', '1', '1', '');
INSERT INTO `代购点产品出库` VALUES ('2', '121', '1', '1', '');
INSERT INTO `代购点产品出库` VALUES ('3', '121', '1', '11', '');

-- ----------------------------
-- Table structure for 代购点产品库存
-- ----------------------------
DROP TABLE IF EXISTS `代购点产品库存`;
CREATE TABLE `代购点产品库存`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 代购点产品库存
-- ----------------------------
INSERT INTO `代购点产品库存` VALUES ('出库单号', NULL, NULL, NULL);
INSERT INTO `代购点产品库存` VALUES ('121', '1', '1', '1');

-- ----------------------------
-- Table structure for 代购点产品盘存
-- ----------------------------
DROP TABLE IF EXISTS `代购点产品盘存`;
CREATE TABLE `代购点产品盘存`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 代购点产品盘存
-- ----------------------------
INSERT INTO `代购点产品盘存` VALUES ('12', '12', '12', '12');

-- ----------------------------
-- Table structure for 代购点信息表
-- ----------------------------
DROP TABLE IF EXISTS `代购点信息表`;
CREATE TABLE `代购点信息表`  (
  `片编码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `片名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `片负责人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `联系电话` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 代购点信息表
-- ----------------------------
INSERT INTO `代购点信息表` VALUES ('1', '公司总部', '赵香港', '15548446841');
INSERT INTO `代购点信息表` VALUES ('2', '基地', '王仪榜', '17825634187');
INSERT INTO `代购点信息表` VALUES ('3', '批发中心', '程万龙', '16478956562');
INSERT INTO `代购点信息表` VALUES ('4', '代购点', '张冕宸', '17986565655');

-- ----------------------------
-- Table structure for 公司机构设置表
-- ----------------------------
DROP TABLE IF EXISTS `公司机构设置表`;
CREATE TABLE `公司机构设置表`  (
  `机构编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构类型` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构地址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `建设日期` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 公司机构设置表
-- ----------------------------
INSERT INTO `公司机构设置表` VALUES ('JG002', '基地', '中心基地二', '五环', '2001-02-01 00:00:00', '无');
INSERT INTO `公司机构设置表` VALUES ('JG001', '基地', '中心基地一', '五环', '2001-02-01 00:00:00', '无');
INSERT INTO `公司机构设置表` VALUES ('JG003', '批发', '批发点一', '四环', '2003-03-15 00:00:00', '无');
INSERT INTO `公司机构设置表` VALUES ('JG004', '批发', '批发点二', '四环', '2004-01-18 00:00:00', '无');
INSERT INTO `公司机构设置表` VALUES ('JG005', '代购', '代购点一', '三环', '2005-12-15 00:00:00', NULL);
INSERT INTO `公司机构设置表` VALUES ('JG006', '代购', '代购点二', '三环', '2006-10-17 00:00:00', NULL);
INSERT INTO `公司机构设置表` VALUES ('JG007', '代购', '代购点三', '二环', '2010-02-08 00:00:00', NULL);
INSERT INTO `公司机构设置表` VALUES ('424', '基地', '中心基地二', '五环', '2001-02-01 00:00:00', '无');

-- ----------------------------
-- Table structure for 农户信息表
-- ----------------------------
DROP TABLE IF EXISTS `农户信息表`;
CREATE TABLE `农户信息表`  (
  `农户编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `农户名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `农户住址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `联系电话` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `播种面积/平方米` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 农户信息表
-- ----------------------------
INSERT INTO `农户信息表` VALUES ('nwh001', '张一', '武汉市洪山区花山镇', '18745140001', '1000');
INSERT INTO `农户信息表` VALUES ('nwh002', '张二', '武汉市洪山区花山镇', '18745140002', '1000');
INSERT INTO `农户信息表` VALUES ('nwh003', '张三', '武汉市洪山区花山镇', '18745140003', '1000');
INSERT INTO `农户信息表` VALUES ('nwh004', '张四', '武汉市洪山区花山镇', '18745140004', '1000');
INSERT INTO `农户信息表` VALUES ('nwh005', '张五', '武汉市洪山区花山镇', '18745140005', '1000');
INSERT INTO `农户信息表` VALUES ('nwh006', '张一一', '武汉市洪山区花山镇', '18745140006', '1000');
INSERT INTO `农户信息表` VALUES ('nwh007', '张一与', '武汉市洪山区花山镇', '18745140007', '1000');
INSERT INTO `农户信息表` VALUES ('nwh008', '张一好', '武汉市洪山区花山镇', '18745140008', '1000');
INSERT INTO `农户信息表` VALUES ('nwh009', '张一雨', '武汉市洪山区花山镇', '18745140009', '1000');
INSERT INTO `农户信息表` VALUES ('nwh010', '张一去', '武汉市洪山区花山镇', '18745140010', '1000');
INSERT INTO `农户信息表` VALUES ('nwh011', '张一额', '武汉市洪山区花山镇', '18745140011', '1000');
INSERT INTO `农户信息表` VALUES ('GZ001', 'D', 'D', 'D', 'D');

-- ----------------------------
-- Table structure for 基地产品出库表
-- ----------------------------
DROP TABLE IF EXISTS `基地产品出库表`;
CREATE TABLE `基地产品出库表`  (
  `单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `进价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `金额` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `经手人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `出库时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `片名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `收货方` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 基地产品出库表
-- ----------------------------
INSERT INTO `基地产品出库表` VALUES ('2', 'OK012', '电条红茄', '2.20', '56285', '123827', '1', '2006/4/17', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('3', 'OK013', '电包红茄', '1.50', '0', '0', '1', '2006/4/17', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('4', 'OK014', '电包红茄', '1.50', '10775', '16162.50', '1', '2006/4/17', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('5', 'OK015', '电次红茄', '1.50', '18271', '27406.50', '1', '2006/4/17', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('6', 'OK016', '电刺青', '1.20', '7400', '8880', '1', '2006/4/17', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('7', 'OK017', '电刺红茄', '2.50', '17750', '44375', '1', '2006/4/18', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('8', 'OK018', '电条红茄', '2.20', '38785', '85327', '1', '2006/4/18', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('9', 'OK019', '电包红茄', '1.50', '39025', '58537', '1', '2006/4/18', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('10', 'OK020', '电次红茄', '1.50', '17950', '26925', '1', '2006/4/18', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('1', 'OK011', '电刺青', '1.25', '1111', '321', '1', '2006/4/18', '观珠', '中心一', '424');
INSERT INTO `基地产品出库表` VALUES ('13', 'OK015', '电次红茄', '1.50', '11', '16.5', '1', '1', '1', '1', '424');
INSERT INTO `基地产品出库表` VALUES ('14', 'OK015', '电次红茄', '1.50', '11', '16.5', '1', '1', '1', '1', '424');
INSERT INTO `基地产品出库表` VALUES ('13', 'OK015', '电次红茄', '1.50', '11', '16.5', '1', '1', '1', '1', '424');

-- ----------------------------
-- Table structure for 基地产品库存信息
-- ----------------------------
DROP TABLE IF EXISTS `基地产品库存信息`;
CREATE TABLE `基地产品库存信息`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `条码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 基地产品库存信息
-- ----------------------------
INSERT INTO `基地产品库存信息` VALUES ('OK111', '电刺红茄', '12', '123', '424', '');
INSERT INTO `基地产品库存信息` VALUES ('0F012', '条红茄', '5', '321', '424', NULL);
INSERT INTO `基地产品库存信息` VALUES ('0k011', '电刺红茄', '100', '0', '424', '1');
INSERT INTO `基地产品库存信息` VALUES ('0K011', '电刺红茄', '100', '0', '424', '1');
INSERT INTO `基地产品库存信息` VALUES ('OK015', '电刺红茄', '100', '1', '424', '1');

-- ----------------------------
-- Table structure for 基地产品盘点表
-- ----------------------------
DROP TABLE IF EXISTS `基地产品盘点表`;
CREATE TABLE `基地产品盘点表`  (
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `盘存数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 基地产品盘点表
-- ----------------------------
INSERT INTO `基地产品盘点表` VALUES ('0F011', '刺红茄', '1');
INSERT INTO `基地产品盘点表` VALUES ('0F012', '条红茄', '2');
INSERT INTO `基地产品盘点表` VALUES ('0F013', '茄子', '12');

-- ----------------------------
-- Table structure for 基地物资盘点表
-- ----------------------------
DROP TABLE IF EXISTS `基地物资盘点表`;
CREATE TABLE `基地物资盘点表`  (
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 基地物资盘点表
-- ----------------------------
INSERT INTO `基地物资盘点表` VALUES ('B00321', '袋子', '22');
INSERT INTO `基地物资盘点表` VALUES ('B00421', '绳子', '4443');
INSERT INTO `基地物资盘点表` VALUES ('B00255', '箩筐', '50');

-- ----------------------------
-- Table structure for 库存表
-- ----------------------------
DROP TABLE IF EXISTS `库存表`;
CREATE TABLE `库存表`  (
  `ID` int(11) NOT NULL,
  `编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `操作` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `余量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `操作人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 库存表
-- ----------------------------
INSERT INTO `库存表` VALUES (1, 'A001', '茄子', '入库', '0', '100', '20180101', 'zxg');
INSERT INTO `库存表` VALUES (2, 'A001', '茄子', '出库', '10', '90', '20180102', 'zxg');
INSERT INTO `库存表` VALUES (3, 'A001', '茄子', '入库', '10', '100', '20180103', 'zxg');
INSERT INTO `库存表` VALUES (4, 'A001', '茄子', '入库', '10', '110', '20180104', 'zxg');
INSERT INTO `库存表` VALUES (5, 'A001', '茄子', '出库', '10', '100', '20180105', 'zxg');
INSERT INTO `库存表` VALUES (6, 'A001', '茄子', '出库', '10', '90', '20180106', 'zxg');
INSERT INTO `库存表` VALUES (7, 'A001', '茄子', '出库', '10', '80', '20180107', 'zxg');
INSERT INTO `库存表` VALUES (8, 'A001', '茄子', '出库', '10', '70', '20180108', 'zxg');
INSERT INTO `库存表` VALUES (9, 'A001', '茄子', '出库', '10', '60', '20180109', 'zxg');
INSERT INTO `库存表` VALUES (10, 'A001', '茄子', '出库', '10', '50', '20180110', 'zxg');
INSERT INTO `库存表` VALUES (11, 'A001', '茄子', '出库', '10', '40', '20180111', 'zxg');

-- ----------------------------
-- Table structure for 物资信息表
-- ----------------------------
DROP TABLE IF EXISTS `物资信息表`;
CREATE TABLE `物资信息表`  (
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单位` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `进价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `出价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 物资信息表
-- ----------------------------
INSERT INTO `物资信息表` VALUES ('B00255', '箩筐', '个', '2.1', '2.1', NULL);
INSERT INTO `物资信息表` VALUES ('B00221', '纸盒', '个', '2.1', '2.1', NULL);
INSERT INTO `物资信息表` VALUES ('B00321', '袋子', '个', '2.1', '2.1', 'history');
INSERT INTO `物资信息表` VALUES ('B00421', '绳子', '捆', '2.1', '2.1', NULL);
INSERT INTO `物资信息表` VALUES ('B00521', '胶筐', '个', '2.1', '2.1', NULL);
INSERT INTO `物资信息表` VALUES ('H00121', '氮肥', '袋', '4.1', '4.1', 'mysql');
INSERT INTO `物资信息表` VALUES ('H00221', '磷肥', '袋', '3.1', '3.1', NULL);
INSERT INTO `物资信息表` VALUES ('H00321', '钾肥', '袋', '5.1', '5.1', NULL);
INSERT INTO `物资信息表` VALUES ('N00121', '杀虫双', '瓶', '2.1', '2.1', NULL);
INSERT INTO `物资信息表` VALUES ('N00221', '敌敌畏', '瓶', '3.1', '3.1', NULL);
INSERT INTO `物资信息表` VALUES ('N00321', '蚜虫净', '瓶', '4.1', '4.1', NULL);
INSERT INTO `物资信息表` VALUES ('Z00121', '西红柿种子', '袋', '9.1', '9.1', NULL);
INSERT INTO `物资信息表` VALUES ('Z00321', '大白菜种子', '袋', '7.1', '7.1', NULL);
INSERT INTO `物资信息表` VALUES ('Z00421', '四季豆种子', '袋', '6.1', '6.1', NULL);
INSERT INTO `物资信息表` VALUES ('Z00521', '夏尖椒', '袋', '5.1', '5.1', 'query');

-- ----------------------------
-- Table structure for 物资入库信息表
-- ----------------------------
DROP TABLE IF EXISTS `物资入库信息表`;
CREATE TABLE `物资入库信息表`  (
  `单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `机构编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 物资入库信息表
-- ----------------------------
INSERT INTO `物资入库信息表` VALUES ('1', '1', '4', '4', '10', '');
INSERT INTO `物资入库信息表` VALUES ('2', '1', '1', '0', '10', '');
INSERT INTO `物资入库信息表` VALUES ('3', '1', '1', '0', '10', '');
INSERT INTO `物资入库信息表` VALUES ('4', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('5', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('6', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('7', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('8', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('9', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('10', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('11', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('12', 'B00255', '箩筐', '2.1', '12', '424');
INSERT INTO `物资入库信息表` VALUES ('13', 'b00255', '箩筐', '2.1', '100', '424');
INSERT INTO `物资入库信息表` VALUES ('14', 'B00255', '箩筐', '2.1', '100', '424');
INSERT INTO `物资入库信息表` VALUES ('15', 'B00255', '箩筐', '2.1', '10', '424');
INSERT INTO `物资入库信息表` VALUES ('16', 'B00255', '箩筐', '2.1', '100', '424');
INSERT INTO `物资入库信息表` VALUES ('17', 'B00255', '箩筐', '2.1', '10', '424');

-- ----------------------------
-- Table structure for 物资出库信息表
-- ----------------------------
DROP TABLE IF EXISTS `物资出库信息表`;
CREATE TABLE `物资出库信息表`  (
  `单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `农户编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `物资名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 物资出库信息表
-- ----------------------------
INSERT INTO `物资出库信息表` VALUES ('1', '1', '1', '1', '0', '10');
INSERT INTO `物资出库信息表` VALUES ('2', '1', '1', '1', '0', '10');
INSERT INTO `物资出库信息表` VALUES ('3', '1', '1', '1', '0', '10');
INSERT INTO `物资出库信息表` VALUES ('4', '1', '1', '1', '0', '10');
INSERT INTO `物资出库信息表` VALUES ('5', 'nwh001', 'B00255', '箩筐', '2.1', '12');
INSERT INTO `物资出库信息表` VALUES ('6', 'nwh001', 'B00255', '箩筐', '2.1', '10');
INSERT INTO `物资出库信息表` VALUES ('7', 'nwh001', 'B00255', '箩筐', '2.1', '100');
INSERT INTO `物资出库信息表` VALUES ('8', 'nwh001', 'b00255', '箩筐', '2.1', '10');
INSERT INTO `物资出库信息表` VALUES ('9', 'nwh001', 'B00255', '箩筐', '2.1', '50');

-- ----------------------------
-- Table structure for 物资库存信息表
-- ----------------------------
DROP TABLE IF EXISTS `物资库存信息表`;
CREATE TABLE `物资库存信息表`  (
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单位` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 物资库存信息表
-- ----------------------------
INSERT INTO `物资库存信息表` VALUES ('B00321', '袋子', '22', '个', '无');
INSERT INTO `物资库存信息表` VALUES ('B00421', '绳子', '4443', '捆', '无');
INSERT INTO `物资库存信息表` VALUES ('b00255', '箩筐', '250', '个', '无');
INSERT INTO `物资库存信息表` VALUES ('B00255', '箩筐', '10', '个', '无');

-- ----------------------------
-- Table structure for 物资盘存信息表
-- ----------------------------
DROP TABLE IF EXISTS `物资盘存信息表`;
CREATE TABLE `物资盘存信息表`  (
  `物资编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 物资盘存信息表
-- ----------------------------
INSERT INTO `物资盘存信息表` VALUES ('B00321', '袋子', '22', '无');
INSERT INTO `物资盘存信息表` VALUES ('B00421', '绳子', '4443', '无');
INSERT INTO `物资盘存信息表` VALUES ('B00255', '箩筐', '140', '无');
INSERT INTO `物资盘存信息表` VALUES ('b00255', '箩筐', '140', '无');
INSERT INTO `物资盘存信息表` VALUES ('B00321', '袋子', '22', '1');

-- ----------------------------
-- Table structure for 生产计划信息表
-- ----------------------------
DROP TABLE IF EXISTS `生产计划信息表`;
CREATE TABLE `生产计划信息表`  (
  `序号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `农户姓名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `品种` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `面积` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `播种期` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 生产计划信息表
-- ----------------------------
INSERT INTO `生产计划信息表` VALUES ('66', '李四', '青瓜', '20', '三月中旬', '无');
INSERT INTO `生产计划信息表` VALUES ('67', '张三', '青瓜', '30', '三月中旬', '无');

-- ----------------------------
-- Table structure for 用户申请
-- ----------------------------
DROP TABLE IF EXISTS `用户申请`;
CREATE TABLE `用户申请`  (
  `用户名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `密码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `公司权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `批发中心权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `基地权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `代购点权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 用户管理
-- ----------------------------
DROP TABLE IF EXISTS `用户管理`;
CREATE TABLE `用户管理`  (
  `用户名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `密码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `公司权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `批发中心权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `基地权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `代购点权限` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 用户管理
-- ----------------------------
INSERT INTO `用户管理` VALUES ('admin', '123456', '1', '1', '1', '1');
INSERT INTO `用户管理` VALUES ('mr', '123', '1', '1', '1', '1');
INSERT INTO `用户管理` VALUES ('zzk', '123', '1', '1', '1', '1');
INSERT INTO `用户管理` VALUES ('zxg', '123', '1', '1', '1', '1');
INSERT INTO `用户管理` VALUES ('1', '2', '1', '0', '0', '0');
INSERT INTO `用户管理` VALUES ('2', '2', '0', '1', '0', '0');
INSERT INTO `用户管理` VALUES ('3', '3', '0', '0', '1', '0');
INSERT INTO `用户管理` VALUES ('4', '4', '0', '0', '0', '1');
INSERT INTO `用户管理` VALUES ('sad', 'as', '0', '1', '0', '0');

-- ----------------------------
-- Table structure for 销售统计表
-- ----------------------------
DROP TABLE IF EXISTS `销售统计表`;
CREATE TABLE `销售统计表`  (
  `销售单号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `产品名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `售出数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `售出价格` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `销售日期` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `客户编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 销售统计表
-- ----------------------------
INSERT INTO `销售统计表` VALUES ('2018010125', 'JN013', '包节瓜', '345', '0.9', '20180101', 'kwh052');
INSERT INTO `销售统计表` VALUES ('2018010125', 'JN013', '包节瓜', '412', '1.1', '20180101', 'kwh053');
INSERT INTO `销售统计表` VALUES ('2018010126', 'JN013', '包节瓜', '101', '2.3', '20180101', 'kwh054');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN013', '包节瓜', '245', '1.3', '20180101', 'kwh055');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN013', '包节瓜', '236', '2', '20180101', 'kwh056');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN013', '包节瓜', '323', '0.9', '20180101', 'kwh057');
INSERT INTO `销售统计表` VALUES ('2018010128', 'JN013', '包节瓜', '324', '1', '20180101', 'kwh058');
INSERT INTO `销售统计表` VALUES ('2018010129', 'JN013', '包节瓜', '423', '2.2', '20180101', 'kwh059');
INSERT INTO `销售统计表` VALUES ('2018010129', 'JN013', '包节瓜', '388', '1.3', '20180101', 'kwh060');
INSERT INTO `销售统计表` VALUES ('2018010130', 'JN013', '包节瓜', '346', '2', '20180101', 'kwh061');
INSERT INTO `销售统计表` VALUES ('2018010130', 'JN013', '包节瓜', '103', '0.9', '20180101', 'kwh062');
INSERT INTO `销售统计表` VALUES ('2018010131', 'JN013', '包节瓜', '300', '1', '20180101', 'kwh063');
INSERT INTO `销售统计表` VALUES ('2018010157', 'JN014', '包炮椒', '334', '0.9', '20180101', 'kwh064');
INSERT INTO `销售统计表` VALUES ('2018010158', 'JN014', '包炮椒', '345', '1.1', '20180101', 'kwh065');
INSERT INTO `销售统计表` VALUES ('2018010158', 'JN014', '包炮椒', '412', '2.3', '20180101', 'kwh066');
INSERT INTO `销售统计表` VALUES ('2018010159', 'JN014', '包炮椒', '101', '1.3', '20180101', 'kwh067');
INSERT INTO `销售统计表` VALUES ('2018010159', 'JN014', '包炮椒', '245', '2', '20180101', 'kwh068');
INSERT INTO `销售统计表` VALUES ('2018010160', 'JN014', '包炮椒', '236', '0.9', '20180101', 'kwh069');
INSERT INTO `销售统计表` VALUES ('2018010142', 'JN015', '包青瓜', '323', '1', '20180101', 'kwh070');
INSERT INTO `销售统计表` VALUES ('2018010143', 'JN015', '包青瓜', '324', '1.3', '20180101', 'kwh071');
INSERT INTO `销售统计表` VALUES ('2018010143', 'JN015', '包青瓜', '423', '2', '20180101', 'kwh072');
INSERT INTO `销售统计表` VALUES ('2018010143', 'JN015', '包青瓜', '388', '0.9', '20180101', 'kwh073');
INSERT INTO `销售统计表` VALUES ('2018010100', 'JN016', '包四季豆', '346', '1', '20180101', 'kwh074');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN016', '包四季豆', '103', '2.2', '20180101', 'kwh075');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN016', '包四季豆', '300', '2.3', '20180101', 'kwh076');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN016', '包四季豆', '334', '1.3', '20180101', 'kwh077');
INSERT INTO `销售统计表` VALUES ('2018010102', 'JN016', '包四季豆', '345', '2', '20180101', 'kwh078');
INSERT INTO `销售统计表` VALUES ('2018010160', 'JN016', '包四季豆', '412', '1', '20180101', 'kwh079');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN017', '包西葫芦', '101', '2', '20180101', 'kwh080');
INSERT INTO `销售统计表` VALUES ('2018010122', 'JN017', '包西葫芦', '245', '1', '20180101', 'kwh081');
INSERT INTO `销售统计表` VALUES ('2018010123', 'JN017', '包西葫芦', '236', '2.2', '20180101', 'kwh082');
INSERT INTO `销售统计表` VALUES ('2018010123', 'JN017', '包西葫芦', '323', '2.3', '20180101', 'kwh083');
INSERT INTO `销售统计表` VALUES ('2018010124', 'JN017', '包西葫芦', '324', '1.3', '20180101', 'kwh084');
INSERT INTO `销售统计表` VALUES ('2018010124', 'JN017', '包西葫芦', '423', '2', '20180101', 'kwh085');
INSERT INTO `销售统计表` VALUES ('2018010115', 'JN018', '包以色列番茄', '388', '2.3', '20180101', 'kwh086');
INSERT INTO `销售统计表` VALUES ('2018010115', 'JN018', '包以色列番茄', '346', '0.9', '20180101', 'kwh087');
INSERT INTO `销售统计表` VALUES ('2018010116', 'JN018', '包以色列番茄', '103', '1.1', '20180101', 'kwh088');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN018', '包以色列番茄', '300', '2.2', '20180101', 'kwh089');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN018', '包以色列番茄', '334', '2.2', '20180101', 'kwh090');
INSERT INTO `销售统计表` VALUES ('2018010118', 'JN018', '包以色列番茄', '345', '2.3', '20180101', 'kwh091');
INSERT INTO `销售统计表` VALUES ('2018010134', 'JN019', '包圆瓜', '412', '2.2', '20180101', 'kwh092');
INSERT INTO `销售统计表` VALUES ('2018010135', 'JN019', '包圆瓜', '101', '1.3', '20180101', 'kwh093');
INSERT INTO `销售统计表` VALUES ('2018010136', 'JN019', '包圆瓜', '245', '0.9', '20180101', 'kwh094');
INSERT INTO `销售统计表` VALUES ('2018010136', 'JN019', '包圆瓜', '236', '1', '20180101', 'kwh095');
INSERT INTO `销售统计表` VALUES ('2018010137', 'JN019', '包圆瓜', '323', '1.1', '20180101', 'kwh096');
INSERT INTO `销售统计表` VALUES ('2018010137', 'JN019', '包圆瓜', '324', '2.2', '20180101', 'kwh097');
INSERT INTO `销售统计表` VALUES ('2018010154', 'JN020', '包圆椒', '423', '2', '20180101', 'kwh098');
INSERT INTO `销售统计表` VALUES ('2018010154', 'JN020', '包圆椒', '388', '1', '20180101', 'kwh099');
INSERT INTO `销售统计表` VALUES ('2018010155', 'JN020', '包圆椒', '346', '2.2', '20180101', 'kwh100');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN020', '包圆椒', '103', '2.3', '20180101', 'kwh101');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN020', '包圆椒', '300', '1.3', '20180101', 'kwh102');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN020', '包圆椒', '334', '2', '20180101', 'kwh103');
INSERT INTO `销售统计表` VALUES ('2018010131', 'JN021', '包长南瓜', '345', '1.1', '20180101', 'kwh104');
INSERT INTO `销售统计表` VALUES ('2018010132', 'JN021', '包长南瓜', '412', '2.3', '20180101', 'kwh105');
INSERT INTO `销售统计表` VALUES ('2018010133', 'JN021', '包长南瓜', '101', '2', '20180101', 'kwh106');
INSERT INTO `销售统计表` VALUES ('2018010133', 'JN021', '包长南瓜', '245', '0.9', '20180101', 'kwh107');
INSERT INTO `销售统计表` VALUES ('2018010133', 'JN021', '包长南瓜', '236', '1', '20180101', 'kwh108');
INSERT INTO `销售统计表` VALUES ('2018010134', 'JN021', '包长南瓜', '323', '1.1', '20180101', 'kwh109');
INSERT INTO `销售统计表` VALUES ('2018010105', 'JN022', '包长三角', '324', '1', '20180101', 'kwh110');
INSERT INTO `销售统计表` VALUES ('2018010106', 'JN022', '包长三角', '423', '2.2', '20180101', 'kwh111');
INSERT INTO `销售统计表` VALUES ('2018010107', 'JN022', '包长三角', '388', '1.3', '20180101', 'kwh112');
INSERT INTO `销售统计表` VALUES ('2018010107', 'JN022', '包长三角', '346', '2', '20180101', 'kwh113');
INSERT INTO `销售统计表` VALUES ('2018010108', 'JN022', '包长三角', '103', '0.9', '20180101', 'kwh114');
INSERT INTO `销售统计表` VALUES ('2018010108', 'JN022', '包长三角', '300', '1', '20180101', 'kwh115');
INSERT INTO `销售统计表` VALUES ('2018010118', 'JN023', '次101番茄', '334', '0.9', '20180101', 'kwh116');
INSERT INTO `销售统计表` VALUES ('2018010119', 'JN023', '次101番茄', '345', '1.1', '20180101', 'kwh117');
INSERT INTO `销售统计表` VALUES ('2018010120', 'JN023', '次101番茄', '412', '2.3', '20180101', 'kwh118');
INSERT INTO `销售统计表` VALUES ('2018010120', 'JN023', '次101番茄', '101', '1.3', '20180101', 'kwh119');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN023', '次101番茄', '245', '2', '20180101', 'kwh120');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN023', '次101番茄', '236', '0.9', '20180101', 'kwh121');
INSERT INTO `销售统计表` VALUES ('2018010102', 'JN024', '次白四季豆', '323', '1.1', '20180101', 'kwh122');
INSERT INTO `销售统计表` VALUES ('2018010103', 'JN024', '次白四季豆', '324', '2.3', '20180101', 'kwh123');
INSERT INTO `销售统计表` VALUES ('2018010104', 'JN024', '次白四季豆', '423', '2', '20180101', 'kwh124');
INSERT INTO `销售统计表` VALUES ('2018010104', 'JN024', '次白四季豆', '388', '0.9', '20180101', 'kwh125');
INSERT INTO `销售统计表` VALUES ('2018010105', 'JN024', '次白四季豆', '346', '1', '20180101', 'kwh126');
INSERT INTO `销售统计表` VALUES ('2018010105', 'JN024', '次白四季豆', '103', '1.1', '20180101', 'kwh127');
INSERT INTO `销售统计表` VALUES ('2018010112', 'JN025', '次扁豆', '300', '1.3', '20180101', 'kwh128');
INSERT INTO `销售统计表` VALUES ('2018010113', 'JN025', '次扁豆', '334', '0.9', '20180101', 'kwh129');
INSERT INTO `销售统计表` VALUES ('2018010113', 'JN025', '次扁豆', '345', '1.1', '20180101', 'kwh130');
INSERT INTO `销售统计表` VALUES ('2018010114', 'JN025', '次扁豆', '412', '2.2', '20180101', 'kwh131');
INSERT INTO `销售统计表` VALUES ('2018010114', 'JN025', '次扁豆', '101', '2.3', '20180101', 'kwh132');
INSERT INTO `销售统计表` VALUES ('2018010115', 'JN025', '次扁豆', '245', '1.3', '20180101', 'kwh133');
INSERT INTO `销售统计表` VALUES ('2018010147', 'JN026', '次大红尖椒', '236', '2.3', '20180101', 'kwh134');
INSERT INTO `销售统计表` VALUES ('2018010148', 'JN026', '次大红尖椒', '323', '2', '20180101', 'kwh135');
INSERT INTO `销售统计表` VALUES ('2018010149', 'JN026', '次大红尖椒', '324', '2.2', '20180101', 'kwh136');
INSERT INTO `销售统计表` VALUES ('2018010149', 'JN026', '次大红尖椒', '423', '2.3', '20180101', 'kwh137');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN026', '次大红尖椒', '388', '1.3', '20180101', 'kwh138');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN026', '次大红尖椒', '346', '2', '20180101', 'kwh139');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN027', '次海花红椒', '103', '0.9', '20180101', 'kwh140');
INSERT INTO `销售统计表` VALUES ('2018010151', 'JN027', '次海花红椒', '300', '1.1', '20180101', 'kwh141');
INSERT INTO `销售统计表` VALUES ('2018010152', 'JN027', '次海花红椒', '334', '2.3', '20180101', 'kwh142');
INSERT INTO `销售统计表` VALUES ('2018010152', 'JN027', '次海花红椒', '345', '1.3', '20180101', 'kwh143');
INSERT INTO `销售统计表` VALUES ('2018010153', 'JN027', '次海花红椒', '412', '2', '20180101', 'kwh144');
INSERT INTO `销售统计表` VALUES ('2018010153', 'JN027', '次海花红椒', '101', '0.9', '20180101', 'kwh145');
INSERT INTO `销售统计表` VALUES ('2018010109', 'JN028', '次荷豆', '245', '2.3', '20180101', 'kwh146');
INSERT INTO `销售统计表` VALUES ('2018010109', 'JN028', '次荷豆', '236', '2', '20180101', 'kwh147');
INSERT INTO `销售统计表` VALUES ('2018010110', 'JN028', '次荷豆', '323', '1', '20180101', 'kwh148');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN028', '次荷豆', '324', '1.1', '20180101', 'kwh149');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN028', '次荷豆', '423', '2.2', '20180101', 'kwh150');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN028', '次荷豆', '388', '2.3', '20180101', 'kwh151');
INSERT INTO `销售统计表` VALUES ('2018010140', 'JN029', '次红茄', '346', '2', '20180101', 'kwh152');
INSERT INTO `销售统计表` VALUES ('2018010125', 'JN031', '次苦瓜', '324', '1.1', '20180101', 'kwh162');
INSERT INTO `销售统计表` VALUES ('2018010125', 'JN031', '次苦瓜', '423', '2.3', '20180101', 'kwh163');
INSERT INTO `销售统计表` VALUES ('2018010126', 'JN031', '次苦瓜', '388', '2', '20180101', 'kwh164');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN031', '次苦瓜', '346', '0.9', '20180101', 'kwh165');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN031', '次苦瓜', '103', '1', '20180101', 'kwh166');
INSERT INTO `销售统计表` VALUES ('2018010127', 'JN031', '次苦瓜', '300', '1.1', '20180101', 'kwh167');
INSERT INTO `销售统计表` VALUES ('2018010128', 'JN031', '次苦瓜', '334', '2.2', '20180101', 'kwh168');
INSERT INTO `销售统计表` VALUES ('2018010129', 'JN031', '次苦瓜', '345', '1.3', '20180101', 'kwh169');
INSERT INTO `销售统计表` VALUES ('2018010129', 'JN031', '次苦瓜', '412', '0.9', '20180101', 'kwh170');
INSERT INTO `销售统计表` VALUES ('2018010130', 'JN031', '次苦瓜', '101', '1', '20180101', 'kwh171');
INSERT INTO `销售统计表` VALUES ('2018010130', 'JN031', '次苦瓜', '245', '1.1', '20180101', 'kwh172');
INSERT INTO `销售统计表` VALUES ('2018010131', 'JN031', '次苦瓜', '236', '2.2', '20180101', 'kwh173');
INSERT INTO `销售统计表` VALUES ('2018010157', 'JN032', '电刺红茄', '323', '1.1', '20180101', 'kwh174');
INSERT INTO `销售统计表` VALUES ('2018010158', 'JN032', '电刺红茄', '324', '2.3', '20180101', 'kwh175');
INSERT INTO `销售统计表` VALUES ('2018010158', 'JN032', '电刺红茄', '423', '2', '20180101', 'kwh176');
INSERT INTO `销售统计表` VALUES ('2018010159', 'JN032', '电刺红茄', '388', '0.9', '20180101', 'kwh177');
INSERT INTO `销售统计表` VALUES ('2018010159', 'JN032', '电刺红茄', '346', '1', '20180101', 'kwh178');
INSERT INTO `销售统计表` VALUES ('2018010160', 'JN032', '电刺红茄', '103', '1.1', '20180101', 'kwh179');
INSERT INTO `销售统计表` VALUES ('2018010142', 'JN032', '电刺红茄', '300', '2.2', '20180101', 'kwh180');
INSERT INTO `销售统计表` VALUES ('2018010142', 'JN032', '电刺红茄', '334', '2', '20180101', 'kwh181');
INSERT INTO `销售统计表` VALUES ('2018010143', 'JN033', '电条红茄', '345', '0.9', '20180101', 'kwh182');
INSERT INTO `销售统计表` VALUES ('2018010143', 'JN033', '电条红茄', '412', '1', '20180101', 'kwh183');
INSERT INTO `销售统计表` VALUES ('2018010100', 'JN033', '电条红茄', '245', '2.2', '20180101', 'kwh185');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN033', '电条红茄', '236', '1.3', '20180101', 'kwh186');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN033', '电条红茄', '323', '2', '20180101', 'kwh187');
INSERT INTO `销售统计表` VALUES ('2018010101', 'JN033', '电条红茄', '324', '0.9', '20180101', 'kwh188');
INSERT INTO `销售统计表` VALUES ('2018010102', 'JN033', '电条红茄', '423', '1', '20180101', 'kwh189');
INSERT INTO `销售统计表` VALUES ('2018010160', 'JN033', '电条红茄', '388', '2.2', '20180101', 'kwh190');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN033', '电条红茄', '346', '1', '20180101', 'kwh191');
INSERT INTO `销售统计表` VALUES ('2018010122', 'JN033', '电条红茄', '103', '2.2', '20180101', 'kwh192');
INSERT INTO `销售统计表` VALUES ('2018010123', 'JN033', '电条红茄', '300', '1.3', '20180101', 'kwh193');
INSERT INTO `销售统计表` VALUES ('2018010123', 'JN033', '电条红茄', '334', '2', '20180101', 'kwh194');
INSERT INTO `销售统计表` VALUES ('2018010124', 'JN033', '电条红茄', '345', '0.9', '20180101', 'kwh195');
INSERT INTO `销售统计表` VALUES ('2018010124', 'JN033', '电条红茄', '412', '1', '20180101', 'kwh196');
INSERT INTO `销售统计表` VALUES ('2018010115', 'JN033', '电条红茄', '101', '2', '20180101', 'kwh197');
INSERT INTO `销售统计表` VALUES ('2018010116', 'JN034', '次以色列番茄', '245', '1.1', '20180101', 'kwh198');
INSERT INTO `销售统计表` VALUES ('2018010116', 'JN034', '次以色列番茄', '236', '2.3', '20180101', 'kwh199');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN034', '次以色列番茄', '323', '1.3', '20180101', 'kwh200');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN034', '次以色列番茄', '324', '1.3', '20180101', 'kwh201');
INSERT INTO `销售统计表` VALUES ('2018010118', 'JN034', '次以色列番茄', '423', '2', '20180101', 'kwh202');
INSERT INTO `销售统计表` VALUES ('2018010134', 'JN035', '电包红茄', '388', '1.3', '20180101', 'kwh203');
INSERT INTO `销售统计表` VALUES ('2018010135', 'JN035', '电包红茄', '346', '0.9', '20180101', 'kwh204');
INSERT INTO `销售统计表` VALUES ('2018010136', 'JN035', '电包红茄', '103', '1.1', '20180101', 'kwh205');
INSERT INTO `销售统计表` VALUES ('2018010136', 'JN035', '电包红茄', '300', '2.2', '20180101', 'kwh206');
INSERT INTO `销售统计表` VALUES ('2018010137', 'JN035', '电包红茄', '334', '2.3', '20180101', 'kwh207');
INSERT INTO `销售统计表` VALUES ('2018010137', 'JN035', '电包红茄', '345', '1.3', '20180101', 'kwh208');
INSERT INTO `销售统计表` VALUES ('2018010154', 'JN035', '电包红茄', '346', '1', '20180101', 'kwh209');
INSERT INTO `销售统计表` VALUES ('2018010154', 'JN035', '电包红茄', '347', '2.2', '20180101', 'kwh210');
INSERT INTO `销售统计表` VALUES ('2018010155', 'JN035', '电包红茄', '348', '1.3', '20180101', 'kwh211');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN035', '电包红茄', '349', '2', '20180101', 'kwh212');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN035', '电包红茄', '350', '0.9', '20180101', 'kwh213');
INSERT INTO `销售统计表` VALUES ('2018010156', 'JN035', '电包红茄', '351', '1', '20180101', 'kwh214');
INSERT INTO `销售统计表` VALUES ('2018010131', 'JN035', '电包红茄', '352', '2.3', '20180101', 'kwh215');
INSERT INTO `销售统计表` VALUES ('2018010132', 'JN035', '电包红茄', '353', '2', '20180101', 'kwh216');
INSERT INTO `销售统计表` VALUES ('2018010133', 'JN035', '电包红茄', '354', '1', '20180101', 'kwh217');
INSERT INTO `销售统计表` VALUES ('2018010133', 'JN035', '电包红茄', '355', '1.1', '20180101', 'kwh218');
INSERT INTO `销售统计表` VALUES ('2018010118', 'JN001', '101番茄', '412', '1.1', '20180101', 'kwh001');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN002', 'A箱番茄', '101', '1.1', '20180101', 'kwh002');
INSERT INTO `销售统计表` VALUES ('2018010138', 'JN003', 'A箱尖椒', '245', '1.3', '20180101', 'kwh003');
INSERT INTO `销售统计表` VALUES ('2018010117', 'JN004', 'B箱番茄', '236', '0.9', '20180101', 'kwh004');
INSERT INTO `销售统计表` VALUES ('2018010120', 'JN005', '包101番茄', '388', '2.2', '20180101', 'kwh008');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN005', '包101番茄', '346', '2.3', '20180101', 'kwh009');
INSERT INTO `销售统计表` VALUES ('2018010121', 'JN005', '包101番茄', '103', '1.3', '20180101', 'kwh010');
INSERT INTO `销售统计表` VALUES ('2018010118', 'JN005', '包101番茄', '323', '1.3', '20180101', 'kwh005');
INSERT INTO `销售统计表` VALUES ('2018010119', 'JN005', '包101番茄', '324', '0.9', '20180101', 'kwh006');
INSERT INTO `销售统计表` VALUES ('2018010120', 'JN005', '包101番茄', '423', '1.1', '20180101', 'kwh007');
INSERT INTO `销售统计表` VALUES ('2018010102', 'JN006', '包白四季豆', '300', '0.9', '20180101', 'kwh011');
INSERT INTO `销售统计表` VALUES ('2018010103', 'JN006', '包白四季豆', '334', '1.1', '20180101', 'kwh012');
INSERT INTO `销售统计表` VALUES ('2018010104', 'JN006', '包白四季豆', '345', '2.3', '20180101', 'kwh013');
INSERT INTO `销售统计表` VALUES ('2018010104', 'JN006', '包白四季豆', '412', '1.3', '20180101', 'kwh014');
INSERT INTO `销售统计表` VALUES ('2018010105', 'JN006', '包白四季豆', '101', '2', '20180101', 'kwh015');
INSERT INTO `销售统计表` VALUES ('2018010105', 'JN006', '包白四季豆', '245', '0.9', '20180101', 'kwh016');
INSERT INTO `销售统计表` VALUES ('2018010112', 'JN007', '包扁豆', '236', '2.2', '20180101', 'kwh017');
INSERT INTO `销售统计表` VALUES ('2018010113', 'JN007', '包扁豆', '323', '1.3', '20180101', 'kwh018');
INSERT INTO `销售统计表` VALUES ('2018010113', 'JN007', '包扁豆', '324', '0.9', '20180101', 'kwh019');
INSERT INTO `销售统计表` VALUES ('2018010114', 'JN007', '包扁豆', '423', '1', '20180101', 'kwh020');
INSERT INTO `销售统计表` VALUES ('2018010114', 'JN007', '包扁豆', '388', '1.1', '20180101', 'kwh021');
INSERT INTO `销售统计表` VALUES ('2018010115', 'JN007', '包扁豆', '346', '2.2', '20180101', 'kwh022');
INSERT INTO `销售统计表` VALUES ('2018010147', 'JN008', '包大红尖椒', '103', '1', '20180101', 'kwh023');
INSERT INTO `销售统计表` VALUES ('2018010148', 'JN008', '包大红尖椒', '300', '2.3', '20180101', 'kwh024');
INSERT INTO `销售统计表` VALUES ('2018010149', 'JN008', '包大红尖椒', '334', '1', '20180101', 'kwh025');
INSERT INTO `销售统计表` VALUES ('2018010149', 'JN008', '包大红尖椒', '345', '1.1', '20180101', 'kwh026');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN008', '包大红尖椒', '412', '2.2', '20180101', 'kwh027');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN008', '包大红尖椒', '101', '2.3', '20180101', 'kwh028');
INSERT INTO `销售统计表` VALUES ('2018010150', 'JN009', '包海花红椒', '245', '1.3', '20180101', 'kwh029');
INSERT INTO `销售统计表` VALUES ('2018010151', 'JN009', '包海花红椒', '236', '0.9', '20180101', 'kwh030');
INSERT INTO `销售统计表` VALUES ('2018010152', 'JN009', '包海花红椒', '323', '1.1', '20180101', 'kwh031');
INSERT INTO `销售统计表` VALUES ('2018010152', 'JN009', '包海花红椒', '324', '2.2', '20180101', 'kwh032');
INSERT INTO `销售统计表` VALUES ('2018010153', 'JN009', '包海花红椒', '423', '2.3', '20180101', 'kwh033');
INSERT INTO `销售统计表` VALUES ('2018010153', 'JN009', '包海花红椒', '388', '1.3', '20180101', 'kwh034');
INSERT INTO `销售统计表` VALUES ('2018010109', 'JN010', '包荷豆', '346', '1.1', '20180101', 'kwh035');
INSERT INTO `销售统计表` VALUES ('2018010109', 'JN010', '包荷豆', '103', '2.3', '20180101', 'kwh036');
INSERT INTO `销售统计表` VALUES ('2018010110', 'JN010', '包荷豆', '300', '2', '20180101', 'kwh037');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN010', '包荷豆', '334', '0.9', '20180101', 'kwh038');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN010', '包荷豆', '345', '1', '20180101', 'kwh039');
INSERT INTO `销售统计表` VALUES ('2018010111', 'JN010', '包荷豆', '412', '1.1', '20180101', 'kwh040');
INSERT INTO `销售统计表` VALUES ('2018010137', 'JN011', '包红茄', '101', '0.9', '20180101', 'kwh041');
INSERT INTO `销售统计表` VALUES ('2018010140', 'JN011', '包红茄', '245', '2.3', '20180101', 'kwh042');

-- ----------------------------
-- Table structure for 顾客信息表
-- ----------------------------
DROP TABLE IF EXISTS `顾客信息表`;
CREATE TABLE `顾客信息表`  (
  `客户编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `名称` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `地址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `邮编` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `电话` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `信誉度` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 顾客信息表
-- ----------------------------
INSERT INTO `顾客信息表` VALUES ('gwh001', '赵先生', '华农', '430070', '1335264321', '90');
INSERT INTO `顾客信息表` VALUES ('gwh002', '程先生', '华农', '430070', '18755421645', '100');
INSERT INTO `顾客信息表` VALUES ('gwh003', '王先生', '华农', '430070', '15422658754', '100');
INSERT INTO `顾客信息表` VALUES ('gwh004', '张先生', '华农', '430070', '16955455844', '100');
INSERT INTO `顾客信息表` VALUES ('gwh005', '马先生', '华农', '430070', '1318511125', '85');

-- ----------------------------
-- Table structure for 顾客购买
-- ----------------------------
DROP TABLE IF EXISTS `顾客购买`;
CREATE TABLE `顾客购买`  (
  `ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `顾客编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `顾客姓名` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `购买物品` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `单价` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `数量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `备注` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 顾客购买
-- ----------------------------
INSERT INTO `顾客购买` VALUES ('1', 'gwh001', '赵先生', '尖椒', '2', '4', '2018-01-08 00:00:00', '无');
INSERT INTO `顾客购买` VALUES ('2', 'gwh001', '赵先生', '四季豆', '3', '9', '2018-01-08 00:00:00', '无');
INSERT INTO `顾客购买` VALUES ('3', 'gwh002', '程先生', '四季豆', '3', '12', '2018-01-08 00:00:00', '无');

SET FOREIGN_KEY_CHECKS = 1;
