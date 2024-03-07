import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dp = [5] * (n+1)
dp[0] = 0
for i in range(n):
    j = 1
    while i+j*j <= n:
        dp[i+j*j] = min(dp[i+j*j], dp[i] + 1)
        j += 1
print(dp[n])