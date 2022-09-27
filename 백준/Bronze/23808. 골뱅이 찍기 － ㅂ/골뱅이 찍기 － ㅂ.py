import sys
input = sys.stdin.readline

def side_at_sign(n, m):
    for _ in range(m):
        print(f"{'@' * n}", end='')
        print(f"{' ' * 3 * n}", end='')
        print(f"{'@' * n}")

def line_at_sign(n, m):
    for _ in range(m):
        print(f"{'@' * 5 * n}")

n = int(input())

side_at_sign(n, 2 * n)
line_at_sign(n, n)
side_at_sign(n, n)
line_at_sign(n, n)