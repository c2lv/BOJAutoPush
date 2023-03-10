t = int(input())
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
day28 = [2]
for _ in range(t):
    x, y = map(int, input().split())
    if 0 <= x <= 23 and 0 <= y <= 59:
        print('Yes', end=' ')
    else:
        print('No', end=' ')
    if x in day31 and 1 <= y <= 31 \
        or x in day30 and 1 <= y <= 30 \
        or x in day28 and 1 <= y <= 29:
        print('Yes')
    else:
        print('No')