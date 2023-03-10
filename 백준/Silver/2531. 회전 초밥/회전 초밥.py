# 입력
import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = list(int(input().rstrip()) for _ in range(n))

# 선언
left = 0 # 먹기 시작하는 인덱스
right = 0 # 먹는 것이 끝나는 인덱스
dict = defaultdict(int)
result = 0 # 먹을 수 있는 최대 가짓수
dict[c] += 1 # 보너스 먹어야 됨

# 먹기
while (right < k):
    dict[arr[right]] += 1
    right += 1

for _ in range(n):
    # 지금까지 최대와 현재 최대 가짓수 비교
    result = max(result, len(dict))
    # 첫 번째 꺼 뱉고 뒤에 꺼 먹어!
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0: # 해당 인덱스 요소 값이 0이면 삭제
        del dict[arr[left]]
    dict[arr[right]] += 1
    left += 1
    right += 1
    if left == n:
        left = 0
    if right == n:
        right = 0

print(result)