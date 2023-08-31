# Read the input data
m = []
with open('input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        m.append(row)

# Initialize the variables
n = len(m)
label = 1
labels = {}

# Define a function to check if a cell is a cat and assign a label to it
def check_cell(i, j):
    global label
    if m[i][j] == 1:
        # Check if any of the neighboring cells have already been labeled
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1)]
        for x, y in neighbors:
            if x >= 0 and y >= 0 and y < n:
                if m[x][y] > 1:
                    m[i][j] = m[x][y]
                    return
        # If none of the neighboring cells have been labeled, assign a new label
        m[i][j] = label
        labels[label] = 1
        label += 1

# Iterate over the cells and assign labels to the cats
for i in range(n):
    for j in range(n):
        check_cell(i, j)

# Print the result
print(len(labels))
for row in m:
    print(' '.join(map(str, row)))