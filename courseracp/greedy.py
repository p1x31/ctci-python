n = int(input())
m = int(input())
from collections import defaultdict
store = defaultdict(list)
#for i in range(n):
#    a = list(map(int,input().split()))
a = []
for i in range(n):
    a.append(i)
counter = 0
def rec(idx):
    global counter
    if (idx == n):
        counter +=1
        print(a, counter)
        return 
    for i in range(1,m+1):
        a[idx] = i
        rec(idx+1)
rec(0)
