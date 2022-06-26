from sys import stdin
M = lambda: map(int, stdin.readline().strip().split())
def main():
    a, b, c, d = M()
    # if either a or b equals to either c or d
    if (a == d and b + c == a) or (b == c and (a + d == b)):
        print("YES")
    else:
        print("NO")
    
if __name__ == "__main__":
    main()