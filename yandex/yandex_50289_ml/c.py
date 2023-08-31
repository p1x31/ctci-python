import numpy as np

# Считываем матрицы A и B
n = int(input())
A = np.zeros((n, n))
B = np.zeros((n, n))
for i in range(n):
    A[i] = list(map(float, input().split()))
for i in range(n):
    B[i] = list(map(float, input().split()))

# Находим наименьший вещественный корень уравнения
z = np.linalg.eigvals(B + A * 1j) / 1j
z_real = np.real_if_close(z[z.real < 0]).max()

# Выводим ответ
print(np.round(z_real, 4))