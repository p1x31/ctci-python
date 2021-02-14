import math
# T = tank size
# C = total distance
with open('petrol2.in', 'r') as file:
    n, C, T = map(int, file.readline().split(' '))
    X = [int(x) for x in file.readline().split(' ')]
    X.append(C+1)
R, Max, cnt = 0,0,0
n_stops = math.ceil(C/T)
d = T
for i in range(1, len(X)):
    if Max + T > C:
        break
    if X[i] > d and X[i-1] <= d:
        Max = X[i-1]
        cnt += 1
        d = Max + T
print(cnt)

