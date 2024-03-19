def star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return [
            "*****",
            "*",
            "* ***",
            "* * *",
            "* * *",
            "*   *",
            "*****"
        ]

    row = []
    row.append('*'*(4*n-3))
    row.append('*')

    r = star(n-1)
    for i in range(len(r)):
        if i == 0:
            row.append('* '+r[i]+'**')
        elif i == 1:
            row.append('* '+r[i]+' '*(4*n-7)+'*')
        else:
            row.append('* '+r[i]+' *')

    row.append('*'+' '*(4*n-5)+'*')
    row.append('*'*(4*n-3))
    return row

n = int(input())
for r in star(n):
    print(r)