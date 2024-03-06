import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
table = []
for i in range(n):
    row = list(map(int, input().split()))
    table.append(row)
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + table[i][j] - dp[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] + dp[x1-1][y1-1] - dp[x2][y1-1] - dp[x1-1][y2])