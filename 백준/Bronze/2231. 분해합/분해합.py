import sys
input = lambda: sys.stdin.readline().rstrip()

N_MAX = 10**6
n = int(input())
answer = 0
for i in range(1, N_MAX+1):
    m = temp = i
    while temp > 0:
        m += temp % 10
        temp //= 10
    if m == n:
        answer = i
        break
print(answer)