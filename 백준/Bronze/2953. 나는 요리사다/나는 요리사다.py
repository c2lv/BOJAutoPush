import sys

score = [0 for _ in range(5)]
winner = 0
winner_score = 0
for i in range(5):
    p = list(map(int, sys.stdin.readline().split()))
    for j in p:
        score[i] += j
    if score[i] > winner_score:
        winner = i + 1
        winner_score = score[i]
print(winner, winner_score)