import sys
input = lambda: sys.stdin.readline().rstrip()

def back_tracking(now):
    global sudoku, row_rule, col_rule, square_rule

    x = now % 9
    y = now // 9

    if now == 9*9:
        for row in sudoku:
            print(*row,sep='')
        exit()
    elif sudoku[y][x] != 0:
        back_tracking(now + 1)
    else:
        for i in range(9):
            if (row_rule[y][i] \
            and col_rule[x][i] \
            and square_rule[y//3*3+x//3][i]):
                sudoku[y][x] = i+1
                row_rule[y][i] = False
                col_rule[x][i] = False
                square_rule[y//3*3+x//3][i] = False
                back_tracking(now + 1)
                sudoku[y][x] = 0
                row_rule[y][i] = True
                col_rule[x][i] = True
                square_rule[y//3*3+x//3][i] = True

sudoku = []
row_rule = [[True]*9 for _ in range(9)] # row_rule[i][j]: i행 j+1 삽입가능여부
col_rule = [[True]*9 for _ in range(9)] # col_rule[i][j]: i열 j+1 삽입가능여부
square_rule = [[True]*9 for _ in range(9)] # square_rule[i][j]: i번째 정사각형 j+1 삽입가능여부
for _ in range(9):
    s = input()
    sudoku.append([int(c) for c in s])
for i in range(9*9):
    y = i // 9
    x = i % 9
    if sudoku[y][x] != 0:
        row_rule[y][sudoku[y][x]-1] = False
        col_rule[x][sudoku[y][x]-1] = False
        square_rule[y//3*3+x//3][sudoku[y][x]-1] = False

back_tracking(0)