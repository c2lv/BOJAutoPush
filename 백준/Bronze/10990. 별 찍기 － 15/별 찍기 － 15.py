def star(n):
    row = ['*']
    if n == 1:
        return row
    row[0] = ' '*(n-1)+'*'
    for i in range(n-1):
        row.append(' '*(n-2-i)+'*'+' '*(2*i+1)+'*')
    return row

n = int(input())
for r in star(n):
    print(r)