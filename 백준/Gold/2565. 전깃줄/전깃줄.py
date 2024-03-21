import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
line = []
dp = [1]*n
max_len = 1
for _ in range(n):
    line.append(list(map(int, input().split())))
line.sort()
for i in range(n):
    for j in range(i):
        if dp[j] >= dp[i] and line[j][0] < line[i][0] and line[j][1] < line[i][1]:
            dp[i] = dp[j] + 1
            max_len = max(max_len, dp[i])
print(n - max_len)