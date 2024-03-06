import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x = 0
y = 0
for _ in range(n):
    winner = input()
    if abs(x - y) == 2:
        pass
    else:
        if winner == 'D':
            x += 1
        else:
            y += 1
print(f'{x}:{y}')