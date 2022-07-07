from sys import stdin,stdout
from collections import Counter,deque,defaultdict
import itertools

#input_file = "./input_file"

#minimum sum window substring of statue_type such that every character in k (including duplicates) is included in the window

def solve(n, k, statue_type):

   # M = lambda: map(int, fr.readline().strip().split())   
    #L = lambda: list(map(int, fr.readline().strip().split()))
    #n, k = M()
    #print(n,k)
    #statute_type = L()
    #n, k = map(int, s.strip().split())
    #statue_type =  list(map(int, t.strip().split()))
    countT = defaultdict(int)
    window = {}
    #countT, window = {}, {}
    min_sum = float("inf")
    for c in range(1, k + 1):
        #countT[c] = countT.get(c, 0) + 1
        countT[c] = 1
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("inf")
    l = 0
    for r in range(len(statue_type)):
        c = statue_type[r]
        window[c] = window.get(c, 0) + 1

        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            #update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            min_sum = min(sum(statue_type[l:r + 1]), min_sum)
            #remove the leftmost character
            window[statue_type[l]] -= 1
            if statue_type[l] in countT and window[statue_type[l]] < countT[statue_type[l]]:
                have -= 1
            l += 1
    l, r = res
    res = min_sum
    #res = min(min_sum, sum(statute_type[l:r + 1])) if resLen != float("inf") else ""
    return res


def main():
    yandex = True
    input_file = "/home/vadim/Documents/ctci-python/yandex/yandex_audio_28413_ml/input_file"
    if (yandex): input_file = "input.txt"

    with open(input_file, "rb") as fr:
        with open("output.txt", "wb") as fw:
            for line1,line2 in itertools.zip_longest(*[fr]*2):
                n, k = map(int, line1.strip().split())
                statue_type = list(map(int, line2.strip().split()))
                #if not line1 or line2: break
                fw.write((str(solve(n, k, statue_type)) + "\n").encode())
            fw.close()
    fr.close()
            
           
            # output_file = "/home/vadim/Documents/ctci-python/yandex/yandex_audio_28413_ml/output.txt"
            # if (yandex): output_file = "output.txt"
            # with open(output_file, "w") as fw:
            #     fw.write(str(res) + '\n')
                
               


if __name__ == "__main__":
    main()   
       