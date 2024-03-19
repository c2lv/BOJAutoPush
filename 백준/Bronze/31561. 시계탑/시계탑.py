import sys
input = lambda: sys.stdin.readline().rstrip()

m = int(input())
if m <= 30:
    print(m/2)
else:
    print(15+(m-30)*3/2)