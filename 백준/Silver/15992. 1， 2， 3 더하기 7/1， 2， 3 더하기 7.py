import sys
input = lambda: sys.stdin.readline().rstrip()

N_MAX = 10**3
dp = [[0]*N_MAX for _ in range(N_MAX)]
dp[0] = [1] + [0]*(N_MAX-1)
dp[1] = [1, 1] + [0]*(N_MAX-2)
dp[2] = [1, 2, 1] + [0]*(N_MAX-3)
for i in range(3, N_MAX):
    for j in range(1, N_MAX):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % (10**9 + 9)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n-1][m-1])