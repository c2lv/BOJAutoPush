from collections import deque

def bfs(x, y):
    if graph[y][x] == 0:
        return False
    graph[y][x] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    klist = []
    result = 0
    
    for _ in range(K):
        i, j = map(int, input().split())
        graph[j][i] = 1
        klist.append([i, j])
    
    for i, j in klist:
        if bfs(i, j) == True:
            result += 1

    print(result)