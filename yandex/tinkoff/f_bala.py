#right
# Read the number of ghosts and questions
n, m = map(int, input().split())

# Initialize the parent and rank arrays for union-find
parent = list(range(n + 1))
rank = [0] * (n + 1)

# Initialize the count array for the number of bands each ghost has been in
count = [1] * (n + 1)

# Define a function to find the root of a ghost
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Define a function to merge two bands
def union(x, y):
    # Find the roots of x and y
    x_root = find(x)
    y_root = find(y)
    
    # If they are already in the same band, do nothing
    if x_root == y_root:
        return
    
    # Otherwise, merge them by rank
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
    
    # Increment the count for each ghost in the merged band
    for i in range(1, n + 1):
        if find(i) == x_root or find(i) == y_root:
            count[i] += 1

# Loop through the questions
for _ in range(m):
    # Read the question type and parameters
    q = list(map(int, input().split()))
    
    # If the question is of type 1, merge the bands of x and y
    if q[0] == 1:
        union(q[1], q[2])
    
    # If the question is of type 2, check if x and y are in the same band
    elif q[0] == 2:
        if find(q[1]) == find(q[2]):
            print("YES")
        else:
            print("NO")
    
    # If the question is of type 3, print the number of bands x has been in
    else:
        print(count[q[1]])