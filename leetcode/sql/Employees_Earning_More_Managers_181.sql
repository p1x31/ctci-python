# Write your MySQL query statement below
SELECT name as Employee
FROM Employee as e1
WHERE e1.salary > (SELECT e2.salary FROM Employee as e2
                   WHERE e1.managerId = e2.id)
               