import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for case in range(t):
    sudoku = []
    row_rule = [[True]*9 for _ in range(9)] # row_rule[i][j]: i행 j+1 삽입가능여부
    col_rule = [[True]*9 for _ in range(9)] # col_rule[i][j]: i열 j+1 삽입가능여부
    square_rule = [[True]*9 for _ in range(9)] # square_rule[i][j]: i번째 정사각형 j+1 삽입가능여부
    solve = True
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    for i in range(9*9):
        y = i // 9
        x = i % 9
        if sudoku[y][x] != 0:
            if (row_rule[y][sudoku[y][x]-1] \
            and col_rule[x][sudoku[y][x]-1] \
            and square_rule[y//3*3+x//3][sudoku[y][x]-1]):
                row_rule[y][sudoku[y][x]-1] = False
                col_rule[x][sudoku[y][x]-1] = False
                square_rule[y//3*3+x//3][sudoku[y][x]-1] = False
            else:
                solve = False
                break
    print(f"Case {case + 1}: {'CORRECT' if solve else 'INCORRECT'}")
    if case != t - 1:
        blank_line = input()