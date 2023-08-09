from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def min_problems_to_remove(n, k, difficulties):
    difficulties.sort()
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if difficulties[i] - difficulties[i - 1] <= k:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return n - max_length

def solve():
    
    t = I()

    for _ in range(t):
        n, k = M()
        difficulties = L()

        result = min_problems_to_remove(n, k, difficulties)
        print(result)

def main():
   solve()

if __name__ == "__main__":
    main()   




    