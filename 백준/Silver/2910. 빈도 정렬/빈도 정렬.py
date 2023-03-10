# 입력
n, c = map(int, input().split())
messages = list(map(int, input().split()))

# 먼저 나온 것이 앞에 있도록 정렬
count = []

for message in messages:
    flag = 0
    for i in range(len(count)):
        if message == count[i][0]:
            count[i][1] += 1
            flag = 1
            break
    if flag != 1:
        count.append([message, 1])

# 등장하는 횟수가 많은 것이 앞에 있도록 정렬
count.sort(key=lambda x:-x[1])

# 출력
for i in count:
    for _ in range(i[1]):
        print(i[0], end=' ')