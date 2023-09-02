# Читаем количество карт и изменений
N, M, Q = map(int, input().split())
# Создаем множества для карт игроков A и B
A = set(map(int, input().split()))
B = set(map(int, input().split()))
# Инициализируем разнообразие как разность мощностей множеств
result = []
diversity = len(A) + len(B) - 2 * len(A & B)
# Для каждого изменения
for _ in range(Q):
    # Читаем тип, игрока и карту
    type, player, card = input().split()
    type = int(type)
    card = int(card)
    # Если добавляется карта
    if type == 1:
        # Если карта есть в множестве другого игрока
        if (player == 'A' and card in B) or (player == 'B' and card in A):
            # Уменьшаем разнообразие на 1
            diversity -= 1
            result.append(diversity)
            # # Удаляем карту из обоих множеств
            if player == 'A':
                B.discard(card)
            else:
                A.discard(card)
        # Иначе
        else:
            # Увеличиваем разнообразие на 1
            diversity += 1
            result.append(diversity)
            # Добавляем карту в множество соответствующего игрока
            if player == 'A':
                A.add(card)
            else:
                B.add(card)
    # Если удаляется карта
    else:
        # Если карта есть в множестве другого игрока
        if (player == 'A' and card in B) or (player == 'B' and card in A):
            # Увеличиваем разнообразие на 1
            diversity += 1
            result.append(diversity)
            # Добавляем карту в множество соответствующего игрока
            if player == 'A':
                A.discard(card)
            else:
                B.discard(card)
        # Иначе
        else:
            if (card not in B) and (card not in A):
                #diversity += 1
                result.append(diversity)
            else:
                # Уменьшаем разнообразие на 1
                diversity -= 1
                result.append(diversity)
                # Удаляем карту из множества соответствующего игрока
                if player == 'A':
                    A.discard(card)
                else:
                    B.discard(card)
    # Выводим разнообразие после изменения
print(*result)