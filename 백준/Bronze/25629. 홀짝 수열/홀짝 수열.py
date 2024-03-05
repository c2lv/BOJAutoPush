n = int(input())
a = list(map(int, input().split()))
odd = 0
for i in range(n):
    if a[i] % 2 == 1:
        odd += 1
if (n % 2 == 1 and odd == n // 2 + 1) or (n % 2 == 0 and odd == n // 2):
    print(1)
else:
    print(0)