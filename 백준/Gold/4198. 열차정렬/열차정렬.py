import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = []
for _ in range(n):
    car = int(input())
    dp.append([car, 1, 1])
len_max = 0
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if dp[j][0] > dp[i][0]:
            dp[i][1] = max(dp[j][1] + 1, dp[i][1])
        if dp[j][0] < dp[i][0]:
            dp[i][2] = max(dp[j][2] + 1, dp[i][2])
    if dp[i][1]+dp[i][2]-1 > len_max:
        len_max = dp[i][1]+dp[i][2]-1
print(len_max)