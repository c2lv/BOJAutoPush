x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2) # 두 과녁의 중심 사이의 거리
if d < r1 + r2: # 두 과녁의 반지름 합이 두 과녁의 중심 사이의 거리보다 커야 겹치는 부분이 발생
    print('YES')
else:
    print('NO')