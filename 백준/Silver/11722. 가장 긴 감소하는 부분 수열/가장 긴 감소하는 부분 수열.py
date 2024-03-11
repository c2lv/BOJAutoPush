def solve(a):
    min_len = 1
    dp = [1] * len(a)
    for i in range(1, len(a)):
        current_min = 0
        min_idx = -1
        for j in range(i):
            if a[j] > a[i]:
                if dp[j] > current_min:
                    current_min = dp[j]
                    min_idx = j
        if min_idx != -1:
            dp[i] = dp[min_idx] + 1
            min_len = max(dp[i], min_len)
    return min_len

n = int(input())
a = list(map(int, input().split()))
print(solve(a))