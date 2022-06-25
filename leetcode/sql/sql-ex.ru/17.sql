/*Get the laptop models that have a speed smaller than the speed of any PC.
Result set: type, model, speed.*/
select distinct p.type,p.model,l.speed 
from laptop l 
join product p on l.model=p.model 
where l.speed<(select min(speed) 
                      from pc)