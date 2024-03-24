import sys
input = lambda: sys.stdin.readline().rstrip()

max = -10**9-1
min = 10**9+1
now = 0

def back_tracking(pl, mi, mu, di, idx):
    global now, min, max

    if idx == len(num):
        if now > max:
            max = now
        if now < min:
            min = now
    else:
        if pl > 0:
            now += num[idx]
            back_tracking(pl-1, mi, mu, di, idx+1)
            now -= num[idx]
        if mi > 0:
            now -= num[idx]
            back_tracking(pl, mi-1, mu, di, idx+1)
            now += num[idx]
        if mu > 0:
            now *= num[idx]
            back_tracking(pl, mi, mu-1, di, idx+1)
            now //= num[idx]
        if di > 0:
            temp = now
            now = abs(now) // num[idx]
            if temp < 0:
                now *= -1
            back_tracking(pl, mi, mu, di-1, idx+1)
            now = temp

n = int(input())
num = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
now = num[0]
back_tracking(pl, mi, mu, di, 1)
print(max,min,sep='\n')