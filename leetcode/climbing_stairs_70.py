def climbStairs(n) -> int:
    # It takes n steps to reach the top.
    #Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
    if n == 1:
        return 1
    previous = 1
    current = 2
    for i in range(3, n + 1):
        previous, current = current, previous + current
    return current 

print(climbStairs(2))
print(climbStairs(3))