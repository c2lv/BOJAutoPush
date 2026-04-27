n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
block_max = 0
for i in range(n):
    for j in range(n):
        block_max = max(block_max, board[i][j])

def merge_line_left(line):
    global block_max

    nums = [x for x in line if x != 0]
    merged = []
    i = 0

    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            value = nums[i] * 2
            merged.append(value)
            block_max = max(block_max, value)
            i += 2
        else:
            merged.append(nums[i])
            i += 1

    merged.extend([0] * (n - len(merged)))
    return merged


def left(cur_board):
    for i in range(n):
        cur_board[i] = merge_line_left(cur_board[i])


def right(cur_board):
    for i in range(n):
        reversed_row = cur_board[i][::-1]
        merged = merge_line_left(reversed_row)
        cur_board[i] = merged[::-1]


def up(cur_board):
    for j in range(n):
        col = [cur_board[i][j] for i in range(n)]
        merged = merge_line_left(col)
        for i in range(n):
            cur_board[i][j] = merged[i]


def down(cur_board):
    for j in range(n):
        col = [cur_board[i][j] for i in range(n)][::-1]
        merged = merge_line_left(col)
        merged = merged[::-1]
        for i in range(n):
            cur_board[i][j] = merged[i]


def copy_board(src):
    return [row[:] for row in src]


def dfs(depth, cur_board):
    global block_max

    if depth == 0:
        return

    for move in (left, right, up, down):
        next_board = copy_board(cur_board)
        move(next_board)
        dfs(depth - 1, next_board)


dfs(5, board)
print(block_max)