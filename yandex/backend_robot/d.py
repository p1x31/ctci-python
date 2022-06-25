X, Y = {}, {}

with open('input.txt', 'r') as file:
    N, M, t = map(int, file.readline().split(' '))
    for i, line in enumerate(file):
        X[i], Y[i] = map(int, line.split())

file.close()