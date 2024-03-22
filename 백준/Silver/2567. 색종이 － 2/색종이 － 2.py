import sys
input = lambda: sys.stdin.readline().rstrip()

paper = [[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for i in range(x, x+10):
            paper[j][i] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            if (i == 0 or paper[i-1][j] == 0):
                answer += 1
            if i == 99 or paper[i+1][j] == 0:
                answer += 1
            if j == 0 or paper[i][j-1] == 0:
                answer += 1
            if j == 99 or paper[i][j+1] == 0:
                answer += 1
print(answer)