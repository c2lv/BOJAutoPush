# 입력
N, K = map(int, input().split())
coins = list(int(input()) for _ in range (N))

# 내림차순 정렬
coins.sort(reverse=True)

# 동전 개수
count = 0

for coin in coins:
    count += K // coin
    K = K % coin

print(count)