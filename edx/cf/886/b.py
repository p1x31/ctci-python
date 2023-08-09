from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def solve():
    
    t = I()

    for _ in range(t):
        n = I()
        responses = []

        for i in range(n):
            a, b = M()
            responses.append((a, b))

        max_quality = 0
        winner = -1

        for i in range(n):
            a, b = responses[i]
            if a <= 10 and b > max_quality:
                max_quality = b
                winner = i + 1

        print(winner)

def main():
   solve()

if __name__ == "__main__":
    main()   


