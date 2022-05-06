# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            i = i + 1
            break
    
    # Getting the period
    pisano_period = i

    # Taking mod of N with
    # period length
    n = n % pisano_period

    previous, current = 0, 1

    if n <= 1:
        return n

    for i in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
