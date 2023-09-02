
def solve(N, A):
    # Сортируем гвоздики по возрастанию координат
    A.sort()
    # Создаем массив dp длины N
    dp = [0] * (N+1)
    if N > 2:
        # Инициализируем dp[0] = 0
        dp[0] = A[1] - A[0]
        # Инициализируем dp[N-1] = 0
        dp[N-1] = A[N-1] - A[N-2]

        for i in range(2, N-2):
            dp[i] = min(A[i] - A[i-1], A[i+1] - A[i]) 
        return sum(dp)
    else:
        dp[0] = A[1] - A[0]
        return dp[0]

# Читаем входные данные
N = int(input())
A = list(map(int, input().split()))
# Выводим ответ
print(solve(N, A))

#3 13 12 4 14 6
#3 4 6 12 13 14
#0 1 2 3  4  5

