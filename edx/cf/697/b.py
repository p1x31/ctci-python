t = int(input())

for i in range(t):
    n = int(input())
    Q = n / 2020
    R = n % 2020
    print("YES" if Q >= R else "NO")