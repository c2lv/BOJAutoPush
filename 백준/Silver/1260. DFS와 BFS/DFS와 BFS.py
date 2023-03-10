N, M, V = map(int, input().split())
graph = [[] for _ in range(10001)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(M):
    if graph[i]:
        graph[i].sort()

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (N + 1)

dfs(graph, V, visited)

print()

# bfs
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N + 1)

bfs(graph, V, visited)