from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    queue.append(i + 1)
while queue:
    discard = queue.popleft()
    print(discard, end=' ')
    if queue:
        upsidedown = queue.popleft()
        queue.append(upsidedown)