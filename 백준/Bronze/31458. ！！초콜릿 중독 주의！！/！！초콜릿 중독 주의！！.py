import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    s = input()
    left = 0
    right = 0
    num = None
    for c in s:
        if not num:
            if c == "!":
                left += 1
            else:
                num = c
        else:
            right += 1
    if num == "0" and right == 0:
        num = 0
    else:
        num = 1
    if left & 1:
        if num == 1:
            num = 0
        else:
            num = 1
    print(num)