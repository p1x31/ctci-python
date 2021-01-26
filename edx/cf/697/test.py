import math
with open('my_file.txt', 'w') as f:
    f.write("10000\n")
    a = 4311260933333
    for i in range(10000):
        f.write(str(a)+"\n")
        a -= 1  # 
        

a = [2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,
 2203,2281,3217,4253,4423,9689,9941,11213,19937,
 21701,23209,44497,86243,110503,132049,216091,
 756839,859433,1257787,1398269,2976221,3021377,
 6972593,13466917,20996011,24036583,25964951,
 30402457,32582657,37156667,42643801,43112609]

with open('test.txt', 'w') as f:
    f.write("10000\n")
    for i in range(len(a)):
        f.write(str(a[i])+"\n") # 
    a = 100000000000000
    for j in range(10000-47):
        f.write(str(a)+"\n")
        a -= 1279  # 

with open('test1000.txt', 'w') as f:
    f.write("10000\n")
    a = int(math.pow(2,46))
    b = int(math.pow(2,44))
    for i in range(5000):
        f.write(str(a)+"\n")
        f.write(str(b)+"\n")

with open('test1001.txt', 'w') as f:
    f.write("10000\n")
    a = 100000000000000
    for j in range(10000):
        f.write(str(a)+"\n")
        a -= 1279  # 