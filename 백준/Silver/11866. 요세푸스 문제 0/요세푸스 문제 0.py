from collections import deque

queue = deque()
n, k = map(int, input().split())
for i in range(n):
    queue.append(i + 1)
print("<", end = '')
while len(queue) > 1:
    queue.rotate(-k + 1)
    temp = queue.popleft()
    print(str(temp) + ", ", end = '')
print(str(queue[0]) + ">")