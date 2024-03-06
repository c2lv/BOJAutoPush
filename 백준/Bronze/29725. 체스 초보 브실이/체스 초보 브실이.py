import sys
input = lambda: sys.stdin.readline().rstrip()

score = {
    ".": 0,
    "K": 0,
    "k": 0,
    "P": 1,
    "p": -1,
    "N": 3,
    "n": -3,
    "B": 3,
    "b": -3,
    "R": 5,
    "r": -5,
    "Q": 9,
    "q": -9,
}
white_score = 0
for _ in range(8):
    row = input()
    for c in row:
        white_score += score[c]
print(white_score)