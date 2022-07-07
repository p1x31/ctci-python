from sys import stdin,stdout
from collections import Counter,deque,defaultdict
import itertools

def main():
    M = lambda: map(int,stdin.readline().strip().split())   
    L = lambda: list(map(int, stdin.readline().strip().split()))
    n, k = M()
    statue_type = L()
    
    countT = defaultdict(int)
    window = {}
    #countT, window = {}, {}
    min_sum = float("inf")
    for c in range(1, k + 1):
        #countT[c] = countT.get(c, 0) + 1
        countT[c] = 1
    have, need = 0, len(countT)
    have, need = 0, k
    #res, resLen = [-1, -1], float("inf")
    res = [-1, -1]
    l = 0
    for r in range(len(statue_type)):
        c = statue_type[r]
        window[c] = window.get(c, 0) + 1

        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            #update our result
            # if (r - l + 1) < resLen:
            #     res = [l, r]
            #     resLen = r - l + 1
            min_sum = min(sum(statue_type[l:r + 1]), min_sum)
            #remove the leftmost character
            window[statue_type[l]] -= 1
            if statue_type[l] in countT and window[statue_type[l]] < countT[statue_type[l]]:
                have -= 1
            l += 1
    # l, r = res
    res = min_sum
    #res = min(min_sum, sum(statute_type[l:r + 1])) if resLen != float("inf") else ""
    print(res)
               


if __name__ == "__main__":
    main()   
       