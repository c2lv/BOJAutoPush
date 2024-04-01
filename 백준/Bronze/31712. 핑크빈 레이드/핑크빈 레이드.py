import sys
input = lambda: sys.stdin.readline().rstrip()

c = []
d = []
for i in range(3):
    temp = list(map(int, input().split()))
    c.append(temp[0])
    d.append(temp[1])
h = int(input())
second = 0
while True:
    for i in range(3):
        if second == 0 or second % c[i] == 0:
            h -= d[i]
    if h <= 0:
        print(second)
        break
    second += 1