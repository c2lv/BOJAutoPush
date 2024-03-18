import sys
input = lambda: sys.stdin.readline().rstrip()

a = list(map(int, input().split()))
while True:
    for i in range(4):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            print(*a)
            if a == [1, 2, 3, 4, 5]:
                break
    if a == [1, 2, 3, 4, 5]:
        break