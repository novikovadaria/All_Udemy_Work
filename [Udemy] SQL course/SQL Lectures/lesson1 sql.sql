-- Example 1
/* CRUD Operations
Create --->>  The INSERT statement
Read ---->>   The SELECT statement
Update ---->> The UPDATE statement
Delete ---->> The DELETE statement
*/

-- Example 1
USE dasha_db;
SELECT * 
FROM countries;

-- Example 2
SELECT country_name
From countries;

-- Example 3
SELECT country_name, region_id
From countries;

-- Example 4
SELECT distinct manager_id
FROM employees;

-- -------------------------INSERT statement---------------------- 
-- Example 1 ---->> adding a single record
INSERT INTO countries
VALUE ('AF', 'Afganistan', '1001');

-- Example 2 ---->> adding a single record
INSERT INTO countries (country_id, country_name, region_id)
VALUE ('NZ', 'New Zeland', '9009');

-- Example 3
-- Example 1 ---->> adding a single record
INSERT INTO countries
VALUE ('CS', 'Cats', '2002');
INSERT INTO countries
VALUE ('DG', 'Dogs', '3003');

-- ----------------------------------UPDATE statement--------------------------
-- Example 1 ---->>> apdating a single record
UPDATE departments
SET department_name = 'Web Development', location_id = 9009
WHERE department_id = 1;

-- Example 2---->>> apdating multiple records
UPDATE departments
SET city = 'Kabul'
WHERE country_id = 'US';

-- Example 2---->>> apdating all records
UPDATE locatins
SET city = 'Krasnodar';

-- --------------------------------------DELETE statement-------------------------
-- Example 1 --->> deleting a single record
DELETE
FROM regions 
WHERE region_id = 2;

-- Example 2 --->> deleting all record
DELETE
FROM regions;

-- Colon names/ in order to not to use USE statement and -- Aliasing Table Names
-- Example 1
SELECT c.countrie_id, c.country_name
FROM countries c;


