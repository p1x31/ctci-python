import sys
t = int(input())

for i in range(t):
    n = int(input())
    while (n % 2 == 0):
        n /= 2
    print ("YES" if n > 1 else "NO") 