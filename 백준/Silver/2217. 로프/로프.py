# 입력
N = int(input())
ropes = list(int(input()) for _ in range(N))

# 내림차순 정렬
ropes.sort(reverse=True)

i = 1
result = 0

for rope in ropes:
    if result < rope * i:
        result = rope * i
    i += 1

print(result)