N_MAX = 1000000
BIG_NUM = 100

dp = [[None] * 2 for _ in range(N_MAX + 1)]

dp[1][0] = BIG_NUM
dp[2][0] = BIG_NUM
dp[4][0] = BIG_NUM
dp[7][0] = BIG_NUM

dp[0][0] = 0
dp[3][0] = 1
dp[3][1] = 3
dp[5][0] = 1
dp[5][1] = 5
dp[6][0] = 2
dp[6][1] = 3

for i in range(8, N_MAX + 1):
    min_num = min(dp[i - 8][0], dp[i - 5][0], dp[i - 3][0])
    if min_num == dp[i - 3][0]:    
        dp[i][0] = dp[i - 3][0] + 1
        dp[i][1] = 3
    elif min_num == dp[i - 5][0]:
        dp[i][0] = dp[i - 5][0] + 1
        dp[i][1] = 5
    else:
        dp[i][0] = dp[i - 8][0] + 1
        dp[i][1] = 8

def get_min_birthnum(n):
    if n in [1, 2, 4, 7]:
        return -1

    ret = ''
    while n > 0:
        ret += str(dp[n][1])
        n -= dp[n][1]
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    print(get_min_birthnum(n))