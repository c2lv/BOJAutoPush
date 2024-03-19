def star(n):
    if n == 1:
        return ['*']
    row = []
    row.append('*'*(4*n-3))
    row.append('*'+' '*(4*n-5)+'*')
    for r in star(n-1):
        row.append('* '+r+' *')
    row.append('*'+' '*(4*n-5)+'*')
    row.append('*'*(4*n-3))
    return row

n = int(input())
for r in star(n):
    print(r)
