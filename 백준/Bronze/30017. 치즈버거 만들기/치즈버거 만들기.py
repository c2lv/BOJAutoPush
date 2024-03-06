import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
patty = 100
cheese = 99
while True:
    if a >= patty and b >= cheese:
        print(patty+cheese)
        break
    else:
        patty -= 1
        cheese -= 1