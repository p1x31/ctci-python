t = int(input())

for i in range(t):
    w, h, n = map(int,input().split())
    res = 1
    while (w % 2 == 0):
        res *= 2
        w /= 2
    while (h % 2 == 0):
        res *= 2
        h /= 2
    if (res >= n):
        print("YES")
    else:
        print("NO")
