from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_pairs(points):
    n = len(points)
    slopes = set()

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1

            if dx == 0:
                slope = float('inf')
            else:
                slope = dy / dx

            slopes.add(slope)

    return len(slopes)

def solve():
    
    t = I()

    for _ in range(t):
        n = I()
        points = [tuple(M()) for _ in range(n)]  # Coordinates of points

        result = count_pairs(points)
        print(result)


def main():
   solve()

if __name__ == "__main__":
    main()   

    