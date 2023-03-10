n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    x = list(map(int, input().split()))
    A.extend(x)
for _ in range(n):
    x = list(map(int, input().split()))
    B.extend(x)
C = [A[i] + B[i] for i in range(len(A))]
for i in range(len(C)):
    if (i + 1) % m != 0:
        print(C[i], end=' ')
    else:
        print(C[i])