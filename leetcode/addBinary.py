#Given two binary strings a and b, return their sum as a binary string.
a = input()
b = input()
a = int(a,2)
b = int(b,2)
x = bin(a+b)
x = x.replace('0b', '')
print(x)