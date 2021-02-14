# Given n and k, return the kth permutation sequence.
n, k = map(int, input().split())
# every number appear only once
a = []
used = [False]*(n+1)
a = list(range(n))
global counter
counter = 0
answe = []
def rec(idx):
    global counter
    if (idx == n):
        global counter
        counter +=1
        if counter == k:
            ans = ''.join(str(x) for x in a)
            answe.append(ans)
            #ans = '"%s"' % ans
        return
    for i in range(1,n+1):
        if (used[i]):
            continue
        a[idx] = i
        used[i] = True
        rec(idx+1)
        used[i] = False # free up the number after recursion return
rec(0)
#return answe[0]