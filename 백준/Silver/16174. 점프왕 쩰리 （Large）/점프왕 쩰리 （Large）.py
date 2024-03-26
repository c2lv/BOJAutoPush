import sys
input = lambda: sys.stdin.readline().rstrip()

def back_tracking(z):
    if z == n*n-1:
        return True
    y = z // n
    x = z % n
    if board[y][x] == 0:
        memo[y][x] = False
        return False
    if x + board[y][x] < n and memo[y][x + board[y][x]]:
        if back_tracking(z+board[y][x]):
            return True
    if y + board[y][x] < n and memo[y + board[y][x]][x]:
        if back_tracking(z+board[y][x]*n):
            return True
    memo[y][x] = False
    return False

n = int(input())
board = []
memo = [[True]*n for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))
if back_tracking(0):
    print("Haru"*2)
else:
    print("Hing")