n = int(input())

p = list(map(int, input().split()))
height_max = 0
now_height = 0
for i in range(1, n):
    if p[i] > p[i - 1]:
        now_height += p[i] - p[i - 1]
    else:
        height_max = max(now_height, height_max)
        now_height = 0
height_max = max(now_height, height_max)
print(height_max)