import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
max_lis = 0
max_lds = 0
lis = [1]*n
lds = [1]*n
answer = 0
car = []
for i in range(n):
    car.append(int(input()))
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if car[j] > car[i]:
            lds[i] = max(lds[j] + 1, lds[i])
        if car[j] < car[i]:
            lis[i] = max(lis[j] + 1, lis[i])
    if lis[i] + lds[i] - 1 > answer:
        answer = lis[i] + lds[i] - 1
print(answer)