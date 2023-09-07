# Read the input data
n, m = map(int, input().split()) # The required sum and the number of denominations
a = list(map(int, input().split())) # The existing denominations
a.sort() # Sort the denominations in ascending order

# Initialize some variables
ans = [] # The list of stolen bills
i = m - 1 # The index of the current denomination
s = 0 # The current sum

# Loop through the denominations from the largest to the smallest
while i >= 0 and s < n:
    # If the current denomination is smaller than or equal to the remaining amount
    if a[i] <= n - s:
        # Add two bills of this denomination to the answer
        ans.append(a[i])
        ans.append(a[i])
        # Update the current sum
        s += 2 * a[i]
    # Move to the next smaller denomination
    i -= 1

# Check if the required sum is reached
if s == n:
    # Print the number of stolen bills and their denominations
    print(len(ans))
    print(*ans)
else:
    # Print -1 to indicate that the plan is impossible
    print(-1)