import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    a = res = 1
    while a % n != 0:
        a = (a*10) % n + 1 % n
        res += 1
    print(res)

while True:
    try:
        n = int(input())
    except:
        break
    solve(n)