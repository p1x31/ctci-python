from sys import stdin,stdout
L = lambda: list(map(int, stdin.readline().strip().split()))
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()

def main():
    target = S()
    guess = S()

    target_list = list(target)
    guess_list = list(guess)
    # result = [None]*len(target)
    result = list()

    if guess == target:
        for _ in range(len(target)):
            print("correct", sep = "\n")
    else:
        for i, c in enumerate(guess_list):
            if c == target_list[i]:
                result.append('correct')
                guess_list[i] = "0"
                target_list[i] = "0"
            elif c in target_list:
                for j, d in enumerate(target_list):
                    if c == d and guess_list[j] != d and d != "0" or (guess_list[target_list.index(c)] != target_list[target_list.index(c)]):
                        result.append('present')
                        guess_list[i] = "0"
                        target_list[j] = "0"
                        break
                    elif (c not in target_list or (guess_list[target_list.index(c)] == target_list[target_list.index(c)])) and d != "0":
                        result.append('absent')
                        guess_list[i] = "0"
                        break
            elif c not in target_list:
                result.append('absent')
                guess_list[i] = "0"
                   
    print(*result, sep = "\n")

if __name__ == "__main__":
    main()   