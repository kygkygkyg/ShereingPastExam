CREATE TABLE IF NOT EXISTS `users` (
    `id`               INT(20) AUTO_INCREMENT PRIMARY KEY,
    `user_name`        VARCHAR(20) UNIQUE NOT NULL,
    `created_at`       Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at`       Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    -- PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

-- sample data --
INSERT INTO users (user_name) VALUES ('YUGA TARO');