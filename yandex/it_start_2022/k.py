from sys import stdin
M = lambda: map(int, stdin.readline().strip().split())
def main():
    a, b, c = M()
    # if sum of two elemnents is equal or greater to third element
    if a+b>c and a+c>b and b+c>a:
        print("YES")
    else:
        print("NO")
    
    
if __name__ == "__main__":
    main()