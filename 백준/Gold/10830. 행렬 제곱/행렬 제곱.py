import sys
input = lambda: sys.stdin.readline().rstrip()

def matrix_mul(a, b):
    if a == None:
        return b
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= 1000
    return res

def solve(a, b):
    res = None
    while b > 0:
        if b & 1:
            res = matrix_mul(res, a)
        b >>= 1
        a = matrix_mul(a, a)
    return res

n, b = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

res = solve(a, b)
for row in res:
    for element in row:
        if b == 1:
            element %= 1000
        print(element, end=' ')
    print()