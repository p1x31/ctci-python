n = int(input())
bottom_up = []
def fib_dp(n):
    if n == 1 or n == 2:
        return 1
    bottom_up.append(0)
    bottom_up.append(1)
    for i in range(2,n+1):
        bottom_up.append(bottom_up[i-1] + bottom_up[i-2])
    return bottom_up[n]
print(fib_dp(n))