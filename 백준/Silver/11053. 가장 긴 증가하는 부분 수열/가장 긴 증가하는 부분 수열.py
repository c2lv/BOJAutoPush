import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(a):
    max_len = 1
    dp = [1] * len(a)
    for i in range(1, len(a)):
        current_max = 0
        max_idx = -1
        for j in range(i):
            if a[j] < a[i]:
                if dp[j] > current_max:
                    current_max = dp[j]
                    max_idx = j
        if max_idx != -1:
            dp[i] = dp[max_idx] + 1
            max_len = max(dp[i], max_len)

    return max_len

n = int(input())
a = list(map(int, input().split()))
print(solve(a))