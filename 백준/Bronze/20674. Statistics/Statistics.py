n = int(input())
N_MAX = 10000
before = N_MAX
answer = 0
for _ in range(n):
    p = int(input())
    if p > before:
        answer += p - before
    elif p < before:
        before = p
print(answer)
