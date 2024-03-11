def solve(n):
    a1 = 1
    a2 = 5
    b1 = 1
    b2 = 1
    c = 2
    ans = 0
    if n == 1:
        return a1
    if n == 2:
        return a2
    for _ in range(2, n):
        ans = a2 + a1 + b2 + 2 * c
        temp = b1
        b1 = b2
        b2 = a2 + temp
        c += a2
        a1 = a2
        a2 = ans
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))