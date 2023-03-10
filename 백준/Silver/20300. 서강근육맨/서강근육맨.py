N = int(input())
data = list(map(int, input().split()))
data.sort()
M = 0
even = 1

if len(data) % 2 == 1:
    even = 2
    M = data[len(data) - 1]

for i in range(len(data) // 2):
    result = data[i] + data[len(data) - i - even]
    if M < result:
        M = data[i] + data[len(data) - i - even]

print(M)

'''
운동 기구가 홀수, 짝수일 때의 for문 각각을 하나로 합치는 과정에서 실수가 있었다.
14줄의 1을 even으로 수정했다.
'''