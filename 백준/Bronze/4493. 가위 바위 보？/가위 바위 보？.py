import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p1_win = 0
    p2_win = 0
    for _ in range(n):
        p1, p2 = map(str, input().split())
        if (p1 == 'R' and p2 == 'S') \
        or (p1 == 'S' and p2 == 'P') \
        or (p1 == 'P' and p2 == 'R'):
            p1_win += 1
        elif (p1 == 'R' and p2 == 'P') \
        or (p1 == 'S' and p2 == 'R') \
        or (p1 == 'P' and p2 == 'S'):
            p2_win += 1
    if p1_win > p2_win:
        print('Player 1')
    elif p1_win < p2_win:
        print('Player 2')
    else:
        print('TIE')