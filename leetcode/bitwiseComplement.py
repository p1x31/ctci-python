#Complement of Base 10 Integer
def bitwiseComplement(N: int) -> int:
    x = bin(N)
    x = x.replace('0', 'x')
    x = x.replace('1', '0')
    x = x.replace('x', '1')
    x = x.replace('1b', '0b')
    return int(x,2)
    
print(bitwiseComplement(5))