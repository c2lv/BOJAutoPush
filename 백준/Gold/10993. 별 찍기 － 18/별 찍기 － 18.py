import sys
input = lambda: sys.stdin.readline().rstrip()

def star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return [
            "*****",
            " ***",
            "  *"
        ]

    row = []
    width = -1
    for i in range(1, n+1):
        width += 2**i
    r = star(n-1)
    if n & 1:
        row.append(' '*(width//2)+'*')
        for i in range(1, len(r)*2):
            if i < len(r):
                row.append(' '*(width//2-i)+'*'+' '*(2*i-1)+'*')
            else:
                row.append(' '*(width//2-i)+'*'+' '*(i-len(r))+r[i-len(r)]+' '*(2*(i-len(r)))+'*')
        row.append('*'*width)
    else:
        row.append('*'*width)
        for i in range(len(r)*2-1):
            if i < len(r):
                row.append(' '*(i+1)+'*'+' '*(len(r)-i-1)+r[i]+' '*(2*(len(r)-i-1))+'*')
            else:
                row.append(' '*(i+1)+'*'+' '*(width-4-2*i)+'*')
        row.append(' '*(width//2)+'*')

    return row

n = int(input())
for r in star(n):
    print(r)