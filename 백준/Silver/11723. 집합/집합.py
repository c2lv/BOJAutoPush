import sys
input = lambda: sys.stdin.readline().rstrip()

s = set([])
m = int(input())
for _ in range(m):
    order = input()
    if ' ' in order:
        order, x = order.split()
        x = int(x)
    if order == "add":
        s.add(x)
    if order == "remove":
        if x in s: s.remove(x)
    if order == "check":
        print(1) if x in s else print(0)
    if order == "toggle":
        s.remove(x) if x in s else s.add(x)
    if order == "all":
        s = {i for i in range(1, 21)}
    if order == "empty":
        s.clear()