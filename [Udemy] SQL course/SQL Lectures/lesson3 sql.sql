-- -------------------------------ORDER BY Clause-------------------------
-- Example 1
SELECT e.first_name, e.last_name, e.salary
FROM employees e
ORDER BY e.salary;

-- Example 2
SELECT c.country_name
FROM countries c
ORDER BY c.country_name;

-- ---------------------------Set Functions----------------------------
/* Set Functions
COUNT()
MAX()
MIN()
AVG()
SUM()
*/

-- Example 1 ---->> COUNT()
SELECT COUNT(*)
FROM employees;

-- Example 2 
SELECT COUNT(e.phone_number)   -- WITHOUT NULL
FROM employees e;

-- Example 3 
SELECT COUNT(e.first_name) 
FROM employees e
WHERE e.salary > 10000;

-- Example 1 ---->> MAX()
SELECT MAX(e.salary) 
FROM employees e;

-- Example 1 ---->> MIN()
SELECT MIN(e.salary) 
FROM employees e;

-- Example 1 ---->> AVG() # ONLY WITH NUM
SELECT ROUND(AVG(e.salary))
FROM employees e;

-- Example 1 ---->> SUM() # ONLY WITH NUM
SELECT SUM(e.salary) 
FROM employees e;

-- --------------------------------Set Functions with qualifiers------------------
-- Example 1
SELECT COUNT(DISTINCT l.country_id)
FROM locations l;

-- ------------------------------GROUP BY clause-----------------------------------
-- Example 1
SELECT COUNT(l.country_id), l.country_id
FROM location l
GROUP BY l.country_id;

-- ---------------------------------HAVING Clause-------------------------
-- Example 1
SELECT COUNT(l.country_id), l.country_id
FROM locations l
GROUP BY country_id
HAVING l.country_id = 'US';

-- Example 2
SELECT COUNT(l.country_id), l.country_id
FROM locations l
GROUP BY country_id
HAVING COUNT(l.country_id) > 1;

-- Example 3
SELECT COUNT(l.country_id) as countryID, l.country_id
FROM locations l
GROUP BY country_id
HAVING countryID >= 2;

-- ------------------------------CROSS JOIN--------------------------
-- Example 1
SELECT e.firts_name, e.last_name, d.deartment_name
FROM employees e, departments d;

-- -----------------------------INNER JOIN------------------------------
-- Example 1
SELECT e.first_name, e.last_name, d.department_name
FROM employees e INNER JOIN departments d ON e.department_id = d.department_id;

-- ----------------------------LEFT OUTER JOIN-----------------------------
-- Example 1
SELECT e.firts_name,e.last_name, d.department_name, d.department_id
FROM employees e  LEFT OUTER JOIN departments d ON e.department_id = d.department_id;
-- ----------------------------RIGHT OUTER JOIN---------------
-- Example 1
SELECT e.firts_name,e.last_name, d.department_name, d.department_id
FROM employees e  RIGHT OUTER JOIN departments d ON e.department_id = d.department_id;



