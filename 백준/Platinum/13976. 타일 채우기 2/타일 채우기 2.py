def cal_m(a, b):
    temp = [[0, 0], [0, 0]]
    temp[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    temp[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    temp[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    temp[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007
    return temp

def solve(n, m):
    if n == 1:
        return m
    m1 = solve(n // 2, m)
    if n & 1:
        return cal_m(cal_m(m1, m1), m)
    else:
        return cal_m(m1, m1)

matrix = [[4, 1], [-1, 0]]
res =  [[1, 1], [1, 3]]
n = int(input())
if n & 1:
    print(0)
else:
    res = cal_m(res, solve(n // 2, matrix))
    print(res[0][0])