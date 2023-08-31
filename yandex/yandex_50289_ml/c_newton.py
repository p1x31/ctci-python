import numpy as np
from scipy.optimize import newton

n = int(input())
A = np.zeros((n, n))
B = np.zeros((n, n))

for i in range(n):
    A[i] = list(map(float, input().split()))

for i in range(n):
    B[i] = list(map(float, input().split()))

def equation(z):
    return np.linalg.det(B + A * z + 1j * z**2)

root =  newton(equation, 0)
print(abs(np.round(root, 4)))