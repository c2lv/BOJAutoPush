import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()
stack = []
d = {}
for i in range(n):
    d[chr(ord('A')+i)] = int(input())
for c in s:
    if ord('A') <= ord(c) <= ord('Z'):
        stack.append(d[c])
    else:
        b = stack.pop()
        a = stack.pop()
        if c == "+":
            a += b
        elif c == "-":
            a -= b
        elif c == "*":
            a *= b
        else:
            a /= b
        stack.append(a)
print(f"{stack.pop():.2f}")