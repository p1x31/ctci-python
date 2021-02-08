def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n


import numpy as np
np.set_printoptions(suppress=True)
n = int(input())
def fib(n):
    phi_1 = (np.sqrt(5) + 1) / 2
    phi_2 = (np.sqrt(5) - 1) / 2
    f = (phi_1**n - phi_2**n) / np.sqrt(5)
    return int(f)

print(fib(n))