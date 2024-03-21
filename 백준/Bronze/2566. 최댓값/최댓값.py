import sys
input = lambda: sys.stdin.readline().rstrip()

max = -1
rc = [0, 0]
for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if max < row[j]:
            rc = [i+1, j+1]
            max = row[j]
print(max)
print(*rc)