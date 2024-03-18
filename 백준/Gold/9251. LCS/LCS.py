import sys
input = lambda: sys.stdin.readline().rstrip()

s = []
s.append(input())
s.append(input())

dp = [[0]*(len(s[0])+1) for _ in range(len(s[1])+1)]
for i in range(1, len(s[1])+1):
    for j in range(1, len(s[0])+1):
        if s[0][j-1] == s[1][i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

lcs_len = dp[len(s[1])][len(s[0])]
print(lcs_len)