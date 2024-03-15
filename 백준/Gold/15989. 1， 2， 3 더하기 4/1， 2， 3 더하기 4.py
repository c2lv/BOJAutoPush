N_MAX = 10**4
dp = [[1, 0], [2, 1], [3, 1], [4, 1], [5, 1], [7, 2]] + [[0, 0] for _ in range(N_MAX - 6)]

for i in range(6, N_MAX):
    dp[i][1] = dp[i-6][1] + 1
    dp[i][0] = dp[i-1][0] + dp[i][1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1][0])