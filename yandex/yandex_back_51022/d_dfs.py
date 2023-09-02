def calculate_language_barrier(N, languages, hierarchy):
    # Initialize lists to store language barrier for each employee
    language_barrier = [0] * N
    visited = [False] * N
    
    # Create an adjacency list to represent the organization hierarchy
    adjacency_list = [[] for _ in range(N)]
    
    # Fill the adjacency list based on the hierarchy
    for i in range(1, 2 * (N + 1), 2):
        boss = hierarchy[i]
        subordinate = i // 2
        adjacency_list[boss - 1].append(subordinate - 1)
    
    # Depth-First Search (DFS) to calculate language barrier
    def dfs(node, current_language):
        visited[node] = True
        for child in adjacency_list[node]:
            language_barrier[child] = language_barrier[node] + (languages[node] != languages[child])
            dfs(child, languages[child])
    
    # Start DFS from the director (employee 0)
    dfs(0, languages[0])

    language_barrier[0] = 0
    
    return language_barrier

# Read input
N = int(input())
languages = input().split()
hierarchy = list(map(int, input().split()))

# Calculate language barriers
language_barrier = calculate_language_barrier(N, languages, hierarchy)

# Print the language barriers
print(*language_barrier)