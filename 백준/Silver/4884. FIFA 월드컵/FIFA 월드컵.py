def cal_y(n):
    p = 1
    while p < n:
        p *= 2
    if p == n:
        return 0
    return p - n

while True:
    g, t, a, d = map(int, input().split())
    if g == -1 and t == -1 and a == -1 and d == -1:
        break
    y = cal_y(g*a+d)
    x = t*(t-1)//2*g + g*a+d+y-1

    print(f"{g}*{a}/{t}+{d}={x}+{y}")