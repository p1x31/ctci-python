def is_quest_possible(n, quests):
    npc_set = set(range(n))
    quest_set = set(quests)

    if npc_set.isdisjoint(quest_set):
        return True
    else:
        return False


# Example usage
n = int(input())
quests = list(map(int, input().split()))

if is_quest_possible(n, quests):
    print("Yes")
else:
    print("No")