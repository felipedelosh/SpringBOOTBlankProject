DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id character varying(255) PRIMARY KEY,
	username character varying(255),
	contrasena character varying(255),
	name character varying(255),
	age integer
);

DROP TABLE IF EXISTS product;
CREATE TABLE product (
	id character varying(255) PRIMARY KEY,
	name character varying(255),
	price DOUBLE PRECISION
);

DROP TABLE IF EXISTS order;
CREATE TABLE order (
	id character varying(255) PRIMARY KEY,
	userId character varying(255),
	productIds String,
	status character varying(255)
);

DROP TABLE IF EXISTS example;
CREATE TABLE example (
	id character varying(255) PRIMARY KEY,
	name character varying(255)
);

