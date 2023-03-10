import sys

min_num = 100
total = 0
for _ in range(7):
    n = int(sys.stdin.readline())
    if n % 2 == 1:
        total += n
        if n < min_num:
            min_num = n
if total != 0:
    print(total)
    print(min_num)
else:
    print(-1)