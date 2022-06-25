/*Find the makers producing PCs but not laptops. */
select distinct product.maker
from product
where product.type='PC' and
    product.maker not in (
    select product.maker
    from product
    where product.type = 'Laptop')