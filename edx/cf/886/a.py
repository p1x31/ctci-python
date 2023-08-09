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
        a, b, c = M()

        if a + b >= 10 or a + c >= 10 or b + c >= 10:
            print("YES")
        else:
            print("NO")

def main():
   solve()

if __name__ == "__main__":
    main()   
    