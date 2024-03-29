import sys
input = lambda: sys.stdin.readline().rstrip()

h, w, n, m = map(int, input().split())
print(((h-1)//(n+1)+1)*((w-1)//(m+1)+1))