
BEGIN;
CREATE TABLE `image` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1024) NOT NULL,
    `size` integer NOT NULL,
    `width` integer NOT NULL,
    `height` integer NOT NULL,
    `url` varchar(2048) NOT NULL
)
;
CREATE TABLE `tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL
)
;
CREATE TABLE `game_screens` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `image_id` integer NOT NULL,
    UNIQUE (`game_id`, `image_id`)
)
;
ALTER TABLE `game_screens` ADD CONSTRAINT `image_id_refs_id_6bf1c595` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`);
CREATE TABLE `game_rec_screens` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `image_id` integer NOT NULL,
    UNIQUE (`game_id`, `image_id`)
)
;
ALTER TABLE `game_rec_screens` ADD CONSTRAINT `image_id_refs_id_71b6857d` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`);
CREATE TABLE `game` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `create_time` datetime NOT NULL,
    `update_time` datetime NOT NULL,
    `name` varchar(1024) NOT NULL,
    `name_ch` varchar(1024) NOT NULL,
    `desc` longtext NOT NULL,
    `desc_ch` longtext NOT NULL,
    `icon_id` integer NOT NULL,
    `flash_url` varchar(2048) NOT NULL,
    `ipa_url` varchar(2048) NOT NULL,
    `apk_url` varchar(2048) NOT NULL
)
;
ALTER TABLE `game` ADD CONSTRAINT `icon_id_refs_id_b002a7ad` FOREIGN KEY (`icon_id`) REFERENCES `image` (`id`);
ALTER TABLE `game_screens` ADD CONSTRAINT `game_id_refs_id_47c1073b` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
ALTER TABLE `game_rec_screens` ADD CONSTRAINT `game_id_refs_id_2578428e` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
CREATE TABLE `game_tag_maps` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `game_id` integer NOT NULL,
    `tags_id` integer NOT NULL
)
;
ALTER TABLE `game_tag_maps` ADD CONSTRAINT `tags_id_refs_id_3029c852` FOREIGN KEY (`tags_id`) REFERENCES `tag` (`id`);
ALTER TABLE `game_tag_maps` ADD CONSTRAINT `game_id_refs_id_69e2c904` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);
CREATE INDEX `game_465cb59b` ON `game` (`icon_id`);
CREATE INDEX `game_tag_maps_65e12249` ON `game_tag_maps` (`game_id`);
CREATE INDEX `game_tag_maps_d03bd400` ON `game_tag_maps` (`tags_id`);

COMMIT;

USE ysgk;
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