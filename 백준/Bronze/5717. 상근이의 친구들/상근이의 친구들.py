import sys

while True:
    m, f = map(int, sys.stdin.readline().split())
    if m == f == 0:
        break
    else:
        print(m + f)