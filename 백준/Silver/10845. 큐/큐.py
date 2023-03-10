import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        num = int(cmd[1])
        queue.append(num)
    if cmd[0] == 'pop':
        if len(queue) != 0:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    if cmd[0] == 'size':
        size = len(queue)
        print(size)
    if cmd[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    if cmd[0] == 'front':
        if len(queue) != 0:
            num = queue[0]
            print(num)
        else:
            print(-1)
    if cmd[0] == 'back':
        if len(queue) != 0:
            num = queue[-1]
            print(num)
        else:
            print(-1)