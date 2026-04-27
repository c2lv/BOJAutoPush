import sys
input = sys.stdin.readline
c, n = map(int, input().split())
cost_customer = []
for i in range(n):
    cost, customer = map(int, input().split())
    cost_customer.append((cost, customer))

# dp[i] = i명의 고객을 얻기 위한 최소 비용
dp = [0] + [100000] * c

# unbounded knapsack
for cost, customer in cost_customer:
    i = 1
    while i <= c:
        if i <= customer:
            dp[i] = min(dp[i], cost)
        else:
            dp[i] = min(dp[i], dp[i-customer] + cost)
        i += 1
print(dp[c])