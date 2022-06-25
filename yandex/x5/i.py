
def func(a: list) -> None:
    '''
    печать элементов списка
    '''
    # print all elements of the list one by one separated by a comma and space ends with dot
    print(', '.join(map(str, a)) + '.')
   
    

print(func([2, 3, 1, 4, 6]))