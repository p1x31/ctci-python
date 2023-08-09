# Read the input from the file
with open("input.txt", "r") as file:
    data = file.readline().split()

# Extract the number of buildings and building heights
num_buildings = int(data[0])
heights = list(map(int, data[1:]))

# Initialize variables for minimum and maximum heights
min_height = float("inf")
max_height = float("-inf")

# Iterate through building heights to find the minimum and maximum heights
for height in heights:
    if height < min_height:
        min_height = height
    if height > max_height:
        max_height = height

# Calculate the maximum possible height of the zipline
max_zipline_height = max_height - min_height

# Write the result to the output file
with open("output.txt", "w") as file:
    file.write(str(max_zipline_height))