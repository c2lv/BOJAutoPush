import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
line = []
for _ in range(n):
    line.append(list(map(int, input().split())))
asc = []
index = [0]*n
max_len = 0
line.sort()
for i in range(n):
    if max_len == 0 or (asc[-1][0] < line[i][0] and asc[-1][1] < line[i][1]):
        index[i] = max_len
        max_len += 1
        asc.append(line[i])
    else:
        left = 0
        right = max_len - 1
        while left < right:
            mid = (left+right)//2
            if asc[mid][0] < line[i][0] and asc[mid][1] < line[i][1]:
                left = mid + 1
            else:
                right = mid
        asc[left] = line[i]
        index[i] = left
print(n - max_len)
l = [line[i][0] for i in range(n)]
for i in range(n):
    if max_len - 1 == index[n-1-i]:
        l.remove(line[n-1-i][0])
        max_len -= 1
        if max_len == 0:
            break
print(*l, end='\n')