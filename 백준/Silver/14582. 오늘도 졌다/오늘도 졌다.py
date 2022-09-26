import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
b_score = 0
upset = False

for i in range(9):
    a_score += a[i]
    if b_score < a_score:
        upset = True
        break
    b_score += b[i]
if upset:
    print('Yes')
else:
    print('No')