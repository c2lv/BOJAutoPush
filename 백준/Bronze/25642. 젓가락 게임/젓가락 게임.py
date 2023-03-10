import sys
input = sys.stdin.readline

yt, yj = map(int, input().split())
for i in range(3):
    if i % 2 == 0:
        yj += yt
        if yj >= 5:
            print('yt')
            break
    if i % 2 == 1:
        yt += yj
        if yt >= 5:
            print('yj')
            break