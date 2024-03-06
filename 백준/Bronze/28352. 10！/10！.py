import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    week = 6
    while n > 10:
        week *= n
        n -= 1
    return week
n = int(input())
print(solve(n))