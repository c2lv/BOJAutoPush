def pinary_number(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    pn = [0] * 90
    pn[0] = 1
    pn[1] = 1
    for i in range(2, n):
        pn[i] = pn[i-1] + pn[i-2]

    return pn[n-1]

n = int(input())
print(pinary_number(n))