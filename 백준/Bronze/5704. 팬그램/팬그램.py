d = {}
lowers = 'abcdefghijklmnopqrstuvwxyz '

while True:
    for lower in lowers:
        d[lower] = 0    
    s = input()
    if s == '*':
        break
    for c in s:
        d[c] += 1
    res = 'Y'
    for i in range(len(lowers) - 1):
        if d[lowers[i]] == 0:
            res = 'N'
            break
    print(res)