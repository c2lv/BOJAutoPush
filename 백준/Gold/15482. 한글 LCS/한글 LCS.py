import sys
input = lambda: sys.stdin.readline().rstrip()

def get_lcs_len(s1, s2):
    dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs_len = dp[len(s2)][len(s1)]
    return lcs_len

s1 = input()
s2 = input()
print(get_lcs_len(s1, s2))