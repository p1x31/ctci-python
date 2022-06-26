from decimal import Decimal
from sys import stdin
I = lambda: int(stdin.readline().strip())
def main():
    n = I()
    res = n % 3
    
    print(res)
if __name__ == "__main__":
    main()