DROP DATABASE  IF EXISTS `ysgk`;
CREATE DATABASE `ysgk`;
USE `ysgk`;

CREATE TABLE `file` (
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
CREATE TABLE `tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL
)
;
CREATE TABLE `category` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL,
    `icon_id` integer NOT NULL
)
;
ALTER TABLE `category` ADD CONSTRAINT `icon_id_refs_id_47eef2d5` FOREIGN KEY (`icon_id`) REFERENCES `file` (`id`);
CREATE TABLE `game_tags` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`game_id`, `tag_id`)
)
;
ALTER TABLE `game_tags` ADD CONSTRAINT `tag_id_refs_id_8f55a277` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`);
CREATE TABLE `game_screens` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `file_id` integer NOT NULL,
    UNIQUE (`game_id`, `file_id`)
)
;
ALTER TABLE `game_screens` ADD CONSTRAINT `file_id_refs_id_e3848933` FOREIGN KEY (`file_id`) REFERENCES `file` (`id`);
CREATE TABLE `game` (
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
ALTER TABLE `game` ADD CONSTRAINT `icon_id_refs_id_2adc86ff` FOREIGN KEY (`icon_id`) REFERENCES `file` (`id`);
ALTER TABLE `game` ADD CONSTRAINT `rec_screen_id_refs_id_2adc86ff` FOREIGN KEY (`rec_screen_id`) REFERENCES `file` (`id`);
ALTER TABLE `game` ADD CONSTRAINT `flash_id_refs_id_2adc86ff` FOREIGN KEY (`flash_id`) REFERENCES `file` (`id`);
ALTER TABLE `game` ADD CONSTRAINT `ipa_id_refs_id_2adc86ff` FOREIGN KEY (`ipa_id`) REFERENCES `file` (`id`);
ALTER TABLE `game` ADD CONSTRAINT `apk_id_refs_id_2adc86ff` FOREIGN KEY (`apk_id`) REFERENCES `file` (`id`);
ALTER TABLE `game` ADD CONSTRAINT `apk_pack_id_refs_id_2adc86ff` FOREIGN KEY (`apk_pack_id`) REFERENCES `file` (`id`);
ALTER TABLE `game_tags` ADD CONSTRAINT `game_id_refs_id_da4533b5` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
ALTER TABLE `game_screens` ADD CONSTRAINT `game_id_refs_id_47c1073b` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
CREATE TABLE `local_store` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `category_id` integer NOT NULL,
    `rank` integer NOT NULL,
    UNIQUE (`game_id`, `category_id`)
)
;
ALTER TABLE `local_store` ADD CONSTRAINT `game_id_refs_id_19cec16b` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
ALTER TABLE `local_store` ADD CONSTRAINT `category_id_refs_id_9fab35a0` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
CREATE INDEX `category_465cb59b` ON `category` (`icon_id`);
CREATE INDEX `game_465cb59b` ON `game` (`icon_id`);
CREATE INDEX `game_0229d4d2` ON `game` (`rec_screen_id`);
CREATE INDEX `game_c74a3f57` ON `game` (`flash_id`);
CREATE INDEX `game_f524f373` ON `game` (`ipa_id`);
CREATE INDEX `game_660e1303` ON `game` (`apk_id`);
CREATE INDEX `game_364de4fe` ON `game` (`apk_pack_id`);
CREATE INDEX `local_store_65e12249` ON `local_store` (`game_id`);
CREATE INDEX `local_store_6f33f001` ON `local_store` (`category_id`);

INSERT INTO tag (name, name_ch) VALUES ('Management', '经营');
INSERT INTO tag (name, name_ch) VALUES ('Strategy', '策略');
INSERT INTO tag (name, name_ch) VALUES ('Puzzle', '益智');
INSERT INTO tag (name, name_ch) VALUES ('Casual', '休闲');
INSERT INTO tag (name, name_ch) VALUES ('Action', '动作');
INSERT INTO tag (name, name_ch) VALUES ('Adventures', '冒险');
INSERT INTO tag (name, name_ch) VALUES ('Sports', '体育');
INSERT INTO tag (name, name_ch) VALUES ('Arcade', '街机');
INSERT INTO tag (name, name_ch) VALUES ('Physics', '物理');
INSERT INTO tag (name, name_ch) VALUES ('Shooter', '射击');
INSERT INTO tag (name, name_ch) VALUES ('Defense', '塔防');
INSERT INTO tag (name, name_ch) VALUES ('Racing', '竞速');
INSERT INTO tag (name, name_ch) VALUES ('Cards', '棋牌');
INSERT INTO tag (name, name_ch) VALUES ('Role-play', '角色扮演');
INSERT INTO tag (name, name_ch) VALUES ('Kids', '小孩');
INSERT INTO tag (name, name_ch) VALUES ('Zuma', '祖玛');

