from collections import deque

queue = deque()
n = int(input())
for i in range(n):
    queue.append(i + 1)
while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
print(queue[0])