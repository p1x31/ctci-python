from sys import stdin,stdout
L = lambda: list(map(int, stdin.readline().strip().split()))
M = lambda: map(int, stdin.readline().strip().split())
I = lambda: int(stdin.readline().strip())
S = lambda: stdin.readline().strip()
C = lambda: stdin.readline().strip().split()
# Читаем количество массивов
n = I()
# Создаем список для массивов
arrays = []
# Для каждого массива
for _ in range(n):
    # Читаем размер массива
    k = I()
    # Читаем элементы массива и добавляем их в список
    array = L()
    arrays.append(array)

# Создаем функцию для нахождения близости двух массивов
def similarity(L):
    res = 0
    for v in zip(*L):
        if len(set(v)) == 1: 
            res += 1
        else: 
            return res
    return res
    

# Создаем переменную для суммы близостей всех пар массивов
total = 0
# Для каждой пары массивов
for i in range(n):
    for j in range(i + 1, n):
        # Вызываем функцию для нахождения близости и прибавляем ее к переменной суммы
        total += similarity([arrays[i], arrays[j]])
# Выводим переменную суммы как ответ
print(total)