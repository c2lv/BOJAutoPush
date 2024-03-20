import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(stair, n):
    dp = [0] * n
    dp[0] = stair[0]
    if n == 1:
        return dp[n-1]
    dp[1] = stair[0] + stair[1]
    if n == 2:
        return dp[n-1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + stair[i-1], dp[i-2]) + stair[i]
    return dp[n-1]
    
n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
print(solve(stair, n))