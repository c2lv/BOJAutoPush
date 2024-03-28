import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    for _ in range(n):
        print("@"*(n*3)+" "*n+"@"*n)
    for _ in range(3*n):
        print("@"*n+" "*n+"@"*n+" "*n+"@"*n)
    for _ in range(n):
        print("@"*n+" "*n+"@"*(n*3))

n = int(input())
solve(n)