import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(2, n):
        dp[i+1] = (dp[i] + dp[i-1]) % 10007
    return dp[n]

n = int(input())
print(solve(n))