t = int(input())
answers = list(map(int, input().split()))
cnt = 0
for answer in answers:
    if answer == t:
       cnt += 1
print(cnt)