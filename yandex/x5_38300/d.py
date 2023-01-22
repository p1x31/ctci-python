def func(a: list) -> int:
    '''
    функция возвращает второй 
    по величине элемент списка
    '''
    return a == a[::-1]

print(func('ab'))