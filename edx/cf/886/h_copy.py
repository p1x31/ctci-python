from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)
    return False

def check_partition(graph, n):
    visited = set()
    
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, set()):
                return "NO"

    return "YES"
def solve():
    
    t = I()

    for _ in range(t):
        n, m = M()
        graph = defaultdict(list)

        for _ in range(m):
            ai, bi, di = M()
            graph[bi].append((ai, di))

        result = check_partition(graph, n)
        print(result)

def main():
   solve()

if __name__ == "__main__":
    main()   
