import sys
input = lambda: sys.stdin.readline().rstrip()

w, h = map(int, input().split())
n = int(input())
shop = []

for _ in range(n):
    shop.append(tuple(map(int, input().split())))
dg = tuple(map(int, input().split()))
result = 0
for s in shop:
    if s[0] == 1:
        if dg[0] == s[0]:
            result += abs(s[1] - dg[1])
        elif dg[0] == 3:
            result += s[1] + dg[1]
        elif dg[0] == 4:
            result += w - s[1] + dg[1]
        else:
            result += h + min(s[1] + dg[1], 2*w - (s[1] + dg[1]))
    elif s[0] == 2:
        if dg[0] == s[0]:
            result += abs(s[1] - dg[1])
        elif dg[0] == 3:
            result += s[1] + h - dg[1]
        elif dg[0] == 4:
            result += w - s[1] + h - dg[1]
        else:
            result += h + min(s[1] + dg[1], 2*w - (s[1] + dg[1]))
    elif s[0] == 3:
        if dg[0] == s[0]:
            result += abs(s[1] - dg[1])
        elif dg[0] == 1:
            result += s[1] + dg[1]
        elif dg[0] == 2:
            result += h - s[1] + dg[1]
        else:
            result += w + min(s[1] + dg[1], 2*h - (s[1] + dg[1]))
    else:
        if dg[0] == s[0]:
            result += abs(s[1] - dg[1])
        elif dg[0] == 1:
            result += s[1] + w - dg[1]
        elif dg[0] == 2:
            result += h - s[1] + w - dg[1]
        else:
            result += w + min(s[1] + dg[1], 2*h - (s[1] + dg[1]))
print(result)