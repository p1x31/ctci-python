# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n
    #print("Compute F sub", n)
    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n, _cache={}):
    assert 0 <= n <= 10000000

    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci_number(n - 1) + fibonacci_number(n - 2))
    return n


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
