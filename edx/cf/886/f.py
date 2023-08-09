from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def max_frogs_caught(n, hops):
    hops.sort(reverse=True)
    max_count = 0

    for i in range(1, n+1):
        count = 0
        for j in range(n):
            if (j + 1) * hops[j] >= i:
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count


def solve():
    
    t = I()

    for _ in range(t):
        n = I()
        hops = L()

        result = max_frogs_caught(n, hops)
        print(result)

def main():
   solve()

if __name__ == "__main__":
    main()   
