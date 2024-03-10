import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, q = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

dp = [[0] * max(n, m) for _ in range(2)]
for _ in range(q):
    row_col, rc, v = map(int, input().split())
    dp[row_col - 1][rc - 1] += v

for i in range(2):
    for j in range(max(n, m)):
        if i == 0 and j < n:
            for x in range(m):
                matrix[j][x] += dp[i][j]
        if i == 1 and j < m:
            for y in range(n):
                matrix[y][j] += dp[i][j]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()