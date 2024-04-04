import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
call_time = list(map(int, input().split()))
y = 0
m = 0
for i in range(n):
    y += 10 * (call_time[i] // 30 + 1)
    m += 15 * (call_time[i] // 60 + 1)
if y < m:
    print("Y", y)
elif y > m:
    print("M", m)
else:
    print("Y M", y)