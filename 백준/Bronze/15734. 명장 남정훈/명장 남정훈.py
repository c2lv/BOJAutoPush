import sys
input = sys.stdin.readline

L, R, A = map(int, input().split())
if L <= R:
    if R - L <= A:
        ans = (R + (A - (R - L)) // 2) * 2
    else:
        ans = (L + A) * 2
else:
    if L - R <= A:
        ans = (L + (A - (L - R)) // 2) * 2
    else:
        ans = (R + A) * 2
print(ans)