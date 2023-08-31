n, t = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
count = 0
for i in range(n):
    if t >= a[i]:
        count += 1
        t -= a[i]
    else:
        break

print(count)