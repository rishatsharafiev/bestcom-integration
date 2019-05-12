/* drop and create db */
DROP DATABASE IF EXISTS bestcom;
CREATE DATABASE bestcom CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
USE bestcom;

/* drop tables */
SET FOREIGN_KEY_CHECKS=0; 
DROP TABLE IF EXISTS itpartner_category;
DROP TABLE IF EXISTS itpartner_product;
DROP TABLE IF EXISTS itpartner_image;
SET FOREIGN_KEY_CHECKS=1;

/* drop indexes
DROP INDEX itpartner_product_category_id_idx ON itpartner_product;
DROP INDEX itpartner_image_product_id_idx ON itpartner_image;
*/

/* create itpartner_category table */
CREATE TABLE itpartner_category (
    id INTEGER NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    parent_id INTEGER NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);


/* create itpartner_product table */
CREATE TABLE itpartner_product (
    sku INTEGER NOT NULL PRIMARY KEY,
    name TEXT NULL,
    part varchar(255) NULL,
    vendor varchar(255) NULL,
    description TEXT NULL,
    volume DECIMAL(20,12) NULL,
    has_image BOOLEAN DEFAULT FALSE,
    weight DECIMAL(20,12) NULL,
    price DECIMAL(20,12) NULL,
    quantity varchar(255) NULL,
    min_quantity INTEGER NULL,
    category_id INTEGER NULL,
    is_deleted BOOLEAN DEFAULT FALSE,
    CONSTRAINT unique_idx_sku UNIQUE (sku)
);

/* create index on foreign key itpartner_product(category_id) */
CREATE INDEX itpartner_product_category_id_idx ON itpartner_product(category_id);

/* create itpartner_image table */
CREATE TABLE itpartner_image (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    url varchar(255) NOT NULL,
    product_sku INTEGER NULL
);

/* create index on foreign key itpartner_image(product_sku) */
CREATE INDEX itpartner_image_product_sku_idx ON itpartner_image(product_sku);
