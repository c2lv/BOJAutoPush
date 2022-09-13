import sys

input = sys.stdin.readline
n, k, l = map(int, input().split())
allow = 0
list = []
for _ in range(n):
    x1, x2, x3 = map(int, input().split())
    if (x1 >= l and x2 >= l and x3 >= l) and \
    (x1 + x2 + x3 >= k):
        allow += 1
        list.extend([x1, x2, x3])
print(allow)
for i in range(len(list)):
    print(list[i], end=' ')