def perform_segmentation(matrix):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a dictionary to store the mapping of segmented objects
    objects = {}

    # Perform segmentation
    object_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # Check the neighbors to determine if there's an existing object
                top = objects.get((i-1, j))
                left = objects.get((i, j-1))

                if top is None and left is None:
                    # Create a new object
                    object_count += 1
                    objects[(i, j)] = object_count
                elif top is not None and left is not None:
                    # Merge two existing objects
                    objects[(i, j)] = top
                    if top != left:
                        # Update the object mapping for objects connected horizontally
                        for key, value in objects.items():
                            if value == left:
                                objects[key] = top
                elif top is not None:
                    # Assign the existing object from the top neighbor
                    objects[(i, j)] = top
                else:
                    # Assign the existing object from the left neighbor
                    objects[(i, j)] = left

    # Create the segmented matrix
    segmented_matrix = [[objects.get((i, j), 0) for j in range(cols)] for i in range(rows)]

    return object_count, segmented_matrix


# Read the input matrix
matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

# Perform segmentation
object_count, segmented_matrix = perform_segmentation(matrix)

# Print the number of unique objects
print(object_count)

# Print the segmented matrix
print(segmented_matrix)
# for row in segmented_matrix:
#     print(''.join(map(str, row)))