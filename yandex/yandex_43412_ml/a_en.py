# Read input
n = int(input())
quests = list(map(int, input().split()))

# Initialize a set to store visited NPCs
visited = set()

# Traverse the quests
for i in range(n):
    npc = i
    visited.clear()

    # Follow the quests until a reward or a loop is encountered
    while npc != -1:
        # If the current NPC has already been visited, it's a loop
        if npc in visited:
            print("No")
            exit(0)

        # Mark the current NPC as visited
        visited.add(npc)
        
        # Move to the next NPC according to the quest
        npc = quests[npc]

# All quests are passable if no loop is encountered
print("Yes")