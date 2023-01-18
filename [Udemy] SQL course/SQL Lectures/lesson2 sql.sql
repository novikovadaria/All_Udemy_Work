-- Example 1
SELECT c.country_name
FROM countrie c
WHERE country_id = 'AU';

-- ---------------------------------AND Boolean Operator-------------------------
-- Example 1
SELECT e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE 
e.salary > 4000
AND
e.salary < 10000;

-- ----------------------------------OR Boolean Operator-----------------------
-- Example 1
SELECT e.first_name, e.last_name, e.email
FROM emoloyees e
WHERE 
e.salsry < 5000
or
e.salary > 15000;

-- --------------------------------------BEETWEN-----------------------------------
-- Example 1
SELECT d.department_name
FROM departments d
WHERE d.department_id
BETWEEN 
1 AND 5;

-- Example 2
SELECT j.job_title, j.min_salary
FROM job j
WHERE j.min_salary
BETWEEN 
10000 AND 20000;

-- -------------------------------------LIKE Boolean Operator--------------------------
-- Example 1
SELECT c.country_name
FROM countries c
WHERE c.country_name
LIKE 'A%';

-- Example 2
SELECT c.country_name
FROM countries c
WHERE c.country_name
LIKE 'a%';

-- Example 3
SELECT c.country_name
FROM countries c
WHERE c.country_name
LIKE '%m%';

-- Example 4
SELECT c.country_name
FROM countries c
WHERE c.country_name
LIKE '_w%';

-- ------------------------------IN Boolean Operator---------------------------------------
-- Example 1
SELECT e.first_name, e.last_name, e.hire_date
FROM employees e
WHERE e.manager_id
IN (100, 103, 108);

-- ------------------------------------IS Boolean Operator----------------------------------
-- Example 1
SELECT e.firts_name, e.last_name
FROM employee e
WHERE e.phone_number IS NULL;

-- ---------------------------IS NOT Boolean Operator------------------------------
SELECT e.firts_name, e.last_name
FROM empoloyees e
WHERE e.phone_number IS NOT NULL