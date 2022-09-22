import sys
input = sys.stdin.readline

cup = [0, 1, 0, 0]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    temp = cup[x]
    cup[x] = cup[y]
    cup[y] = temp
for i in range(1, 4):
    if cup[i]:
        print(i)
        break