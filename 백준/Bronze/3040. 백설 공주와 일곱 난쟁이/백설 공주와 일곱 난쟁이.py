import sys
input = lambda: sys.stdin.readline().rstrip()

a = []
for _ in range(9):
    a.append(int(input()))

sum_a = sum(a)
for i in range(9):
    for j in range(i+1, 9):
        if sum_a - a[i] - a[j] == 100:
            for k in range(9):
                if k not in [i, j]:
                    print(a[k])
            break