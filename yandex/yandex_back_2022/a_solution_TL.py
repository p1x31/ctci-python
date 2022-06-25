from sys import stdin,stdout
L = lambda: list(map(int, stdin.readline().strip().split()))
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()

def solve():
    # Example code
    target = S()
    guess = S()
    
    # lst = []
    # letters = set(target)

    #multiples guesses
    #for char in guess:
    # print (*["correct" if a==b else                # identical
    #         "present" if b in letters else        # somewhere in word
    #         "absent" for a,b                     # not in word
    #         in zip(target, guess)], sep="\n") # for all letter-tuples
    target_list = list(target)
    guess_list = list(guess)
    result = [None]*len(target)
    for i, c in enumerate(guess_list):
        if c == target[i]:
            result.insert(i, 'correct')
            guess_list[i] = "0"
            target_list[i] = "0" 
            result = result[:-1]
        else:
            continue
    # print(result)
    # print("res:", target_list)
    # print("res:", guess_list)
    for i, c in enumerate(guess_list):
        if c in target_list and c != "0":
            result.insert(i, 'present')
            result = result[:-1]
            guess_list[i] = "0"
            target_list[target_list.index(c)] = "0"
        elif c == "0":
            continue
        else:
            result.insert(i, 'absent')
            result = result[:-1]
    result = ['correct' if v is None else v for v in result]
    #filtered_result = list(filter(None, result))
    print(*result, sep = "\n")
    

def main():
    target = S()
    guess = S()

    # target_list = list(target)
    # guess_list = list(guess)
    # result = [None]*len(target)
    result = list()
    xs = list(target)
    ys = list(guess)
    set_target = set(target)


    for x, y in zip(xs, ys):
        count_diff = 0
        if x == y:
            
            result.insert(xs.index(x), 'correct') # insert at index
            xs[xs.index(x)] = "0" # replace with 0
            ys[ys.index(y)] = "0" # replace with 0
        #elif y in xs and any(y != ys[xs.index(y)] for y in ys):
        # elif y in xs and y != ys[xs.index(y)]: # for each y in xs check y != ys[xs.index(y)] (x[, i[, j]])
        #     print(xs[xs.index(y)]) 
        #     print(ys[xs.index(y)])
        #     result.insert(ys.index(y), "present")
        #     xs[xs.index(y)] = "0"
        #     ys[ys.index(y)] = "0"
        elif any((y == xs[i] and xs[i] != ys[i]) for i in range(len(xs))) :
            print("target element: ", xs[xs.index(x)])
            print("guess element" , ys[xs.index(x)])
            result.insert(ys.index(y), "present")
            xs[xs.index(x)] = "0"
            ys[ys.index(y)] = "0"
            print(result)
        else:
            result.insert(ys.index(y), 'absent')
            ys[ys.index(y)] = "0"
        # else:
        #     result.insert(ys.index(y), "present")
        #     ys[ys.index(y)] = "0"

    print(*result, sep = "\n")

    # for i, c in enumerate(guess_list):
    #     if c == target[i]:
    #         result.insert(i, 'correct')
    #         guess_list[i] = "0"
    #         target_list[i] = "0" 
    #         result = result[:-1]
    #     else:
    #         continue
    
    # for i, c in enumerate(guess_list):
    #     if c in target_list and c != "0":
    #         result.insert(i, 'present')
    #         result = result[:-1]
    #         guess_list[i] = "0"
    #         target_list[target_list.index(c)] = "0"
    #     elif c == "0":
    #         continue
    #     else:
    #         result.insert(i, 'absent')
    #         result = result[:-1]
    # result = ['correct' if v is None else v for v in result]
    # print(*result, sep = "\n")

if __name__ == "__main__":
    main()   