from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))

def calculate_area(painting_sizes, w):
    total_area = 0
    for size in painting_sizes:
        total_area += (size + 2 * w) ** 2 - size ** 2
    return total_area

def find_w(painting_sizes, c):
    # Set the left and right bounds for the binary search
    left = 0
    right = 10**9

    # Perform binary search until the left and right bounds overlap
    while left < right:
        # Calculate the midpoint of the current left and right bounds
        mid = (left + right) // 2

        # Calculate the area using the given painting sizes and the current midpoint
        area = calculate_area(painting_sizes, mid)

        # Check if the calculated area is equal to the target area
        if area == c:
            # If the area is equal to the target area, return the current midpoint decreased by 1
            # If the current midpoint is already 1, return 1
            return mid - 1 if mid - 1 >= 1 else mid
        elif area < c:
            # If the calculated area is less than the target area, adjust the left bound to be the current midpoint + 1
            left = mid + 1
        else:
            # If the calculated area is greater than the target area, adjust the right bound to be the current midpoint
            right = mid

    # If the left and right bounds overlap, return the current left bound decreased by 1
    # If the current left bound is already 1, return 1
    return left - 1 if left - 1 >= 1 else left


def solve():
    
    t = I()

    for _ in range(t):
        n, c = M()
        sizes = L()

        result = find_w(sizes, c)
        print(result)

def main():
    solve()

if __name__ == "__main__":
    main()   

