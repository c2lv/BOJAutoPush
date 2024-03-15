n = int(input())
dp = [0, -1, 1, -1, 2, 1, 3, 2, 4] + [0] * (100000 - 8)
for i in range(9, n+1):
    dp[i] = min(dp[i-5], dp[i-2]) + 1
print(dp[n])