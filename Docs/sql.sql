CREATE TABLE examples (
	id character varying(255) PRIMARY KEY,
	name character varying(255) NOT NULL
);


INSERT INTO examples (id, name) VALUES
('1', 'a'),
('2', 'b'),
('3', 'c'),
('4', 'd'),
('5', 'e'),
('6', 'f'),
('7', 'g'),
('8', 'h'),
('9', 'i');

COMMIT;
