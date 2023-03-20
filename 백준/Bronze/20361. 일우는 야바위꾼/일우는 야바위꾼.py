import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
cup = [False for _ in range(n + 1)]
cup[x] = True
for _ in range(k):
    a, b = map(int, input().split())
    temp = cup[a]
    cup[a] = cup[b]
    cup[b] = temp
print(cup.index(True))