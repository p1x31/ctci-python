def steal_money(target, denominations):
    dp = [0] + [-1] * target
    
    for i in range(1, target + 1):
        for denom in denominations:
            if i - denom >= 0 and dp[i - denom] != -1:
                dp[i] = denom
                break
    
    if dp[target] == -1:
        return -1
    
    result = []
    while target > 0:
        result.append(dp[target])
        target -= dp[target]
    
    return result

# Read input
n, m = map(int, input().split())
denominations = sorted(map(int, input().split()))

# Try to steal the money
stolen_money = steal_money(n, denominations)

# Print the result
if stolen_money == -1:
    print(-1)
else:
    print(len(stolen_money), *stolen_money)