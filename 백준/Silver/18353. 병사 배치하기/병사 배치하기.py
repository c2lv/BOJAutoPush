import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
power = list(map(int, input().split()))
dp = [1]*n
desc_max = 1
for i in range(n):
    for j in range(i):
        if power[j] > power[i]:
            dp[i] = max(dp[j] + 1, dp[i])
    if dp[i] > desc_max:
        desc_max = dp[i]
print(n - desc_max)