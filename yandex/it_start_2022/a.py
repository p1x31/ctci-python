from decimal import Decimal
from sys import stdin
I = lambda: int(stdin.readline().strip())
def main():
    s = I()
    res = 3 * s - 2
    # pi = 3.14
    # s = 2 * Decimal(pi) * r * (h + r)
    # res = "{:.2f}".format(s)
    print(res)
if __name__ == "__main__":
    main()