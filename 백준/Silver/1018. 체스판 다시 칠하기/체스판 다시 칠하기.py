import sys
input = sys.stdin.readline

board = []
min_cnt = 32
n, m = map(int, input().split())
cnt = 0
for i in range(n):
    board.extend([input().rstrip()])

# 잘라낼 수 있는 모든 8 * 8 타일에서 다시 칠해야 하는 정사각형의 최소 개수 구하기
for i in range(n - 7): # repeat min 1, max 43 times
    for j in range(m - 7): # repeat min 1, max 43 times
        cnt = 0
        for k in range(i, i + 8): # repeat 64 times
            for l in range(j, j + 8):
                if ((k + l) % 2 == 0 and board[k][l] == 'B') \
                or ((k + l) % 2 == 1 and board[k][l] == 'W'):
                    cnt += 1
        cnt = min(cnt, 64 - cnt)
        if cnt < min_cnt:
            min_cnt = cnt
print(min_cnt)