import numpy as np
n = int(input())
a = [] 
s = input()
while s != '':  
    i = s.split()       
    a.extend(map(lambda s: str(s),i))
    s = input()
print(len(np.unique(a)))