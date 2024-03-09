a, b, c = map(int, input().split())

def ft_pow(a, b):
    if b == 1:
        return a
    x = ft_pow(a, b//2)
    if b & 1:
        return x * x * a % c
    else:
        return x * x % c

print(ft_pow(a, b) % c)