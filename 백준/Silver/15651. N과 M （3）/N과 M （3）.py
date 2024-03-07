import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(a1):
    if len(a1) == m:
        for a in a1:
            print(a, end=' ')
        print()
    else:
        for a in a2:
            a3 = a1[:]
            a3.append(a)
            solve(a3)

n, m = map(int, input().split())
a2 = [i + 1 for i in range(n)]
solve([])