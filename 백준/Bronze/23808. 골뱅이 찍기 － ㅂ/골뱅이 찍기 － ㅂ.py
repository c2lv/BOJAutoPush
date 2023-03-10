import sys
input = sys.stdin.readline

n = int(input())

for i in range(5*n):
    if (2*n <= i<3*n) or (4*n <= i):
        print('@'*5*n)
    else:
        print('@'*n + ' '*3*n + '@'*n)