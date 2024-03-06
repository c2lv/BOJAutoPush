import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * (n+1)
dp[0] = 0
for i in range(n):
    dp[i+1] = dp[i] + a[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])