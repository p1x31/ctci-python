#right
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l, r = 0, n - 1
while l < n and a[l] == b[l]:
    l += 1
while r >= 0 and a[r] == b[r]:
    r -= 1

if l > r:
    print("YES")
else:
    if sorted(a[l:r+1]) == b[l:r+1]:
        print("YES")
    else:
        print("NO")