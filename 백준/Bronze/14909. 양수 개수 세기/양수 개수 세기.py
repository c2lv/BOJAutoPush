n = list(map(int, input().split()))
result = 0

for i in n:
    if i > 0:
        result += 1

print(result)