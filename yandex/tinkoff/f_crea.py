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
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return
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

# Process the questions
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # Merge two bands
        union(query[1], query[2])
    elif query[0] == 2:
        # Check if two ghosts are in the same band
        if find(query[1]) == find(query[2]):
            print("YES")
        else:
            print("NO")
    else:
        # Print the number of bands a ghost has been in
        print(count[query[1]])