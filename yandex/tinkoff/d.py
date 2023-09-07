n, m = map(int, input().split())
a = list(map(int, input().split()))

if n > sum(a)*2:
    print(-1)
else:
    b = [0] * (n // 2)
    for i in range(m):
        if a[i] <= n and b[n // 2 - a[i] // 2] == 0:
            b[n // 2 - a[i] // 2] = a[i]
            if sum(b) == n:
                print(len(b), end=' ')
                for j in range(len(b)):
                    print(b[j], end=' ')
                break
    else:
        print(-1)