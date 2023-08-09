from sys import stdin
Ma = lambda: map(int, stdin.readline().strip().split())
L = lambda: list(map(int, stdin.readline().strip().split()))


def main():
    # Чтение входных данных
    N, M, k = Ma()

    # Заполнение матрицы
    result = fill_matrix(N, M, k)

    # Вывод матрицы
    for row in result:
        print(' '.join(map(str, row)))

def fill_matrix(N, M, k):
    matrix = [[k] * M for _ in range(N)]
    return matrix


if __name__ == "__main__":
    main()