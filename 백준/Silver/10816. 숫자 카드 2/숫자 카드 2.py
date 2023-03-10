from collections import deque

import sys
input = sys.stdin.readline

# n개의 카드 받고 정수 m개 주어졌을 때 n 리스트에 몇 개 있는지 체크
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

'''
이분탐색 사용 풀이법
'''
from collections import Counter

cnt = Counter(n_list)
n_list.sort()

result = [0] * m

# target은 해당 숫자카드
def binary_search(target):
    start = 0
    end = len(n_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return mid
        elif n_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# 모든 m에 대하여
for i in range(m):
    temp = binary_search(m_list[i])
    if temp == -1:
        continue    
    result[i] = cnt[m_list[i]]

for i in range(m):
    print(result[i], end=' ')

'''
딕셔너리 사용 풀이법
'''
# count = dict()

# for i in n_list:
#     try:
#         count[i] += 1
#     except:
#         count[i] = 1

# for i in m_list:
#     try:
#         print(count[i], end=' ')
#     except:
#         print(0, end=' ')