import sys

def A(n, steps=0):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return A(n // 2, steps + 1)
    else:
        return A(n + 1, steps + 1)

n = int(sys.stdin.readline())
print(A(n))