t = int(input())
# n boys
# m girls
# k number of couples ready to dance together
for _ in range(t):
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
# count repeated boys put in dict
# count repeated girls put in dict
# answer k * k-1 nCk e.g. 6 ways to chose 2 elements from {1,2,3,4}
# complementary counting bad pairs
# get value at key a[i] -> how many bad boys -1 except yourself
# get value at key a[i] -> how many bad girls -1 except yourself
# answer / 2 because counted twice
# (n k) = n!/k!(n-k)! chose 2 from 4 k=2 n=4
# dict.get(key, default = None) if doesnt exist 0