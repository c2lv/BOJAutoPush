n = int(input())

a = [0] * n
for i in range(n):
    a[i] = int(input())
if a[2] - a[1] == a[1] - a[0]:
    d = a[1] - a[0]
    print(a[-1] + d)
else:
    r = a[1] // a[0]
    print(a[-1] * r)