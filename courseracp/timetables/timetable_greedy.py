#import numpy as np
#ставить каждый заказ на наиболее поздний день,
d = []
c = []
summ = 0 
n = int(input())
for line in open('schedule2.in'):
    xx, yy = map(int, line.split())
    d.append(xx)
    c.append(yy)

used = [False] * (n+1)
for i in range(n):
#    d_i , c_i = map(int, input().split())
#    d.append(d_i)
#    c.append(c_i)
    k = d[i] # date to do the order
    while (k >= 1 and used[k]):
        k -= 1
    if (k == 0):
        continue
    used[k] = True
    summ += c[i]
print(summ)