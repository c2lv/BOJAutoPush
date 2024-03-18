import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
power = list(map(int, input().split()))
desc = []
len_desc = 0
for i in range(n):
    if not desc or desc[-1] > power[i]:
        desc.append(power[i])
        len_desc += 1
    else:
        left = 0
        right = len_desc
        while left < right:
            mid = (right+left) // 2
            if desc[mid] > power[i]:
                left = mid + 1
            else:
                right = mid
        desc[right] = power[i]
print(n - len(desc))