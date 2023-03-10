# 입력
N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]

minus = [] # - 부호가 사용된 인덱스
plus = [] # + 부호가 사용된 인덱스
result = 0 # 최솟값
front_plus_back = [] # 각 카드의 앞면과 뒷면의 합

# 부호의 개수를 고려하지 않고 최솟값을 만든다
for i, card in enumerate(cards):
    if abs(card[0]) < abs(card[1]): # 뒷면의 절댓값이 더 크다면
        if card[1] < 0: # 뒷면이 음수라면
            plus.append(i) # 더해준다
        else: # 뒷면이 0 또는 양수라면
            minus.append(i) # 빼준다
        result -= abs(card[1])
    else: # 앞면의 절댓값이 더 크다면
        if card[0] < 0: # 앞면이 음수라면
            plus.append(i) # 더해준다
        else: # 앞면이 0 또는 양수라면
            minus.append(i)  # 빼준다
        result -= abs(card[0])

# 사용된 더하기, 빼기 개수가 다르다면 부족한 만큼의 카드를 더 많이 사용된 부호 카드 리스트 중에서 뒤집어 기존과 반대 부호로 사용한다
if len(minus) < len(plus):
    for i in plus:
        front_plus_back.append(abs(cards[i][0] + cards[i][1]))
elif len(plus) < len(minus):
    for i in minus:
        front_plus_back.append(abs(cards[i][0] + cards[i][1]))

# 각 카드의 앞면과 뒷면을 더했을 때의 절댓값이 낮은 카드부터 뒤집는다. 카드를 뒤집어 사용하게 되면 최솟값이 증가하게 되므로 front_plus_back을 오름차순 정렬 후 필요한 만큼 앞 인덱스 원소부터 더하고 그 합을 result에 더해주면 최솟값을 구할 수 있다.
front_plus_back.sort()
for i in range(0, abs(len(plus) - len(minus)) // 2):
    result += front_plus_back[i]

print(result)