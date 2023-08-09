n = int(input())
quests = list(map(int, input().split()))

visited = set()

def is_quest_passable(start_npc):
    visited.clear()
    npc = start_npc

    while npc != -1:
        if npc in visited:
            return False
        visited.add(npc)
        npc = quests[npc - 1]

    return True

def check_all_quests():
    for i in range(1, n + 1):
        if not is_quest_passable(i):
            return False
    return True

if check_all_quests():
    print("Yes")
else:
    print("No")