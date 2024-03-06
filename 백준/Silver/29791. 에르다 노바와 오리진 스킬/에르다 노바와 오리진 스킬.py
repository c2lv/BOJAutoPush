import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(list, cooldown):
    recent_use = -cooldown
    cnt = 0
    for sec in list:
        if sec >= recent_use + cooldown:
            cnt += 1
            recent_use = sec
    return cnt

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
stun = solve(a, 100)
absolute_stun = solve(b, 360)
print(stun, absolute_stun)