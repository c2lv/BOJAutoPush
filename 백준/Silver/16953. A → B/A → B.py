from collections import deque
a, b = map(int, input().split())
cal_min = 0
answer = -1
q = deque([b])
while q:
    x = q.popleft()

    # x > a
    if x % 2 == 0:
        q.append(x // 2)
    if x % 10 == 1:
        q.append(x // 10)
    
    if x == a:
        answer = cal_min + 1
        break
    if x < a:
        break
    cal_min += 1

print(answer)