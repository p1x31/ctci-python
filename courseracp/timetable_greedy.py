import numpy as np
d = []
c = []
summ = 0 
n = int(input())
for line in open('schedule2.in'):
    xx, yy = map(int, line.split())
    d.append(xx)
    c.append(yy)
print(d)
used = [False] * n
for i in range(n):
    d_i , c_i = map(int, input().split())
    d.append(d_i)
    c.append(c_i)
    k = d[i]
    while (k >= 1 and used[k]):
        k -= 1
    if (k == 0):
        continue
    used[k] = True
    summ += c[i]
print(summ)