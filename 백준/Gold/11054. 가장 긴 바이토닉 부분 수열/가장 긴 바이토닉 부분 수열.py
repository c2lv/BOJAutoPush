import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n, a):
    dp = [[1, 1] for _ in range(n)]
    bitonic_max = 0
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j][1] >= dp[i][1]:
                dp[i][1] = dp[j][1] + 1
            if a[j] > a[i] and max(dp[j][0], dp[j][1]) >= dp[i][0]:
                dp[i][0] = max(dp[j][0], dp[j][1]) + 1
        if bitonic_max < max(dp[i][0], dp[i][1]):
            bitonic_max = max(dp[i][0], dp[i][1])
    return bitonic_max

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))