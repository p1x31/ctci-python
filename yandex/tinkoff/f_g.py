def find_root(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find_root(parents, parents[x])
    return parents[x]

def unite(parents, sizes, x, y):
    root_x = find_root(parents, x)
    root_y = find_root(parents, y)
    
    if root_x != root_y:
        if sizes[root_x] < sizes[root_y]:
            root_x, root_y = root_y, root_x
        parents[root_y] = root_x
        sizes[root_x] += sizes[root_y]

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
sizes = [1] * (n + 1)

answers = []

for _ in range(m):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        unite(parents, sizes, query[1], query[2])
    elif query[0] == 2:
        if find_root(parents, query[1]) == find_root(parents, query[2]):
            answers.append("YES")
        else:
            answers.append("NO")
    else:
        answers.append(str(sizes[find_root(parents, query[1])]))

for answer in answers:
    print(answer)