def func(a: list) -> int:
    '''
    сумма всех четных чисел
    '''
    return sum(a[i] for i in range(len(a)) if a[i] % 2 == 0)