def is_quest_possible(n, quests):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            while quests[i] != -1:
                if visited[quests[i]-1]:
                    return False
                visited[quests[i]-1] = True
                quests[i] = quests[quests[i]-1]
    return True

# Example usage
n = int(input())
quests = list(map(int, input().split()))

if is_quest_possible(n, quests):
    print("Yes")
else:
    print("No")