import sys
input = lambda: sys.stdin.readline().rstrip()

N_MAX = 10**6
dp = [1, 2, 4] + [0] * (N_MAX - 3)
for i in range(3, N_MAX):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % (10**9 + 9)
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1])