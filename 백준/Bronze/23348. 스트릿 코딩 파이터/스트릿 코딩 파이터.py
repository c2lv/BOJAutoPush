a, b, c = map(int, input().split())
n = int(input())
high_score = 0
for _ in range(n):
    score = 0
    for _ in range(3):
        d, e, f = map(int, input().split())
        score += a * d + b * e + c * f
    if score > high_score:
        high_score = score
print(high_score)