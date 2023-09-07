#right
n, s = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in range(n):
    if s >= a[i]:
        print(a[i])
        break
else:
    print(0)