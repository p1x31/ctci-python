/*Get the models and prices for all commercially available products (of any type) produced by maker B. */
SELECT * FROM (SELECT model, price 
 FROM PC
 UNION
 SELECT model, price 
 FROM Laptop
 UNION
 SELECT model, price 
 FROM Printer
 ) AS a
WHERE a.model IN (SELECT model 
 FROM Product 
 WHERE maker = 'B'
 )
