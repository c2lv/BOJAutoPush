n, m, k = map(int, input().split())

if m == k:
    print(n)
elif m > k:
    print(n - m + k)
else:
    print(n - k + m)