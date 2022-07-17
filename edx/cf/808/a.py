from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))
#_________________________________________________#
        
def solve():
    # Example code
    n = I()
    a = L()
    
    for i in range(1, n):
        if a[i] % a[0] != 0:
            print("NO")
            return
    print("YES")

def main():
    for _ in range(I()):
        solve()

if __name__ == "__main__":
    main()   