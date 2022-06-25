from sys import stdin,stdout
L = lambda: list(map(int, stdin.readline().strip().split()))
I = lambda: int(stdin.readline().strip())
        
def solve():
    # Example code
    q,d = M()
    a = L()
    for i in range(q):
        x = a[i]
        b = 0
        while x>=d:
            if str(d) in str(x):
                b = 1
                break
            x-=d
        if b:
            print("YES")
        else:
            print("NO")

def main():
    for _ in range(I()):
        solve()

if __name__ == "__main__":
    main()   

from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(max(c.values()))

from collections import Counter

n = int(input()) 
a = [int(i) for i in input().split()] 

counter = Counter(a)

result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result) 