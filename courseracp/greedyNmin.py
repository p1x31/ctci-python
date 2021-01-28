import sys
n = int(input())
a = []
ans = sys.maxint
used = [False]*n
p[0] = 0
for i in range(n):
    a.append(i)

def rec(idx, len):
    if len >= ans:
        return
    if (idx == n):
        ans = min(ans, len + a[p[idx-1]][0])
        print(a)
        return
    for i in range(n):
        if (used[i]):
            continue
        p[idx] = i
        used[i] = True
        rec(idx+1, len + a[p[idx-1]][i])
        used[i] = False # free up the number after recursion return
rec(0)

def count(p):
    return p.sum()


rec(1,0)