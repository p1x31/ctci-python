def earn_money(n, m, nominals):
    nominals.sort()  # Sort the nominals in ascending order
    result = []  # Initialize a list to store the stolen nominals

    # Helper function to check if a sum of nominals equals n
    def find_combination(target_sum, current_combination):
        if target_sum == 0:
            return current_combination
        if target_sum < 0 or len(current_combination) >= 3:
            return None

        for i, nominal in enumerate(nominals):
            remaining_combination = find_combination(target_sum - nominal, current_combination + [nominal])
            if remaining_combination:
                return remaining_combination

        return None

    # Try to find a combination of nominals that equals n
    combination = find_combination(n, [])

    if combination:
        for nominal in combination:
            result.extend([nominal, nominal])  # Add each nominal twice
        return result
    else:
        return [-1]  # No valid combination found


# Read input
n, m = map(int, input().split())
nominals = list(map(int, input().split()))

# Calculate the result
result = earn_money(n, m, nominals)

# Print the result
print(*result)