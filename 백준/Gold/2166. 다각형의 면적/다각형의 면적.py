import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())
area = 0
for i in range(n):
    if i == n-1:
        area += x[i]*y[0]
        area -= x[0]*y[i]
    else:
        area += x[i]*y[i+1]
        area -= x[i+1]*y[i]

# def ft_round(number, ndigits):
#     integer_part = int(number * 10**ndigits)
#     decimal_part = number * 10**ndigits - integer_part
#     if decimal_part >= 0.5:
#         integer_part += 1
#     integer_part /= 10**ndigits
#     return integer_part

print(round(abs(area/2), 1))