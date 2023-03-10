import sys
# 입력
n = int(sys.stdin.readline())

number = [0] * 10001
for _ in range(n):
    i = int(sys.stdin.readline())
    number[i] += 1

# 출력
for i in range(10001):
    for j in range(number[i]):
        print(i)