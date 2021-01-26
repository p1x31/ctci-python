t = int(input())
for ith in range(t):
    n, m, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_cnt = {}
    b_cnt = {}
    for items in a:
        a_cnt[items] = a_cnt.get(items, 0) + 1 
    for items in b:
        b_cnt[items] = b_cnt.get(items, 0) + 1 
    answer = k * (k - 1)
    for i in range(k):
        answer -= int(a_cnt.get(a[i])) + int(b_cnt.get(b[i])) - 2
    print(int(answer/2))