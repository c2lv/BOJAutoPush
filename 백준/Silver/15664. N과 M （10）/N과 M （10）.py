import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(a1, a2):
    if len(a1) == m:
        print(*a1)
    else:
        for i in range(len(a2)):
            if i > 0 and a2[i-1] == a2[i]:
                continue
            if len(a1) == 0 or (a1[-1] <= a2[i]): 
                a3 = a1[:]
                a4 = a2[:]
                a3.append(a2[i])
                a4.remove(a2[i])
                solve(a3, a4)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
solve([], a)