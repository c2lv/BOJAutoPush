# (x - k) * n >= x를 만족하는 x의 최솟값
# x * n - k * n >= x
# x * n - x >= k * n
# x * (n - 1) >= k * n
# x >= k * n / (n - 1)
k, n = map(int, input().split())
if n == 1:
    print(-1)
else:
    x = (k * n) // (n - 1)
    if (k * n) % (n - 1) != 0:
        x += 1
    print(x)