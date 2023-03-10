import sys

t = int(sys.stdin.readline())
stack = []
for _ in range(t):
    cmd = sys.stdin.readline().strip()
    if cmd[:4] == 'push':
        x = int(cmd[5:])
        stack.append(x)
    if cmd == 'pop':
        if len(stack) != 0:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    if cmd == 'size':
        print(len(stack))
    if cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if cmd == 'top':
        if len(stack) != 0:
            x = stack[-1]
            print(x)
        else:
            print(-1)