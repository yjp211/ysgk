BEGIN;

DROP DATABASE  IF EXISTS `ysgk`;
CREATE DATABASE `ysgk`;
USE `ysgk`;

CREATE TABLE `game_file` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `use_on` varchar(1024) NOT NULL,
    `mini_type` varchar(1024) NOT NULL,
    `width` integer,
    `height` integer,
    `size` integer NOT NULL,
    `url` varchar(2048) NOT NULL
)
;
CREATE TABLE `game_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `update_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL,
    `desc` longtext,
    `desc_ch` longtext
)
;
CREATE TABLE `game_category` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `update_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL,
    `desc` longtext,
    `desc_ch` longtext,
    `icon_id` integer
)
;
ALTER TABLE `game_category` ADD CONSTRAINT `icon_id_refs_id_9d46e9d7` FOREIGN KEY (`icon_id`) REFERENCES `game_file` (`id`);
CREATE TABLE `game_game_tags` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`game_id`, `tag_id`)
)
;
ALTER TABLE `game_game_tags` ADD CONSTRAINT `tag_id_refs_id_fb802a13` FOREIGN KEY (`tag_id`) REFERENCES `game_tag` (`id`);
CREATE TABLE `game_game_screens` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `file_id` integer NOT NULL,
    UNIQUE (`game_id`, `file_id`)
)
;
ALTER TABLE `game_game_screens` ADD CONSTRAINT `file_id_refs_id_abe1456a` FOREIGN KEY (`file_id`) REFERENCES `game_file` (`id`);
CREATE TABLE `game_game` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `update_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL,
    `desc` longtext NOT NULL,
    `desc_ch` longtext NOT NULL,
    `star` integer NOT NULL,
    `icon_id` integer,
    `rec_screen_id` integer,
    `flash_id` integer,
    `ipa_id` integer,
    `apk_id` integer,
    `apk_pack_id` integer
)
;
ALTER TABLE `game_game` ADD CONSTRAINT `icon_id_refs_id_13d2eb14` FOREIGN KEY (`icon_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game` ADD CONSTRAINT `rec_screen_id_refs_id_13d2eb14` FOREIGN KEY (`rec_screen_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game` ADD CONSTRAINT `flash_id_refs_id_13d2eb14` FOREIGN KEY (`flash_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game` ADD CONSTRAINT `ipa_id_refs_id_13d2eb14` FOREIGN KEY (`ipa_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game` ADD CONSTRAINT `apk_id_refs_id_13d2eb14` FOREIGN KEY (`apk_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game` ADD CONSTRAINT `apk_pack_id_refs_id_13d2eb14` FOREIGN KEY (`apk_pack_id`) REFERENCES `game_file` (`id`);
ALTER TABLE `game_game_tags` ADD CONSTRAINT `game_id_refs_id_47cf5d07` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`);
ALTER TABLE `game_game_screens` ADD CONSTRAINT `game_id_refs_id_95d60a02` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`);
CREATE TABLE `game_categorys` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `stick_time` datetime,
    `game_id` integer NOT NULL,
    `category_id` integer NOT NULL,
    `rank` integer NOT NULL,
    UNIQUE (`game_id`, `category_id`)
)
;
ALTER TABLE `game_categorys` ADD CONSTRAINT `game_id_refs_id_3689d066` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`);
ALTER TABLE `game_categorys` ADD CONSTRAINT `category_id_refs_id_bd993c42` FOREIGN KEY (`category_id`) REFERENCES `game_category` (`id`);
CREATE INDEX `game_category_465cb59b` ON `game_category` (`icon_id`);
CREATE INDEX `game_game_465cb59b` ON `game_game` (`icon_id`);
CREATE INDEX `game_game_0229d4d2` ON `game_game` (`rec_screen_id`);
CREATE INDEX `game_game_c74a3f57` ON `game_game` (`flash_id`);
CREATE INDEX `game_game_f524f373` ON `game_game` (`ipa_id`);
CREATE INDEX `game_game_660e1303` ON `game_game` (`apk_id`);
CREATE INDEX `game_game_364de4fe` ON `game_game` (`apk_pack_id`);
CREATE INDEX `game_categorys_65e12249` ON `game_categorys` (`game_id`);
CREATE INDEX `game_categorys_6f33f001` ON `game_categorys` (`category_id`);


INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Management', '经营', '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Strategy', '策略', '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Puzzle', '益智',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Casual', '休闲',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Action', '动作',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Adventures', '冒险',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Sports', '体育',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Arcade', '街机',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Physics', '物理',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Shooter', '射击',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Defense', '塔防',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Racing', '竞速',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Cards', '棋牌',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Role-play', '角色扮演',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Kids', '小孩',  '', '');
INSERT INTO game_tag (`create_time`, `update_time`, `name`, `name_ch`, `desc`, `desc_ch`) VALUES ('2014/06/15 12:00:00', '2014/06/15 12:00:00', 'Zuma', '祖玛',  '', '');

COMMIT;