n = int(input())
p = int(input())
min_p = 0
if n < 5:
    min_p = p
elif n < 10:
    min_p = p - 500
elif n < 15:
    min_p = min(p - 500, p - p // 10)
elif n < 20:
    min_p = min(p - 2000, p - p // 10)
else:
    min_p = min(p - 2000, p - p // 100 * 25)
print(min_p) if min_p > 0 else print(0)