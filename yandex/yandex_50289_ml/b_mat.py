# Read the input data
m = []
with open('input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        m.append(row)

# Initialize the variables
n = len(m)
label = 1
count = 0

# Iterate over the cells and assign labels to the non-zero values
for i in range(n):
    for j in range(len(m[i])):
        if m[i][j] != 0:
            count += 1
            m[i][j] = label
            label += 1

# Print the result
print(count)
for row in m:
    print(''.join(map(str, row)))