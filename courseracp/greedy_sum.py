n = int(input())
a = []
for i in range(n):
    a.append(i)
def rec(idx, current_sum, i):
    if (sum == n):
        print(a[idx])
        return
    for i in range(1,n-current_sum):
        a[idx] = i
        rec(idx + 1, current_sum + i, i)
    
rec(0,0,0)