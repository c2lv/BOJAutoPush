import sys
input = lambda: sys.stdin.readline().rstrip()

def back_tracking(z):
    if z == n*n-1:
        return True
    y = z // n
    x = z % n
    if board[y][x] == 0:
        return False
    if x + board[y][x] < n:
        if back_tracking(z+board[y][x]):
            return True
    if y + board[y][x] < n:
        if back_tracking(z+board[y][x]*n):
            return True
    return False

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
if back_tracking(0):
    print("Haru"*2)
else:
    print("Hing")
