n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    for _ in range(i):
        print('*', end=' ')
    print()