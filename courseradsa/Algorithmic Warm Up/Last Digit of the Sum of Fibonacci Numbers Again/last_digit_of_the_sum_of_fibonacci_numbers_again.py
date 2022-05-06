# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    def fib(n):# The first two Fibonacci numbers
        f0 = 0
        f1 = 1
        if n == 0:
            return 0

        # Pisano Period for % 10 is 60
        remainder = n % 60

        # Checking the remainder
        if remainder == 0:
            return 0

        # The loop will range from 2 to
        # two terms after the remainder
        for i in range(2, remainder + 3):
            f = (f0 + f1) % 60
            f0, f1 = f1, f
        summ = f1 - 1
        return summ

    return (fib(to_index) - fib(from_index - 1)) % 10




if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
