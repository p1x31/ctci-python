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
    a = sorted([1,4,3,2,4], key=lambda x:-x, reverse=True) 
    print a

def main():
    for _ in range(I()):
        solve()

if __name__ == "__main__":
    main()   

# count from one to 100
