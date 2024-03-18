import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x = list(map(int, input().split()))
score = 0
for i in range(n):
    if i == 0 or x[i - 1] + 1 != x[i]:
        score += x[i]
print(score)