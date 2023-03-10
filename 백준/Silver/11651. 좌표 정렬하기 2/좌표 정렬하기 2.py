# 입력
n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

# 정렬
dots.sort(key=lambda x:(x[1], x[0]))

# 출력
for dot in dots:
    print(dot[0], dot[1])