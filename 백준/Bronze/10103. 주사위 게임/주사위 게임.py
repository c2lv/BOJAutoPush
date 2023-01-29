n = int(input())
score1 = 100
score2 = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        score1 -= b
    elif a > b:
        score2 -= a
print(score1)
print(score2)