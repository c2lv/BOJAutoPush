import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [[] for _ in range(2)]
    sticker[0] = list(map(int, input().split()))
    sticker[1] = list(map(int, input().split()))
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    elif n == 2:
        print(max(sticker[1][0]+sticker[0][1], sticker[0][0]+sticker[1][1]))
    else:
        dp = [[] for _ in range(2)]
        dp[0] = [sticker[0][0], sticker[1][0]+sticker[0][1]]+[0]*(n-2)
        dp[1] = [sticker[1][0], sticker[0][0]+sticker[1][1]]+[0]*(n-2)
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
        print(max(dp[0][n-1],dp[1][n-1]))