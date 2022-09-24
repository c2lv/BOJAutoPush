import sys
input = sys.stdin.readline

L, R, A = map(int, input().split())
if L + A < R:
    print((L + A) * 2)
elif R + A < L:
    print((R + A) * 2)
else:
    print((L + R + A) // 2 * 2)