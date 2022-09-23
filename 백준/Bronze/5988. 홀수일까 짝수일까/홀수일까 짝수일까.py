import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    if k % 2 == 1:
        print('odd')
    else:
        print('even')