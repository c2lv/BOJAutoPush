import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(a):
    max_sum = a[0]
    dp_sum = [0] * len(a)
    for i in range(len(a)):
        current_max = 0
        max_idx = -1
        for j in range(i):
            if a[j] < a[i] and dp_sum[j] > current_max:
                current_max = dp_sum[j]
                max_idx = j
        if max_idx != -1:
            dp_sum[i] = dp_sum[max_idx] + a[i]
            max_sum = max(dp_sum[i], max_sum)
        else:
            dp_sum[i] = a[i]
    return max_sum

n = int(input())
a = list(map(int, input().split()))
print(solve(a))