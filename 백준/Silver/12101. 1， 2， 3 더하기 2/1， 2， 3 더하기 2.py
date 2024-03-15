N_MAX = 10**1
K_MAX = 274
dp = [[-1]*K_MAX for _ in range(N_MAX)]
dp[0] = ["1"] + [-1]*(K_MAX - 1)
dp[1] = ["1+1", "2"] + [-1]*(K_MAX - 2)
dp[2] = ["1+1+1", "1+2", "2+1", "3"] + [-1]*(K_MAX - 4)
for i in range(3, N_MAX):
    j = 0
    while True:
        if dp[i-1][j] == -1:
            break
        dp[i][j] = "1+" + dp[i-1][j]
        j += 1
    l = 0
    while True:
        if dp[i-2][l] == -1:
            break
        dp[i][j] = "2+" + dp[i-2][l]
        j += 1
        l += 1
    l = 0
    while True:
        if dp[i-3][l] == -1:
            break
        dp[i][j] = "3+" + dp[i-3][l]
        j += 1
        l += 1

n, m = map(int, input().split())
if m > K_MAX:
    print(-1)
else:
    print(dp[n-1][m-1])