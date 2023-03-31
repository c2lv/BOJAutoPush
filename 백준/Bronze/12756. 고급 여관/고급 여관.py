a, b = map(int, input().split())
c, d = map(int, input().split())
while True:
    b -= c
    d -= a
    if b <= 0 or d <= 0:
        if b <= 0 and d <= 0:
           print('DRAW')
        elif d <= 0:
           print('PLAYER A')
        elif b <= 0:
           print('PLAYER B')
        break