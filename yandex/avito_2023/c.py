from sys import stdin
M = lambda: map(int, stdin.readline().strip().split())
L = lambda: list(map(int, stdin.readline().strip().split()))


def replace_values(min_val, max_val, values):
    return [min(max(value, min_val), max_val) for value in values]


def main():

    # Read input
    min_val, max_val = M()
    values = L()

    # Replace values
    result = replace_values(min_val, max_val, values)

    # Print the result
    print(' '.join(map(str, result)))



if __name__ == "__main__":
    main()