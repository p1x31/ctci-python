import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
t = int(input())

def solve(n, points):
    d_plus, d_minus, red, stupac = {}, {}, {}, {}
    r=0
    
    for i in points:
        x, y = i
        a, b, c, d = red.get(x, 0), stupac.get(y, 0), d_plus.get(x+y, 0), d_minus.get(x-y, 0) 
        r+=(a+b+c+d)*2; red[x], stupac[y], d_plus[x+y], d_minus[x-y] = a+1, b+1, c+1, d+1;

    return r

for i in range(t):
    n = int(input())
    points = [list(map(int, (input().decode()).split())) for i in range(n)]
    print(solve(n, points))
