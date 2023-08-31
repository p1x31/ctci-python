from sys import stdin
Ma = lambda: map(int, stdin.readline().strip().split())
L = lambda: list(map(int, stdin.readline().strip().split()))


def my_function(some_mass):
    # length = 0
    # while some_number > 5:
    #     length +=some_number
    #     some_number -= 2
    # return length
    # proceed = False
    # if some_number >= 80:
    #     proceed = True
    # return proceed
    # a = [2, 5, 7, 10]
    # b = []
    # for i in a:
    #     if some_number > i:
    #         b.append(i)
    # return b

    # letters = {
    #     0: "a",
    #     1: "v",
    #     2: "i",
    #     3: "t",
    #     4: "o",
    #     5: "q",
    # }
    # word = ""
    # for n in a:
    #     i = 10 -n 
    #     if i < 0:
    #         continue
    #     word += letters[i]
    # return word
    for i in range (4):
        for j in range(4):
            if i == j:
                some_mass[i][j] = 1
            else:
                continue
    return some_mass

def main():
    print(my_function([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))

if __name__ == "__main__":
    main()