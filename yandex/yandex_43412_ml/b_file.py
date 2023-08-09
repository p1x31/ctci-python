# Read the input from the file
with open("input.txt", "r") as file:
    data = file.readline().split()

# Extract the number of buildings and building heights
num_buildings = int(data[0])
heights = list(map(int, data[1:]))

# Initialize variables for minimum and maximum heights
l , r = 0, len(heights) - 1
leftMax, rightMax = heights[l], heights[r]
res = 0
while l < r:
    if leftMax < rightMax:
        l += 1
        leftMax = max(leftMax, heights[l])
        res = max(res, (leftMax - heights[l]))
        
    else:
        r -= 1
        rightMax = max(rightMax, heights[r])
        res = max(res, (rightMax - heights[r]))
        
# Write the result to the output file
with open("output.txt", "w") as file:
    file.write(str(res))