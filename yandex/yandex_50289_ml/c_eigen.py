import numpy as np
from scipy.linalg import eigh

n = int(input())
A = np.zeros((n, n))
B = np.zeros((n, n))

for i in range(n):
    A[i] = list(map(float, input().split()))

for i in range(n):
    B[i] = list(map(float, input().split()))

M = np.kron(np.eye(n), A) + np.kron(B, np.eye(n))
eigenvalues, _ = eigh(M)

positive_roots = [eigval for eigval in eigenvalues if eigval > 0]
smallest_positive_root = np.min(positive_roots)
smallest_real_root = np.sqrt(smallest_positive_root)

print(np.round(smallest_real_root, 4))