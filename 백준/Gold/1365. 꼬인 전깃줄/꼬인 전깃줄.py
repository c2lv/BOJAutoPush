import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
port = list(map(int, input().split()))

asc = []
max_len = 0
for i in range(n):
    if max_len == 0 or asc[-1][1] < port[i]:
        asc.append([i+1, port[i]])
        max_len += 1
    else:
        left = 0
        right = max_len - 1
        while left < right:
            mid = (left+right)//2
            if asc[mid][0] < i+1 and asc[mid][1] < port[i]:
                left = mid + 1
            else:
                right = mid
        asc[left] = [i+1, port[i]]
print(n-max_len)