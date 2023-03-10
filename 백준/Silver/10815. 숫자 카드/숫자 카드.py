n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(x):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            print("1", end=" ")
            return
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
    print("0", end=" ")

for i in b:
    binary_search(i)