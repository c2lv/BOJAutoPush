import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
book = list(map(int, input().split()))
asc = []
max_len = 0
for i in range(n):
    if max_len == 0 or asc[-1] < book[i]:
        asc.append(book[i])
        max_len += 1
    else:
        left = 0
        right = max_len -1
        while left < right:
            mid = (left+right)//2
            if asc[mid] < book[i]:
                left = mid + 1
            else:
                right = mid
        asc[left] = book[i]
print(n-max_len)