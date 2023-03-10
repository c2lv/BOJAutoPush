from collections import deque
import sys

dq = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "push_front":
        num = int(command[1])
        dq.appendleft(num)
    if command[0] == "push_back":
        num = int(command[1])
        dq.append(num)
    
    if command[0] == "pop_front":
        if dq:
            num = dq.popleft()
            print(num)
        else:
            print(-1)
    if command[0] == "pop_back":
        if dq:
            num = dq.pop()
            print(num)
        else:
            print(-1)
    if command[0] == "size":
        print(len(dq))
    if command[0] == "empty":
        print(0 if dq else 1)
    if command[0] == "front":
        print(dq[0] if dq else -1)
    if command[0] == "back":
        print(dq[len(dq) - 1] if dq else -1)