from sys import stdin
S = lambda:stdin.readline().strip()
def main():
    digit = S()
    res = sum(int(x) for x in digit if x.isdigit())
    print(res)
if __name__ == "__main__":
    main()