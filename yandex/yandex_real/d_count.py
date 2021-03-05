import sys
n = int(input())
chrCounter = 0
a = {None}
#for line in sys.stdin:
for _ in range(n):
    a.add(str(input().split()))
print(len(a)-1)
