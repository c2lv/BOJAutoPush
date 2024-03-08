import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(y):
    global case

    if y == n:
        case += 1
        return
    
    for x in range(n):
        if column[x] and xy_sum[x+y] and xy_sub[x-y]:
            column[x] = xy_sum[x+y] = xy_sub[x-y] = 0
            solve(y+1)
            column[x] = xy_sum[x+y] = xy_sub[x-y] = 1

n = int(input())
case = 0
column = [1 for _ in range(n)]
xy_sum = [1 for _ in range(2*n-1)]
xy_sub = [1 for _ in range(2*n-1)]
solve(0)
print(case)