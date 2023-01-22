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
    #s = S()
    s = input().strip().split("+")
    #print(type(s))
    res = sorted(s)
    print(*res, sep="+")

def main():
   solve()

if __name__ == "__main__":
    main()   
    
