def func(a: list) -> int:
    '''
    функция возвращает второй 
    по величине элемент списка
    '''
    return sorted(a)[-2]

print(func([2, 3, 1, 4, 6]))