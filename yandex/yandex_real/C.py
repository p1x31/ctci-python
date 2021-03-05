from collections import deque
n, m = map(int,input().split())
a = deque()
for i in range(n):
    a.append(int(input()))

def rec(idx, i):
   
    if (idx == m-1):
        print(a[idx-1], a[i])
        a.popleft()
        return
    for i in range(n):
        if (a[idx]==a[i]):
            continue
        a[idx] = a[i]
        
        rec(idx+1)
        
rec(0)