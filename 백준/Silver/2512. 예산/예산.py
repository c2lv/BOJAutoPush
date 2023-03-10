import sys
input = sys.stdin.readline

# 입력
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

# 상한액 찾기(이분 탐색)
def binary_search(start, end, array):
    if start > end:
        print(end)
        return
    mid = (start + end) // 2
    temp = 0 # 총 지출
    for i in n_list:
        if mid < i:
            temp += mid
        else:
            temp += i
    if temp <= m:
        binary_search(mid + 1, end, array)
    else:
        binary_search(start, mid - 1, array)

binary_search(0, max(n_list), n_list)