import sys
input = lambda: sys.stdin.readline().rstrip()

def cal_m(a, b):
    if a == []:
        return b
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = (a[i][0]*b[0][j] + a[i][1]*b[1][j]) % 1000000007
    return c

m = [[1, 1], [1, 0]]
n = int(input())
res = []

while n > 1:
    if n & 1:
        res = cal_m(res, m)
    m = cal_m(m, m)
    n >>= 1
res = cal_m(res, m)
print(res[0][1])