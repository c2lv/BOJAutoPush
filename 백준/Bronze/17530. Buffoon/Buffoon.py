import sys

n = int(sys.stdin.readline())
elected = 1
for i in range(n):
    if i == 0:
        yc_votes = int(sys.stdin.readline())
    else:
        votes = int(sys.stdin.readline())
        if yc_votes < votes:
            elected = 0
            break
if elected:
    print('S')
else:
    print('N')