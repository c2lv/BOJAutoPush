n, k = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(4)]

# 동 내림차순 정렬
nations.sort(key=lambda x: x[3], reverse = True)
# 은 내림차순 정렬
nations.sort(key=lambda x: x[2], reverse = True)
# 금 내림차순 정렬
nations.sort(key=lambda x: x[1], reverse = True)

before_nation = nations[0]
rank = 1

for nation in nations:
    # 이전 국가보다 잘했으면 등수 증가
    if not (nation[1] == before_nation[1] and nation[2] == before_nation[2] and nation[3] == before_nation[3]):
        before_nation = nation
        rank += 1
    # 등수를 알고 싶은 국가면 반복문 탈출
    if nation[0] == k:
        break

print(rank)