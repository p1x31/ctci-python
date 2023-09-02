#Читаем количество сотрудников
N = int(input())
# Читаем языки сотрудников и добавляем None для директора
languages = ["AB"] + input().split()
# Читаем иерархию организации
hierarchy = list(map(int, input().split()))
# Создаем словарь для подчиненных каждого сотрудника
subordinates = {}
# Для каждого сотрудника
for i in range(N + 1):
    # Инициализируем пустой список подчиненных
    subordinates[i] = []
# Для каждого элемента иерархии кроме первого и последнего
for i in range(1, 2 * (N + 1) - 1):
    # Если элемент не равен предыдущему
    if hierarchy[i] != hierarchy[i - 1]:
        # Добавляем элемент в список подчиненных предыдущего элемента
        subordinates[hierarchy[i - 1]].append(hierarchy[i])

# Создаем функцию для нахождения языкового барьера
def find_barrier(employee, boss):
    # Если у сотрудника есть начальник
    if boss not in "Node":
        # Если языки совпадают
        if languages[employee] == languages[boss]:
            # Возвращаем ноль
            return 0
        # Иначе
        else:
            # Возвращаем единицу плюс языковой барьер начальника
            return 1 + find_barrier(boss, hierarchy[hierarchy.index(boss) - 1])
    # Иначе (сотрудник - директор)
    else:
        # Возвращаем ноль
        return 0

# Создаем список для языковых барьеров каждого сотрудника
barriers = []
# Для каждого сотрудника кроме директора
for i in range(1, N + 1):
    # Находим его начальника по индексу в иерархии
    boss = hierarchy[hierarchy.index(i) - 1]
    # Вызываем функцию для нахождения языкового барьера
    barrier = find_barrier(i, boss)
    # Добавляем языковой барьер в список
    barriers.append(barrier)
# Выводим список языковых барьеров как ответ
print(*barriers)