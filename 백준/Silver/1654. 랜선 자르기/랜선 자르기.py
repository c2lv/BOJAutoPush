import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = [None for _ in range(k)]
max = 0
for i in range(k):
    a[i] = int(input())
    if a[i] > max:
        max = a[i]

left = 1
right = max + 1
# n-1개를 만들 수 있는 랜선의 최소 길이 찾기
while left < right:
    length = (right + left) // 2
    line = 0
    for i in range(k):
        line += a[i] // length
    if line < n:
        right = length
        # print(line, left, right, length)
    else:
        left = length + 1
        # print(line, left, right, length)
# n-1개를 만들 수 있는 랜선의 최소 길이 - 1 = n개를 만들 수 있는 랜선의 최대 길이
print(left - 1)