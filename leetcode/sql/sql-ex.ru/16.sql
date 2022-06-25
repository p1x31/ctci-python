/*Get pairs of PC models with identical speeds and the same RAM capacity. Each resulting pair should be displayed only once, i.e. (i, j) but not (j, i).
Result set: model with the bigger number, model with the smaller number, speed, and RAM. */

SELECT DISTINCT P.model, P1.model, P.speed, P.ram
FROM PC P, PC P1
WHERE P.speed = P1.speed 
AND P.ram = P1.ram
AND P.model > P1.model
ORDER BY P.model DESC