import sys
input = lambda: sys.stdin.readline().rstrip()

infix = input()
stack = []

for c in infix:
    if c == '(':
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif c in "+-*/":
        if c in "+-":
            while stack and stack[-1] in "+-*/":
                print(stack.pop(), end='')
        else:
            while stack and stack[-1] in "*/":
                print(stack.pop(), end='')
        stack.append(c)
    else:
        print(c, end='')

while stack:
    print(stack.pop(), end='')