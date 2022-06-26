from sys import stdin
I = lambda: int(stdin.readline().strip())
def main():
    a = I()
    if a == 1:
        print(0)
    else:
        print(a // 2)
if __name__ == "__main__":
    main()