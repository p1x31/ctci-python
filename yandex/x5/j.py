def func(a: int) -> int:
    '''
    находи разность между суммой цифр четных разрядов (раздяд единиц всегда нулевой) и суммой цифр нечетных разрядов натурального числа. 
    разность сама должна делиться на 11.
    '''
    # Check the difference between sum an even indexes and sum of integers at odd indexes 
    return (sum(int(value) for key, value in enumerate(str(a)) if key % 2 == 0) - sum(int(value) for key, value in enumerate(str(a)) if key % 2 != 0))

print(func(86416))
