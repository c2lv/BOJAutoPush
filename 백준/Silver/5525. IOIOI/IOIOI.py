import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
s = input()

cnt = 0
for i in range(m - 2*n):
    if s[i:2*n+1+i] == "I"+"OI"*n:
        cnt += 1
print(cnt)