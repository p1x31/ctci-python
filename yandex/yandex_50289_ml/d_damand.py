def calculate_demand_supply(m, s, n, data, q, queries):
    # Initialize the demand and supply arrays
    demand = [0] * m
    supply = [s] * m

    # Process the historical data
    for i in range(n):
        week, day, hour, *requests = data[i]
        for j in range(m):
            demand[j] += requests[j]
            supply[j] -= requests[j]

    # Process the queries
    results = []
    for i in range(q):
        query_type, week, day, hour, *requests = queries[i]
        if query_type == 1:
            # Update the demand and supply based on the new data
            for j in range(m):
                demand[j] += requests[j]
                supply[j] -= requests[j]
        elif query_type == 2:
            # Calculate the average number of requests that need to be "cut"
            cut = sum(max(0, demand[j] - supply[j]) for j in range(m)) / m
            results.append(cut)

    return results

# Read the input
m, s = map(int, input().split())
n = int(input())
data = []
for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)
q = int(input())
queries = []
for _ in range(q):
    row = list(map(int, input().split()))
    queries.append(row)

# Calculate the demand-supply balance
results = calculate_demand_supply(m, s, n, data, q, queries)

# Print the results
print(' '.join(f'{result:.11f}' for result in results))