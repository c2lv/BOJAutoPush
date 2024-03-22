import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
slash = [1]*(2*n-1)
back_slash = [1]*(2*n-1)
bishop = 0
max_bishop = [0, 0]
def back_tracking(case, now):
    global bishop, max_bishop

    if bishop + n - now // 2 - case <= max_bishop[case]:
        return
    if now >= 2*n-1:
        if max_bishop[case] < bishop:
            max_bishop[case] = bishop
        return

    for i in range(now + 1):
        x = i
        y = now - i
        if x >= n or y >= n:
            continue
        if board[y][x] and slash[y+x] and back_slash[y-x]:
            board[y][x] = slash[y+x] = back_slash[y-x] = 0
            bishop += 1
            back_tracking(case, now + 2)
            board[y][x] = slash[y+x] = back_slash[y-x] = 1
            bishop -= 1
        back_tracking(case, now + 2)

back_tracking(0, 0) # x+y is even
back_tracking(1, 1) # x+y is odd

print(sum(max_bishop))