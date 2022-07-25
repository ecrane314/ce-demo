CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS test.example_table (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
text_col VARCHAR(50),
int_col INT,
created_at TIMESTAMP
);
INSERT INTO test.example_table (text_col, int_col, created_at) VALUES
('hello', 0, '2020-01-01 00:00:00'),
('goodbye', 1, NULL),
('name', -987, NOW()),
('other', 2786, '2021-01-01 00:00:00');