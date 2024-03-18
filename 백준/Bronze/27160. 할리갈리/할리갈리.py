import sys
input = lambda: sys.stdin.readline().rstrip()

d = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0,
}
n = int(input())
for _ in range(n):
    s, x = input().split()
    d[s] += int(x)
answer = "NO"
if 5 in d.values():
    answer = "YES"
print(answer)