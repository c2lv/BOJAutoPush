import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(3):
    n = int(input())
    s = 0
    for _ in range(n):
        s += int(input())
    if s == 0:
        print(s)
    elif s < 0:
        print("-")
    else:
        print("+")
