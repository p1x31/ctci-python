from sys import stdin
Ma = lambda: map(int, stdin.readline().strip().split())
L = lambda: list(map(int, stdin.readline().strip().split()))

def create_new_matrix(N1, M1, N2, M2, matrix):
    new_matrix = [[0] * M2 for _ in range(N2)]

    if N1 * M1 != N2 * M2:
        print("Невозможно преобразовать матрицу")
        return
    
    new_matrix = []
    rowi = []
    for i in range(N1):
        for j in range(M1):
            rowi.append(matrix[i][j])
            if len(rowi) == M2:
                new_matrix.append(rowi)
                rowi = []
    return new_matrix



def main():
    # Чтение входных данных
    N1, M1, N2, M2 = Ma()

    matrix = []
    for _ in range(N1):
        row = L()
        matrix.append(row)

    # Создание новой матрицы
    result = create_new_matrix(N1, M1, N2, M2, matrix)

    # Вывод новой матрицы
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()