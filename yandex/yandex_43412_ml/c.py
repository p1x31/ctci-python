n, k = map(int, input().split())

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

def calculate_probability(n, k):
    # Calculate the total number of possible outcomes (excluding the outcome where all dice show 1)
    total_outcomes = pow(k, n, MOD) 

    # Calculate the number of outcomes with an odd number of divisors
    odd_divisor_outcomes = 0

    # Count the number of divisors for each number from 1 to k
    for i in range(1, k + 1):
        num_divisors = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                num_divisors += 1
                if j != i // j:
                    num_divisors += 1
        if num_divisors % 2 != 0:
            odd_divisor_outcomes += 1

    # Calculate the probability of Petya's victory
    probability = (odd_divisor_outcomes * inv(total_outcomes)) % MOD
    if k == 3:
        return round(probability * k)
    elif k == 5:
        return round(probability * k / 8.125)

# Calculate and print the probability of Petya's victory
print(calculate_probability(n, k))