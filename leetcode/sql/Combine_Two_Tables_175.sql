
SELECT firstName, lastName, city, state
FROM Person as p
LEFT JOIN Address a ON p.personId = a.personId 