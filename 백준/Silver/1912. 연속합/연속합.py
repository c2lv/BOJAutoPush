n = int(input())
a = list(map(int, input().split()))
best = a[0]
current_best = a[0]
for i in range(1, n):
    current_best = max(current_best + a[i], a[i])
    best = max(current_best, best)
print(best)