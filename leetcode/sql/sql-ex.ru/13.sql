/*Find out the average speed of the PCs produced by maker A. */
SELECT AVG(speed)
FROM PC
JOIN Product on PC.model = Product.model
WHERE Product.maker = 'A'