def multiples():
    multiples = []
    for i in range (1000):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples.append(i)
    res = sum(multiples)
    print(res)
    return res

print(multiples())