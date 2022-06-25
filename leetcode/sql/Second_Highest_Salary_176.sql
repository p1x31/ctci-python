/* similar to 17 sql-ex.ru*/
SELECT max(salary) as SecondHighestSalary
FROM Employee
WHERE salary < (SELECT max(salary) FROM Employee)