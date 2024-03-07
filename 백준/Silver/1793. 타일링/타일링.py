import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(2, n):
        dp[i+1] = (dp[i] + 2*dp[i-1])
    return dp[n]
while True:
    try:
        n = int(input())
        print(solve(n))
    except:
        break