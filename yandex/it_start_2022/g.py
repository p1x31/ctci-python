from sys import stdin
M = lambda: map(int, stdin.readline().strip().split())
def main():
    a, b, c, d = M()
    print(a, d)
    
if __name__ == "__main__":
    main()