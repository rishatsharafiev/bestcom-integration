/* drop and create db */
DROP DATABASE IF EXISTS bestcom;
CREATE DATABASE bestcom CHARACTER SET utf8 COLLATE utf8_general_ci;
USE bestcom;

/* drop tables */
SET FOREIGN_KEY_CHECKS=0; 
DROP TABLE IF EXISTS itpartner_category;
DROP TABLE IF EXISTS itpartner_product;
DROP TABLE IF EXISTS itpartner_image;
SET FOREIGN_KEY_CHECKS=1;

/* drop indexes */
DROP INDEX IF EXISTS itpartner_product_category_id_idx;
DROP INDEX IF EXISTS itpartner_image_product_id_idx;

/* create itpartner_category table */
CREATE TABLE itpartner_category (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    parent_id INTEGER NULL
);


/* create itpartner_product table */
CREATE TABLE itpartner_product (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    part varchar(255) NOT NULL,
    sku INTEGER NOT NULL,
    vendor varchar(255) NOT NULL,
    volume DECIMAL(20,12) NOT NULL,
    has_image BOOLEAN DEFAULT FALSE,
    weight DECIMAL(20,12) NOT NULL,
    price DECIMAL(20,12) NOT NULL,
    qty varchar(255) NOT NULL,
    category_id INTEGER NULL,
    CONSTRAINT fk_categorys
        FOREIGN KEY (category_id)
        REFERENCES itpartner_category(id)
        ON DELETE CASCADE
);

/* create index on foreign key itpartner_product(category_id) */
CREATE INDEX itpartner_product_category_id_idx ON itpartner_product(category_id);

/* create itpartner_image table */
CREATE TABLE itpartner_image (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    url varchar(255) NOT NULL,
    product_id INTEGER NULL,
    CONSTRAINT fk_products
        FOREIGN KEY (product_id)
        REFERENCES itpartner_product(id)
        ON DELETE CASCADE
);

/* create index on foreign key itpartner_image(product_id) */
CREATE INDEX itpartner_image_product_id_idx ON itpartner_image(product_id);
