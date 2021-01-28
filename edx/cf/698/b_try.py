n = int(input())
d = int(input())
def partitions(n, I=d):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            if i % 10 == 7 and p[0] % 10 == 7:
                print(p)
                yield (i,) + p
partitions_all = list(partitions(n))
partitions_all.sort()
print(partitions_all)
counter = 0
for items in partitions_all: 
    print(items)
    counter += 1
    print(counter) 