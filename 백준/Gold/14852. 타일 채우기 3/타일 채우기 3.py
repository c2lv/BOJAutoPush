def solve(n):
    a1 = 1
    a2 = 0
    a3 = 1
    for _ in range(n):
        res = (3*a3 + a2 - a1) % 1000000007
        a1 = a2
        a2 = a3
        a3 = res
    print(res)

n = int(input())
solve(n)