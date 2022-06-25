from sys import stdin
#L = lambda: list(map(int, stdin.readline().strip().split()))
#I = lambda: int(stdin.readline().strip())
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
        for i in range(len(guess)):
            if guess_list[i] == target[i]:
                result.append('correct')
                guess_list[i] = "0"
                target_list[i] = "0"
            elif guess_list[i] in target_list and guess_list[i] != 0:
                j = 0
                count_diff = 0
                while j < len(target_list):
                    if target_list[j + count_diff] == guess_list[i] and \
                    target_list[j + count_diff] != guess_list[j + count_diff]:
                        result.append('present')
                        guess_list[j] = "0"
                        target_list[count_diff] = "0"
                        j += 1
                        count_diff = 0
                        break
                    else:
                        count_diff += 1
                        if count_diff >= len(target_list):
                            result.append('absent')
                            guess_list[i] = "0"
                            break
            else:
                result.append('absent')
                guess_list[i] = "0"       
    print(*result, sep = "\n")

if __name__ == "__main__":
    main()   