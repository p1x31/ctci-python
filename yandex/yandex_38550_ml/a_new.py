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
# В первой строке содержится одно число n(3≤n≤105) количества работников.
# Во второй строке содержится n чисел, равное количеству результатов тестов в конце рабочего дня.
# ai - 1 в случае, если человек болел на момент начала рабочего дня, в противном случае 0.
# Далее следует n строк.
# Первое число ki(0≤ki≤105) равное количеству встреч, которое посетил сотрудник.
# Далее через пробел перечислены порядковые номера встреч meetingi(1≤meetingi≤109) - номера встреч.
# Чем меньше номер, тем раньше была встреча, при этом некоторые встречи могли не состояться (номеров таких встреч не будет ни у одного работника).
# Гарантируется, что сумма всех ki не превышает 105
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
            if len(set(meeting[key][0][1:])) == 0:
                res.append(value)
                continue
            elif any([len(set(meeting[key][0][1:]) & set(meeting[i][0][1:])) != 0 and (value != a[i]) for i in range(len(meeting))]):
                res.append(value | 1)
                a[key] = 1
                continue
            else:
                res.append(value)
                continue
    print(*res)

if __name__ == "__main__":
    main()   