# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    def pisano_num_mod10(n):
        previous, current = 0, 1
        #num mod 10 gives 60 repeatations in Pisano Series.
        n = n % 60
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            #Iterate until n+2, since we are looking for F_N + F_{N+1}
            for _ in range(2, n + 1): 
                previous, current = current, (previous + current) % 60 
            return current
    return pisano_num_mod10(n) * pisano_num_mod10(n+1) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
