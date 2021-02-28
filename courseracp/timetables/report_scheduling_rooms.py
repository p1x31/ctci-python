X, Y = {}, {}
# n = int(input())
# for i in range(n):
#     X[i] = int(input())
#     Y[i] = int(input())


with open('request2.in', 'r') as file:
    n = int(file.readline())
    for i, line in enumerate(file):
        X[i], Y[i] = map(int, line.split())

file.close()

I = dict(zip(X.values(), Y.values())) # time intervals
I_sorted = dict(sorted(I.items()))


limit = sum(Y.values())
# T - begin of the report time
# cnt - max number of rooms
T, Min, C, cnt = 0, 0, 0, 0 # C - max number of reports 
while I_sorted:
    T, Min = 0 , 0
    while Min < limit:
        Min = limit
        # find earliest time possible
        for key, value in I_sorted.items():
            if key >= T and value < Min:
                Min = value
                key_to_delete = key
        if Min < limit:
            T = Min # update begin time
            I_sorted.pop(key_to_delete)
            #print(I_sorted)
            C += 1
    cnt += 1
#print(C)
print(cnt)

