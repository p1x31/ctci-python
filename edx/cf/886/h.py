from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def check_partition(n, m, conditions):
    camps = [0] * n

    for i in range(m):
        a, b, d = conditions[i]
        if camps[a-1] != 0 and camps[b-1] != 0:
            if abs(camps[a-1] - camps[b-1]) != abs(d):
                return False
        elif camps[a-1] != 0:
            camps[b-1] = camps[a-1] + d
        elif camps[b-1] != 0:
            camps[a-1] = camps[b-1] - d

    return True

def solve():
    
    t = I()

    for _ in range(t):
        n, m = M()
        conditions = []

        for _ in range(m):
            a, b, d = M()
            conditions.append((a, b, d))

        if check_partition(n, m, conditions):
            print("YES")
        else:
            print("NO")

def main():
   solve()

if __name__ == "__main__":
    main()   
