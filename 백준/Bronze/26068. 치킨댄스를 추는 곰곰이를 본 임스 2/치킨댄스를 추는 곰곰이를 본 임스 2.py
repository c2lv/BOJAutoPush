n = int(input())
cnt = 0
for _ in range(n):
    x = input()
    if int(x[2:]) <= 90:
        cnt += 1
print(cnt)