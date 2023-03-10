import sys

l = int(sys.stdin.readline())
for _ in range(l):
    n, symbol = sys.stdin.readline().split()
    print(symbol * int(n))