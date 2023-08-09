from sys import stdin
import math
I = lambda: int(stdin.readline().strip())

def is_prime(n):
    if n < 2:
        return False
    sq = int(math.sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = I()
    print(str(is_prime(n)).lower())
if __name__ == "__main__":
    main()

# function that determines is the number is prime

def is_prime2(n):
    if n < 2:
        return False
    sq = int(math.sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True