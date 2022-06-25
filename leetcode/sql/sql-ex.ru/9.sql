/*Find the makers of PCs with a processor speed of 450 MHz or more. Result set: maker. */
SELECT DISTINCT Maker
FROM product inner join PC ON product.model=pc.model AND PC.speed>=450