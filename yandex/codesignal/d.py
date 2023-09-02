def max_arithmetic_progression(a, b):
    max_len = 2
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            diff = a[j] - a[i]
            count = 2
            last = a[j]
            for k in range(len(b)):
                if b[k] - last == diff:
                    count += 1
                    last = b[k]
            max_len = max(max_len, count)
    return -1 if max_len == 2 else max_len

a = [0, 4, 8, 16]
b = [0, 2, 6, 12, 14, 20]
print(max_arithmetic_progression(a, b))