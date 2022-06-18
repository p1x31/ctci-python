from decimal import Decimal
from sys import stdin
M = lambda:map(Decimal, stdin.readline().strip().split())
def main():
    r, h = M()
    pi = 3.14
    s = 2 * Decimal(pi) * r * (h + r)
    res = "{:.2f}".format(s)
    print(res)
if __name__ == "__main__":
    main()