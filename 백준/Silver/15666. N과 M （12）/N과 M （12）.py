import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
temp = []

def solve(prev, k):
    if k == m:
        print(*temp)
    else:
        before = 0
        for i in range(n):
            if a[i] != before and prev <= a[i]:
                before = a[i]
                temp.append(a[i])
                solve(a[i], k+1)
                temp.pop()

solve(0, 0)