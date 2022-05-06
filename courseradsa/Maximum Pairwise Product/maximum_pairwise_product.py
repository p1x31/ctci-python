# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_index1 = numbers.index(max(numbers))
    first_max_number = numbers[max_index1]
    # we need pop because -> index returns the first item whose value is "bar". 
    # If "bar" exists twice at list, you'll never find the key for the second "bar". 
    # See documentation: docs.python.org/3/tutorial/datastructures.html
    numbers.pop(max_index1)
    max_index2 = numbers.index(max(numbers))
    second_max_number = numbers[max_index2]
    return first_max_number * second_max_number


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
