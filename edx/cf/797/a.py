import math
t = int(input())

for _ in range(t):
    n = int(input())
    if (n % 3) == 0:
        y = n / 3 + 1
        x = n / 3
        z = n / 3 - 1
    else:
        x = (n // 3) 
        z = x - 1 
        y = n - x - z
        if x + 2 < y:
            x += 1
            y -=1
    print(int(x), int(y), int(z))