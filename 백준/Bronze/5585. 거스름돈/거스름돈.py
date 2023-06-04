# 물건의 가격 입력 받기
price = int(input())

# 지불액과 잔돈 계산
payment = 1000
change = payment - price

# 잔돈의 종류와 개수를 저장하는 리스트
coins = [500, 100, 50, 10, 5, 1]
coin_count = 0  # 잔돈의 개수 초기화

# 잔돈의 개수 계산
for coin in coins:
    count = change // coin  # 현재 동전으로 거슬러 줄 수 있는 개수 계산
    change -= count * coin  # 거슬러 준 돈만큼 잔돈에서 차감
    coin_count += count  # 잔돈의 개수에 더하기

# 잔돈 개수 출력
print(coin_count)
