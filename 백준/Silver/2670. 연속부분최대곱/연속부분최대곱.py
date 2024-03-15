import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [0.]*(n+1)
ans = 0.
for i in range(n):
    f = float(input())
    dp[i+1] = max(dp[i]*f, f)
    if ans < dp[i+1]:
        ans = dp[i+1]
print(f"{round(ans * 10000, -1) / 10000:.3f}")