class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.count[x_root] += self.count[y_root]
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

n, m = map(int, input().split())
dsu = DSU(n)
count = [1] * n
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1]-1, query[2]-1
        if dsu.find(x) != dsu.find(y):
            count[dsu.find(x)] += 1
            count[dsu.find(y)] += 1
        dsu.union(x, y)
    elif query[0] == 2:
        x, y = query[1]-1, query[2]-1
        print('YES' if dsu.find(x) == dsu.find(y) else 'NO')
    else:
        x = query[1]-1
        print(count[dsu.find(x)])