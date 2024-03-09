a, b, c = map(int, input().split())

res = 1
while b > 0:
    if b & 1:
        res *= a % c
        res %= c
    a *= a
    a %= c
    b >>= 1
print(res % c)