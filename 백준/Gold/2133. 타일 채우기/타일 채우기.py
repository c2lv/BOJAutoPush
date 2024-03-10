def solve(n):
    if n == 0 or n & 1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]
    return dp[n]

n = int(input())
print(solve(n))