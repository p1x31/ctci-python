from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))
#_________________________________________________#

def main():
    n = I()
    #ill or not
    a = L()
    res = list()
    meeting = defaultdict(list)
    for i in range (n):
        meeting_read = L()
        meeting[i].append(meeting_read)
    for key, value in enumerate(a):
        if value == 1:
            res.append(value)
            continue
        else:
            for i in range(len(meeting)):
                if len(set(meeting[key][0][1:])) == 0:
                    res.append(value)
                    break
                elif (len(set(meeting[key][0][1:]) & set(meeting[i][0][1:])) != 0):
                    if (value != a[i]):
                        res.append(value | a[i])
                        break
                    elif (value == a[i]):
                        res.append(value)
                        break  
    print(*res)
if __name__ == "__main__":
    main()   