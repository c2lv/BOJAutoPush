import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    if n == 1:
        return 10
    if n == 2:
        return 55
    dp = [[0] * 11 for _ in range(1001)]
    dp[1][0] = 10
    dp[2] = [11 - i for i in range(11)]
    dp[2][0] = 55

    for i in range(3, n + 1):
        dp[i][1] = dp[i - 1][0]
        dp[i][0] += dp[i][1]
        for j in range(2, 11):
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
            dp[i][0] += dp[i][j] % 10007
        dp[i][0] %= 10007
    return dp[n][0]

n = int(input())
print(solve(n))