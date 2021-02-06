V = 10
answer = []
# current position = 0
# count to 1
# cost to 0
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
def tsp(graph, v, currPos, n, count, cost):
    # If lst node is reached and it has
    # a link to the starting node i.e
    # the source then keep the minimum value out of the total cost of traversal
    # and ans Finally return to check for more possible values
    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return
    # backtracking step 
    # Loop to travesrse the adjacency list of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count+1, cost + graph[currPos][i])

            # Mark ith node as unvisited
            v[i] = False
#  n - количество городов

v = [False] * n

v[0] = True

#print(graph)

tsp(graph, v, 0, n ,1, 0)

print(min(answer))