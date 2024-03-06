import sys
input = lambda: sys.stdin.readline().rstrip()

direction = ['N', 'E', 'S', 'W']
i = 0
for _ in range(10):
    t = int(input())
    i += t
print(direction[i % 4])