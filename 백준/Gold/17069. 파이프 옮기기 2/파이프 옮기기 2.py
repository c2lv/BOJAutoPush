import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
status = []
for _ in range(n):
    status.append(list(map(int, input().split())))
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1] = [1, 0, 0]
for r in range(n):
    for c in range(2, n):
        if status[r][c] == 1:
            continue
        dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
        if r > 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
            if status[r-1][c] == status[r][c-1] == 0:
                dp[r][c][2] += sum(dp[r-1][c-1])
print(sum(dp[n-1][n-1]))