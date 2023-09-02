# Читаем количество массивов
n = int(input())
# Создаем список для массивов
arrays = []
# Для каждого массива
for _ in range(n):
    # Читаем размер массива
    k = int(input())
    # Читаем элементы массива и добавляем их в список
    array = list(map(int, input().split()))
    arrays.append(array)

# Импортируем функцию permutations из модуля itertools
from itertools import combinations

def similarity(L):
    res = 0
    for v in zip(*L):
        if len(set(v)) == 1: 
            res += 1
        else: 
            return res
    return res

# Создаем переменную для суммы близостей всех пар массивов и инициализируем ее нулем
total = 0
# Для каждой перестановки массивов
for pair in combinations(arrays, 2):
    # Вызываем функцию для нахождения близости этих двух частей и прибавляем ее к переменной суммы
    total += similarity(pair)
# Выводим переменную суммы как ответ
print(total)