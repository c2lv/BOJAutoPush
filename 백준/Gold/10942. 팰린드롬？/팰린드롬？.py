import sys

input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)] # dp[i][j] : i번째 수부터 j번째 까지 수의 팰린드롬 여부
for i in range(1, n + 1):
    dp[i][i] = 1 # 길이 1은 팰린드롬
for i in range(n, 0, -1): # 오름차순으로 채우면 dp[i + 1][j - 1]가 아직 채워지지 않은 경우가 생김
    for j in range(i + 1, n + 1):
        if j - i == 1: # 길이 2
            dp[i][j] = 1 if (num[i] == num[j]) else 0
        else: # 길이 3 이상
            dp[i][j] = 1 if (num[i] == num[j]) and dp[i + 1][j - 1] else 0

m = int(input())

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])