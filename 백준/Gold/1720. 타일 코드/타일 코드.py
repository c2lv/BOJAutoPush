def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    a[1] = 1
    a[2] = 3
    b[1] = 1
    b[2] = 3
    c[1] = 1
    c[2] = 3
    for i in range(3, n + 1):
        a[i] = a[i - 1] + 2 * a[i - 2]
        if i & 1:
            b[i] = a[i//2]
        else:
            b[i] = a[i//2 + 1]
        c[i] = (a[i] - b[i]) // 2 + b[i]
    return c[n]

n = int(input())
print(solve(n))