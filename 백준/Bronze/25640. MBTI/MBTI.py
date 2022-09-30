import sys
input = sys.stdin.readline

cnt = 0
jinho = input()
n = int(input())
for _ in range(n):
    s = input()
    if jinho == s:
        cnt += 1
print(cnt)