import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
asc = []
index = [0]*n
len_asc = 0
for i in range(n):
    if not asc or asc[-1] < a[i]:
        asc.append(a[i])
        len_asc += 1
        index[i] = len_asc
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
        index[i] = right + 1

print(len_asc)
asc = []
i = n - 1
while len_asc > 0:
    if index[i] == len_asc:
        asc.append(a[i])
        len_asc -= 1
    i -= 1
print(*asc[::-1])