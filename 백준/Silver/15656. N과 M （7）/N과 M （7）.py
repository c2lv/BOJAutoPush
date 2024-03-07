import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(a1, a2):
    if len(a1) == m:
        for a in a1:
            print(a, end=' ')
        print()
    else:
        for a in a2:
            a3 = a1[:]
            a4 = a2[:]
            a3.append(a)
            solve(a3, a4)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
solve([], a)