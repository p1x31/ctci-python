n, k = map(int, input().split())

MOD = 1000000007

def calculate_probability(n, k):
    # Initialize the probability table
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base cases
    dp[0][0] = 1

    # Fill the probability table
    for i in range(1, k + 1):
        for j in range(n + 1):
            for d in range(1, min(j, k) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - d]) % MOD

    # Calculate the total probability
    total_probability = sum(dp[k]) % MOD

    # Calculate p * q^(-1) mod 1000000007
    result = (total_probability * pow(k, MOD - 2, MOD)) % MOD

    return result

# Calculate and print the probability of winning
print(calculate_probability(n, k))