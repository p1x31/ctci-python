
#n = int(input())

X, Y = {}, {}

with open('request2.in', 'r') as file:
    n = int(file.readline())
    for i, line in enumerate(file):
        X[i], Y[i] = map(int, line.split())

file.close()

# for i in range(n):
#     X[i] = int(input())
#     Y[i] = int(input())

limit = sum(Y.values())

T, Min, C = 0,0, # C - max number of reports possible
while Min < limit:
    Min = limit
    for i in range(n):
        if X[i] >= T and Y[i] < Min: Min = Y[i]
    if Min < limit:
        T = Min
        C += 1
print(C)
