from sys import stdin
I = lambda: int(stdin.readline().strip())
def main():
    i = I()
    #хотя бы одна цифра четная, и при этом средняя цифра равна сумме крайних
    if any(int(value) % 2 == 0 for key, value in enumerate(str(i))) and int(str(i)[1]) == int(int(str(i)[0]))+int(str(i)[2]):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()