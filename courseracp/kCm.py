n = int(input())
m = int(input())

a = ["."]*n
used = [False]*(n+1)
counter = 0
def rec(idx):
    global counter
    if (idx == n):
        counter +=1
        print(a, counter)
        return
        #print(used)
    for i in range(n):
        if (used[i]):
            continue
        a[idx] = '*'
        rec(idx+1)
        
rec(0)