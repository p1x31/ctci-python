n, m = map(int,input().split())
a = list() 
for i in range(n):
    a.append(int(input()))

counter = 0    
def rec(idx):
    global counter
    if (idx == n):
        counter +=1
        print(a, counter)
        return 
    for i in range(1,m+1):
        if a[idx] != a[i]:
            print(idx)
        else:
            continue
        rec(idx+1)
