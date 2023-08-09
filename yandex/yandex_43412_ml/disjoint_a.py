class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def is_quest_possible(n, quests):
    ds = DisjointSet(n)

    for i in range(n):
        if quests[i] != -1:
            ds.union(i, quests[i] - 1)

    for i in range(n):
        if quests[i] != -1 and ds.find(i) == ds.find(quests[i] - 1):
            return False

    return True


# Example usage
n = int(input())
quests = list(map(int, input().split()))

if is_quest_possible(n, quests):
    print("Yes")
else:
    print("No")