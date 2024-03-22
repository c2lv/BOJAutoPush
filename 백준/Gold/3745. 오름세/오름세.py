import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    try:
        n = int(input())
        p = list(map(int, input().split()))
        asc = []
        max_len = 0
        for i in range(n):
            if max_len == 0 or asc[-1] < p[i]:
                asc.append(p[i])
                max_len += 1
            else:
                left = 0
                right = max_len -1
                while left < right:
                    mid = (left+right)//2
                    if asc[mid] < p[i]:
                        left = mid + 1
                    else:
                        right = mid
                asc[left] = p[i]
        print(max_len)
    except:
        break