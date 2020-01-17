# bsgo 사이트를 사용한 번역 로그 테이블
# 해당 데이터는 어느 정도 쌓이면 학습용 데이터로 사용된다.

CREATE TABLE `tbl_trans_lang_log` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`oCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '언어감지코드',
	`tCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '번역결과언어코드',
	`oStr` TEXT NULL DEFAULT NULL COMMENT '원문',
	`tStc` TEXT NULL DEFAULT NULL COMMENT '번역문',
	`regDate` TIMESTAMP NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`id`)

INSERT INTO `py_db`.`tbl_trans_lang_log` 
	(`oCode`, `tCode`, `oStr`, `tStc`) 
VALUES ('en', 'ko', 'hello', '안녕');