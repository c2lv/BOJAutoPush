n, s = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
left = 0
right = 0
k = 0
while right < n:
    sum += a[right]
    if sum >= s:
        while sum - a[left] >= s:
            sum -= a[left]
            left += 1
        if k == 0:
            k = right - left + 1
        else:
            k = min(k, right - left + 1)
    right += 1
print(k)