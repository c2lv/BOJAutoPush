s, d, i, l, n = map(int, input().split())
if s+d+i+l < 4*n:
    print(4*n - (s+d+i+l))
else:
    print(0)