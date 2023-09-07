#right
n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] + [float('inf')] * n
for i in range(n + 1):
    for j in a:
        if i >= j:
            dp[i] = min(dp[i], dp[i - j] + 1)
            

if dp[n] == float('inf') or sum(a)*2 < n:
    print(-1)
else:
    print(dp[n])
    while n > 0:
        for j in a:
            if dp[n - j] == dp[n] - 1:
                print(j, end=' ')
                n -= j
                break