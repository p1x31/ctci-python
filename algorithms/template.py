from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L=lambda:list(map(int, stdin.readline().strip().split()))
M=lambda:map(int, stdin.readline().strip().split())
I=lambda:int(stdin.readline().strip())
S=lambda:stdin.readline().strip()
C=lambda:stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))
#_________________________________________________#
        
def solve():
    # Example code
    q,d = M()
    a = L()
    for i in range(q):
        x = a[i]
        b = 0
        while x>=d:
            if str(d) in str(x):
                b = 1
                break
            x-=d
        if b:
            print("YES")
        else:
            print("NO")

def main():
    for _ in range(I()):
        solve()

if __name__ == "__main__":
    main()   
