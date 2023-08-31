import numpy as np
from scipy.ndimage import label

# Считываем матрицу сегментации
matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

n, m = len(matrix), len(matrix[0])

# Находим количество уникальных объектов
num_objects, object_labels = label(matrix)

# Выводим количество уникальных объектов
print(m)
#remove [] from matrix num_objects
for row in num_objects:
    print(''.join(map(str, row)))


# Выводим матрицу с разметкой общих сегментированных областей на отдельные объекты
# for i in range(n):
#     for j in range(m):
#         print(str(object_labels[i][j]))