import sys
input = lambda: sys.stdin.readline().rstrip()

def cal_m(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = (a[i][0]*b[0][j] + a[i][1]*b[1][j]) % 1000000007
    return c

def fibo(n, m):
    if n < 2:
        return m
    l = cal_m(m, m)
    if n & 1:
        return cal_m(fibo(n//2, l), m)
    else:
        return fibo(n//2, l)

n = int(input())
print(fibo(n, [[1, 1], [1, 0]])[0][1])