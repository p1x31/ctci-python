from collections import Counter
n = int(input())
a = list() 
for _ in range(n):
    a.append(str(input()))
    c = Counter(a)
print(len(c.values()))