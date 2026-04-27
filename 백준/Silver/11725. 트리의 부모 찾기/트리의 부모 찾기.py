from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)] # graph[i] = i번 노드와 연결된 노드들의 리스트
ROOT = 1
parent = [0] * (n + 1) # parent[i] = i번 노드의 부모 노드 번호
visited = [False] * (n + 1) # visited[i] = i번 노드 방문 여부
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# breadth-first search (BFS) to find parent nodes
q = deque([ROOT])
visited[ROOT] = True

while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            q.append(neighbor)

for i in range(2, n + 1):
    print(parent[i])