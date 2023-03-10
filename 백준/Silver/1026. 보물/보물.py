# 입력
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순, B는 내림차순 정렬
A.sort()
B.sort(reverse=True)

C = list(map(lambda a, b: a * b, A, B))

# S의 최솟값
result = sum(C)

print(result)