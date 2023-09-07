def steal_money(n, m, nominals):
    # Sort the nominals in ascending order
    nominals.sort()
    
    # Initialize variables to keep track of the stolen nominals
    stolen_nominals = []
    remaining_money = n
    
    # Create a list to count how many times each nominal is used
    usage_count = [0] * m
    
    # Iterate through the nominals
    for i in range(m):
        # Check if we have already stolen enough money
        if remaining_money == 0:
            break
        
        # Calculate how many times we can use the current nominal
        max_usage = min(2, remaining_money // nominals[i])
        
        # Use the current nominal the maximum possible times
        for _ in range(max_usage):
            stolen_nominals.append(nominals[i])
            remaining_money -= nominals[i]
            usage_count[i] += 1
    
    # If we have stolen exactly n dollars, return the result; otherwise, return -1
    if remaining_money == 0:
        return usage_count, stolen_nominals
    else:
        return -1

# Read input
n, m = map(int, input().split())
nominals = list(map(int, input().split()))

# Calculate the result
result = steal_money(n, m, nominals)

# Print the result
if result == -1:
    print(-1)
else:
    usage_count, stolen_nominals = result
    print(len(stolen_nominals))
    print(*stolen_nominals)