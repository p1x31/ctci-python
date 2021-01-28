t = int(input())

for i in range(t):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    keys = ["key"]*n
    store = dict(zip(a, keys))
    def partitions(n, I=d):
        yield (n,)
        for i in range(I, n//2 + 1):
            for p in partitions(n-i, i):
                if i % 10 == 7 and p[0] % 10 == 7:
                    yield (i,) + p
    
    for value, key in store.items():
        if value % 10 == d:
            print("YES")
        else:
            partitions_all = list(partitions(value, d))
            if len(partitions_all) < 2:
                print("NO")
            else: 
                print("YES")
            
    