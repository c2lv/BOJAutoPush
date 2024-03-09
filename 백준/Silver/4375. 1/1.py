import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    a = "1"
    res = 1
    while True:
        if int(a*res) % n == 0:
            print(res)
            return
        res += 1

while True:
    try:
        n = int(input())
    except:
        break
    solve(n)