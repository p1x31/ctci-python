n = int(input())
# every number appear only once
a = []
used = [False]*n
for i in range(n):
    a.append(i)
counter = 0
def rec(idx):
    global counter
    if (idx == n):
        counter +=1
        print(a, counter)
        return
    for i in range(n):
        if (used[i]):
            continue
        a[idx] = i
        used[i] = True
        rec(idx+1)
        used[i] = False # free up the number after recursion return
rec(0)