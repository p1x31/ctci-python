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
    n, l, r = M()
    out = []
    flg = 'YES'
    ans = []
    used = set()
    for i in range(1, n + 1)[::-1]:
        x = l + (i - l % i) % i
        if x <= r:
            ans.append(x)
            used.add(x)
        else:
            flg = "NO"
            break
    if flg == "NO":
        out.append([flg])
    else:
        out.append([flg])
        out.append(ans[::-1])
     
    for o in out:
        print(*o)

    

def main():
    for _ in range(I()):
        solve()

if __name__ == "__main__":
    main()   