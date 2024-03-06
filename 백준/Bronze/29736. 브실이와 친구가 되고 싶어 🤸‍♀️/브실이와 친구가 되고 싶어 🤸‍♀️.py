import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
k, x = map(int, input().split())
friends = 0
for i in range(a, b+1):
    if k - x <= i <= k + x:
        friends += 1
print(friends) if friends > 0 else print("IMPOSSIBLE")