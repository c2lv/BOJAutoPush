import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [[0] * n for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[0][0] = int(input())
    elif i == 1:
        a = list(map(int, input().split()))
        dp[1][0] += a[0] + dp[0][0]
        dp[1][1] += a[1] + dp[0][0]
    else:
        row = list(map(int, input().split()))
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + row[j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + row[j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + row[j]
print(max(dp[n-1]))