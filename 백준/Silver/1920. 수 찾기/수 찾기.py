import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

def binary_search(x):
    left = 0
    right = n - 1
    while (left <= right):
        mid = (left + right) // 2
        if a[mid] == x:
            print(1)
            return
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
    print(0)
        
a.sort()
for i in b:
    binary_search(i)