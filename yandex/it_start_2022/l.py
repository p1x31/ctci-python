from sys import stdin
M = lambda: map(int, stdin.readline().strip().split())
def main():
    x, y = M()
    # if x or y is a three-digit number
    if (x>=100 and x<=999) or (y>=100 and y<=999):
        print("NO")
    else:
        print("YES")
    
if __name__ == "__main__":
    main()