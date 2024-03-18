import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
asc = []
len_asc = 0
for i in range(n):
    if not asc or asc[-1] < a[i]:
        asc.append(a[i])
        len_asc += 1
    else:
        left = 0
        right = len_asc
        while left < right:
            mid = (left+right) // 2
            if asc[mid] < a[i]:
                left = mid + 1
            else:
                right = mid
        asc[right] = a[i]
print(len_asc)