import sys
input = lambda: sys.stdin.readline().rstrip()


def back_tracking(now, sum, len):
    global count

    if now == n:
        if len > 0 and sum == s:
            count += 1
        return
    else:
        back_tracking(now+1, sum + a[now], len+1)
        back_tracking(now+1, sum, len)

n, s = map(int, input().split())
a = list(map(int, input().split()))
count = 0

back_tracking(0, 0, 0)
print(count)