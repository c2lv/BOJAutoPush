n = int(input())
apply_info = list(input().split())
track_info = input()
cnt = 0
for track in apply_info:
    if track == track_info:
        cnt += 1
print(cnt)