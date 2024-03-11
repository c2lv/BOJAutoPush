def solve(n):
    dp = [[0] * 10 for _ in range(101)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(10):
            if j > 0:
                dp[i][j - 1] += dp[i - 1][j] % 1000000000
            if j < 9:
                dp[i][j + 1] += dp[i - 1][j] % 1000000000
    res = 0
    for i in range(10):
        res += dp[n][i] % 1000000000
    return res % 1000000000

n = int(input())
print(solve(n))