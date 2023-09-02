def sort_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        j = 0
        k = i
        diagonal = []
        while k >= 0:
            diagonal.append(matrix[j][k])
            j += 1
            k -= 1
        diagonal.sort(reverse=True)
        j = 0
        k = i
        while k >= 0:
            matrix[j][k] = diagonal.pop(0)
            j += 1
            k -= 1

    for i in range(1, n):
        j = n - 1
        k = i
        diagonal = []
        while k < n:
            diagonal.append(matrix[k][j])
            j -= 1
            k += 1
        diagonal.sort(reverse=True)
        j = n - 1
        k = i
        while k < n:
            matrix[k][j] = diagonal.pop(0)
            j -= 1
            k += 1

    return matrix