n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(101)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, v, visited, kinship):
    visited[v] = kinship + 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, visited[v])

visited = [False] * 101

dfs(graph, person1, visited, 0)

if visited[person2] - 1 != 0:
    print(visited[person2] - 1)
else:
    print(-1)