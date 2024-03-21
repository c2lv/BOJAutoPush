import sys
input = lambda: sys.stdin.readline().rstrip()

paper = [[0]*100 for _ in range(100)]
area = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

for p in paper:
    area += sum(p)
print(area)