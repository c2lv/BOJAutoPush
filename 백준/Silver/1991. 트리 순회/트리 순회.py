from collections import deque

n = int(input())
parent = [0] * (n + 1)
left = [0] * (n + 1)
right = [0] * (n + 1)
visited = [False] * (n + 1) # visited[i] = i번째 대문자 알파벳이 방문되었는지 여부
ROOT = 1
for _ in range(n):
    t, u, v = input().split()
    if u != ".":
        left[int(ord(t) - ord('A') + 1)] = int(ord(u) - ord('A') + 1)
        parent[int(ord(u) - ord('A') + 1)] = int(ord(t) - ord('A') + 1)
    if v != ".":
        right[int(ord(t) - ord('A') + 1)] = int(ord(v) - ord('A') + 1)
        parent[int(ord(v) - ord('A') + 1)] = int(ord(t) - ord('A') + 1)

# 전위 순회
q = deque([ROOT])
while q:
    x = q.popleft()
    visited[x] = True
    print(chr(ord('A') + x - 1), end='')
    if right[x] and not visited[right[x]]:
        q.appendleft(right[x])
    if left[x] and not visited[left[x]]:
        q.appendleft(left[x])
print()
# 중위 순회
visited = [False] * (n + 1)
q = deque([ROOT])
while q:
    x = q.popleft()
    if left[x] and not visited[left[x]]:
        q.appendleft(left[x])
    else:
        if not visited[x]:
            visited[x] = True
            print(chr(ord('A') + x - 1), end='')
        if right[x] and not visited[right[x]]:
            q.appendleft(right[x])
        elif parent[x]:
            q.appendleft(parent[x])
print()
# 후위 순회
visited = [False] * (n + 1)
q = deque([ROOT])
while q:
    x = q.popleft()
    if left[x] and not visited[left[x]]:
        q.appendleft(left[x])
    elif right[x] and not visited[right[x]]:
        q.appendleft(right[x])
    else:
        if not visited[x]:
            visited[x] = True
            print(chr(ord('A') + x - 1), end='')
        if parent[x]:
            q.appendleft(parent[x])
print()