import sys
input = sys.stdin.readline

d1, d2, d3 = map(int, input().split())

x = (d1 + d2 + d3) / 2
a = x - d3
b = x - d2
c = x - d1

if a > 0 and b > 0 and c > 0:
    print(1)
    print(a, b, c)
else:
    print(-1)