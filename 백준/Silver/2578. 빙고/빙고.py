import sys

input = lambda: sys.stdin.readline().rstrip()

board = []
bingo = [[0]*5 for _ in range(5)]
call = []
line = 0
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    call.append(list(map(int, input().split())))
for k in range(25):
    for i in range(5):
        for j in range(5):
            if board[i][j] == call[k//5][k%5]:
                bingo[i][j] = 1
                if sum(bingo[i]) == 5:
                    line += 1
                if sum(bingo[x][j] for x in range(5)) == 5:
                    line += 1
                if i == j and sum(bingo[x][x] for x in range(5)) == 5:
                    line += 1
                if i + j == 4 and sum(bingo[x][4-x] for x in range(5)) == 5:
                    line += 1
    if line >= 3:
        print(k+1)
        break