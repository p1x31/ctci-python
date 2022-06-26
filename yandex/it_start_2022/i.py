from sys import stdin
I = lambda: int(stdin.readline().strip())
def main():
    i = I()
    # счастливый билет имеет вид: 666 666, т.е. сумма первый трех цифр равна сумме последних
    if sum(int(value) for key, value in enumerate(str(i)) if key >=3 ) == sum(int(value) for key, value in enumerate(str(i)) if key <3):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()