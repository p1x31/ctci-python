MOD = 1000000007

def inv(a):
    r = 1
    t = a
    k = MOD - 2
    while k:
        if k & 1:
            r = (r * t) % MOD
        t = (t * t) % MOD
        k >>= 1
    return r

n, k = map(int, input().split())
p = inv(k) % MOD
a = 1
b = 0

for i in range(n):
    a = (a * inv(p)) % MOD
    b = (b * inv(p)) % MOD
    a = (a + (p - 1) * inv(p)) % MOD
    # this should be
    b = (b + inv(p) - 1) % MOD

result = (MOD - b) * inv(a) % MOD
print(result)