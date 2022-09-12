n = int(input())
max_prize = 0
for _ in range(n):
    eyes = list(map(int, input().split()))
    if eyes[0] == eyes[1] == eyes[2]:
        prize = 10000 + eyes[0] * 1000
    elif eyes[0] == eyes[1] or eyes[0] == eyes[2]:
        prize = 1000 + eyes[0] * 100
    elif eyes[1] == eyes[2]:
        prize = 1000 + eyes[1] * 100
    else:
        prize = max(eyes) * 100
    if prize > max_prize:
        max_prize = prize
print(max_prize)