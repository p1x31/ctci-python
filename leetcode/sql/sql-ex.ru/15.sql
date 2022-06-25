/*Get hard drive capacities that are identical for two or more PCs.
Result set: hd. */
Select PC.hd From PC
group by PC.hd
Having Count(PC.hd) >= 2
