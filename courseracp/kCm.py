n = int(input())
k = int(input())

a = ["."]*n
used = [False]*(n+1)
counter = 0
def rec(idx):
    global counter
    if (idx == k):
        counter +=1
        print(a, counter)
        return
        #print(used)
    for i in range(k):
        if (used[i]):
            continue
        a[i] = '*'
        used[i] = True
        used[idx+1] = True
        rec(idx+1)
        used[idx] = False
rec(0)