import sys
input = lambda: sys.stdin.readline().rstrip()

N_MAX = 10**5
MOD = 10**9 + 9
dp = [1, 2, 2, 3, 3, 6] + [0] * (N_MAX - 6)
for i in range(6, N_MAX):
    dp[i] = (dp[i-6] + dp[i-4] + dp[i-2]) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1])