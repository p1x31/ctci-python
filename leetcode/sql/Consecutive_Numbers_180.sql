# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums 
FROM Logs
where (Id + 1, num) in (SELECT * from Logs) and (Id + 2, num) in (select * from Logs);