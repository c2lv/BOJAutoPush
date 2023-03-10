A, B = map(int, input().split())

if A > B:
    big = A
    small = B
else: # A < B
    big = B
    small = A

sum = (big + small) * (big - small + 1) // 2
print(sum)