import sys
input = lambda: sys.stdin.readline().rstrip()

x, n = map(int, input().split())

now_x = x
for _ in range(n):
    if now_x % 2 == 0:
        now_x = now_x//2 ^ 6
    else:
        now_x = 2*now_x ^ 6
print(now_x)