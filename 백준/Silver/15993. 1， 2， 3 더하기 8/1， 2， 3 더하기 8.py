import sys
input = lambda: sys.stdin.readline().rstrip()

N_MAX = 10**5
dp = [[0, 0] for _ in range(N_MAX)]
dp[0] = [1, 0]
dp[1] = [1, 1]
dp[2] = [2, 2]
for i in range(3, N_MAX):
    dp[i][0] = (dp[i-3][1] + dp[i-2][1] + dp[i-1][1]) % (10**9 + 9)
    dp[i][1] = (dp[i-3][0] + dp[i-2][0] + dp[i-1][0]) % (10**9 + 9)
t = int(input())
for _ in range(t):
    n = int(input())
    print(*dp[n-1])