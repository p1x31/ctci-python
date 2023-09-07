#Union-find is a data structure that supports two operations: find and union. 
#Find returns the root of a given element, and union merges two sets that contain the given elements. 
#To implement union-find in Python, you need to maintain two arrays: parent and rank. 
#Parent stores the parent of each element, and rank stores the rank (or height) of each set. 
#Initially, each element is its own parent and has rank zero. Here is an example of how to implement union-find in
# Initialize the parent and rank arrays
n = 10 # The number of elements
parent = list(range(n))
rank = [0] * n

# Define a function to find the root of an element
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Define a function to merge two sets
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