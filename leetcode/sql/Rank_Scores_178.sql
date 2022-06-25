SELECT s.score, COUNT(s2.score) as "Rank" 
FROM Scores s, (SELECT DISTINCT score FROM Scores) as s2
WHERE s.score <= s2.score
GROUP BY s.id
ORDER BY s.score DESC