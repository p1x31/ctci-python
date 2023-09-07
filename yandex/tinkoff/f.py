# Функция для нахождения представителя множества
def find(x):
    # Если представитель множества равен самому элементу, то возвращаем его
    if parent[x] == x:
        return x
    # Иначе находим представителя рекурсивно и обновляем значение для текущего элемента
    parent[x] = find(parent[x])
    return parent[x]

# Функция для объединения двух множеств
def union(x, y):
    # Находим представителей множеств
    x_root = find(x)
    y_root = find(y)
    # Если представители равны, то множества уже объединены
    if x_root == y_root:
        return
    # Иначе объединяем меньшее множество с большим
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
        size[y_root] += size[x_root]
        visited[y_root] |= visited[x_root]
    else:
        parent[y_root] = x_root
        size[x_root] += size[y_root]
        visited[x_root] |= visited[y_root]
        # Если ранги равны, то увеличиваем ранг большего множества на 1
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

# Считываем входные данные
n, m = map(int, input().split())
# Создаем массивы для хранения представителей, рангов и размеров множеств
parent = list(range(n + 1))
rank = [0] * (n + 1)
size = [1] * (n + 1)
# Создаем массив для хранения информации о посещенных бандах для каждого духа
visited = [set([i]) for i in range(n + 1)]
# Проходим по всем вопросам крика
for _ in range(m):
    # Считываем тип вопроса и параметры
    query = list(map(int, input().split()))
    # Если тип вопроса равен 1, то объединяем банды с духами x и y
    if query[0] == 1:
        union(query[1], query[2])
    # Если тип вопроса равен 2, то проверяем, находятся ли духи x и y в одной банде
    elif query[0] == 2:
        if find(query[1]) == find(query[2]):
            print('YES')
        else:
            print('NO')
    # Если тип вопроса равен 3, то выводим количество банд, в которых побывал дух x
    else:
        print(len(visited[find(query[1])]))