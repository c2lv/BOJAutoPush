import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(k, l):
    for i in range(2, 10**6 + 1):
        if k % i == 0:
            min_int = min(k//i, i)
            if min_int >= l:
                print("GOOD")
                return
            else:
                print("BAD", min_int)
                return
    print("GOOD")
    return
k, l = map(int, input().split())
solve(k, l)