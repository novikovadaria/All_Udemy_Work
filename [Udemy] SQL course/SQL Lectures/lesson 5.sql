USE dasha_db;
-- --------------------------CREATING DATABASE-----------------------------------
-- Example 1
-- CREATE DATABASE first_attempt;

-- USE keyword
-- Example 2
-- USE first_attempt;

-- Example 3
-- SELECT * 
-- FROM first_attempt.lessons l;

-- ---------------------------CREATING TABLE---------------------------
-- ---------------------------NULL------------------------------
-- ---------------------------PRIMARY KEY---------------------------------
-- ---------------------------CONSTRAINTS----------------------------
-- CREATE TABLE students 
-- (
-- student_id INTEGER,
-- first_name VARCHAR (100) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- CONSTRAINT
-- PK_student_id
-- PRIMARY KEY 
-- (student_id)
-- );

-- -------------------------------ALTER TABLE---------------------------------
-- ALTER TABLE
-- email_address
-- ADD CONSTRAINT
-- email_address_student_id
-- FOREIGN KEY
-- (email_address_student_id)
-- REFERENCES 
-- students
-- (student_id);

-- ----------------------------DROP TABLE-------------------------------------
-- Example 1
-- DROP TABLE button

-- Example 2
-- DROP TABLE students;

-- ---------------------------CREATING TABLE part 2--------------------------
USE dasha_db;
-- Example 1 ---->> NOT RECOMMENDED
-- CREATE TABLE students
-- (
-- student_id INTEGER NOT NULL PRIMARY KEY,
-- first_name VARCHAR(50),
-- last_name VARCHAR(50)
-- );

-- CREATE TABLE email_address
-- (
-- email_address_id INTEGER NOT NULL PRIMARY KEY,
-- email_address VARCHAR(50),
-- email_address_student_id INTEGER,

-- CONSTRAINT
-- FK_email_address_student_id
-- FOREIGN KEY
-- (FK_email_address_student_id) 
-- REFERENCES 
-- students
-- );

-- Example 2 ---->> RECOMMENDED
CREATE TABLE students
(
student_id INTEGER NOT NULL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50)
);

CREATE TABLE email_address
(
email_address_id INTEGER NOT NULL PRIMARY KEY,
email_address VARCHAR(50),
email_address_student_id INTEGER
);

ALTER TABLE
email_address
ADD CONSTRAINT 
FK_email_address_student_id
FOREIGN KEY
(FK_email_address_student_id)
REFERENCES
students
(student_id);

