# 입력
n = int(input())
p = list(map(int, input().split()))

# 최솟값 구하기
p.sort()

result = 0
for i in range(n, 0, -1):
    result += p[n - i] * i

# 출력
print(result)