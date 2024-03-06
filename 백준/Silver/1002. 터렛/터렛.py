import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    if abs(r1 - r2) < d < r1 + r2:
        print(2)
    elif r1 + r2 < d or abs(r1 - r2) > d:
        print(0)
    elif d == 0 and r1 == r2:
        print(-1)
    else:
        print(1)