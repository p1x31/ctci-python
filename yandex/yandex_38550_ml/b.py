from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
import numpy as np
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))
#_________________________________________________#

def calc_top(x, y, x_prev, y_prev):
    return np.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2)

def calc_bottom(x, y, x_prev, y_prev, x_next, y_next):
    res = 0
    res += np.sqrt((x - x_prev) ** 2 + (y_prev - y) ** 2)
    res += np.sqrt((x_next - x) ** 2 + (y_next - y) ** 2)
    return res



def main():
    n = I()
    res = 0
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    x_low = 0
    y_low = 0
    for i in range (1, n + 1):
        x[i], y[i] = M()
        if y[i - 1] < y[i]:
            res += calc_top(x[i], y[i], x[i - 1], y[i - 1]) 
            if x_low != 0:
                res = res + np.sqrt((x[i] - x_low) ** 2 + (y[i] - y_low) ** 2)
        else:
            res += np.sqrt((x[i] - x[i - 1]) ** 2 + (y[i - 1] - y[i]) ** 2)
            x_low = x[i]
            y_low = y[i]
            x[i], y[i] = x[i - 1], y[i - 1]
    res = "{:.12f}".format(res)
    print(res)
if __name__ == "__main__":
    main()   