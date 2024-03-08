def solve(y):
    if y == n:
        return 1
    
    case = 0
    for x in range(n):
        if column[x] == xy_sum[x+y] == xy_sub[x-y] == 1:
            column[x] = xy_sum[x+y] = xy_sub[x-y] = 0
            case += solve(y+1)
            column[x] = xy_sum[x+y] = xy_sub[x-y] = 1
    return case

n = int(input())
column = [1 for _ in range(n)]
xy_sum = [1 for _ in range(2*n-1)]
xy_sub = [1 for _ in range(2*n-1)]
print(solve(0))