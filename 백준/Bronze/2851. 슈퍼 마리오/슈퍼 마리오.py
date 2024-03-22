import sys
input = lambda: sys.stdin.readline().rstrip()

scores = [0]*10
for i in range(10):
    scores[i] = int(input())
answer = 0
for score in scores:
    if abs(answer-100) >= abs(answer+score-100):
        answer += score
    else:
        break
print(answer)