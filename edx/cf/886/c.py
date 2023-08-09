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
        grid = [input() for _ in range(8)]
        word = ""

        for col in range(8):
            for row in range(8):
                if grid[row][col] != '.':
                    word += grid[row][col]

        print(word)

def main():
   solve()

if __name__ == "__main__":
    main()   
