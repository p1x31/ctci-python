X, Y = {}, {} # X - weight Y - cost
with open('cont2.in', 'r') as file:
    n, W = map(int, file.readline().split(" "))
    for i, line in enumerate(file):
        X[i], Y[i] = map(int, line.split())

file.close()
# C = Cost / Weight
C = {}
total = 0 # total possible weight
for i in range(len(X)):
    # index | cost-weight ratio
    C[i] = Y[i] / X[i]
# sort by cost-weight ratio preserve the indecies  
# param (, reverse=True) to sort high low
print(C)
C = dict(sorted(C.items(), key=lambda item: item[1], reverse=True))
print(C)
for key, sorted_ratio in C.items():
    # used index for weight
    if W - X[key] >= 0:
        W -= X[key]
        # use index for cost
        total += Y[key]
    #elif W < X[key]:
    else:
        rest = Y[key] * (W / X[key])
        total += rest
        break
print(total)