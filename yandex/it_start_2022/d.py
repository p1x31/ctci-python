from sys import stdin
I = lambda: int(stdin.readline().strip())
M = lambda: map(int, stdin.readline().strip().split())
def main():
    x, a, b, c = M()
    #if a, b or c smaller than x
    if a >= x and b >= x and c >= x:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()