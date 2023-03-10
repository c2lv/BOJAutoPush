computer = int(input())
m = int(input())
graph = [[] for _ in range(101)]
cnt = -1

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * 101

dfs(graph, 1, visited)

print(cnt)