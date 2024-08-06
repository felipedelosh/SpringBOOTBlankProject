DROP TABLE IF EXISTS example;
CREATE TABLE examples (
	id character varying(255) PRIMARY KEY,
	name character varying(255) NOT NULL
);


INSERT INTO examples (id, name) VALUES
('1A', 'example 01'),
('2B', 'example 02'),
('3C', 'example 03'),
('4D', 'example 04'),
('5E', 'example 05'),
('6F', 'example 06'),
('7G', 'example 07'),
('8H', 'example 08'),
('9I', 'example 09');

COMMIT;
