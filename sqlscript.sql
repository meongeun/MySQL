DROP DATABASE IF EXISTS estate_db;
CREATE DATABASE estate_db DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

USE estate_db;
DROP TABLE IF EXISTS estate_db.estate;
CREATE TABLE estate_db.estate (
    estate_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    price INT NOT NULL,
    year CHAR(4) NOT NULL,
    dong VARCHAR(30) NOT NULL,
    apartname VARCHAR(30) NOT NULL,
    month CHAR(2) NOT NULL,
    day CHAR(5) NOT NULL,
    space VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    addresscode CHAR(5) NOT NULL,
    floor CHAR(3) NOT NULL,
    PRIMARY KEY(estate_id)
)
