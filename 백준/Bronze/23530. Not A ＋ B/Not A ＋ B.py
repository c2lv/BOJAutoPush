import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
c = [i+1 for i in range(50)]
for _ in range(t):
    a, b = map(int, input().split())
    print(c[(a+b)%49+1])