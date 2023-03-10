# 입력
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

# 회의 시작 시간 기준 오름차순으로 정렬
times.sort(key=lambda x: x[0])
# 회의 종료 시간 기준 오름차순으로 정렬
times.sort(key=lambda x: x[1])

# 회의의 개수
count = 0

# 마지막 회의가 끝나는 시간
last_end_time = 0

for start_time, end_time in times:
    if last_end_time <= start_time:
        count += 1
        last_end_time = end_time

print(count)