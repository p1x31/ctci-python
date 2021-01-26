N, X = map(int, input().split())
s = 0
for i in range(N):
    V, P = map(int, input().split())
    s += V*P
    if s > X*100:
        print(i+1)
        exit()
print(-1)