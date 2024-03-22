import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    port = [[0, 0] for _ in range(n)]
    for i in range(n):
        port[i] = [i+1, int(input())]
    asc = []
    max_len = 0
    case = 0
    for i in range(n):
        if max_len == 0 or (asc[-1][0] < port[i][0] and asc[-1][1] < port[i][1]):
            asc.append(port[i])
            max_len += 1
        else:
            left = 0
            right = max_len -1
            while left < right:
                mid = (left+right)//2
                if (asc[mid][0] < port[i][0] and asc[mid][1] < port[i][1]):
                    left = mid + 1
                else:
                    right = mid
            asc[left] = port[i]
    print(max_len)