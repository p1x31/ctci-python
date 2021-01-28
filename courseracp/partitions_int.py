n = int(input())
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p
partitions_all = list(partitions(n))
partitions_all.sort()
counter = 0
for items in partitions_all: 
    print(items)
    counter += 1
    print(counter) 
