n = int(input())
min = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b and b < min:
        min = b
print(min) if min < 1001 else print(-1)