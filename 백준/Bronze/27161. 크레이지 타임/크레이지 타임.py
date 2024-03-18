import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
time = 1
back = False
for _ in range(n):
    s, x = input().split()
    act = "NO"
    if int(x) == time and s == "HOURGLASS":
        pass
    elif int(x) == time:
        act = "YES"
    elif s == "HOURGLASS":
        back = not back
    print(time, act)
    if back:
        if time != 1:
            time -= 1
        else:
            time = 12
    else:
        if time != 12:
            time += 1
        else:
            time = 1