import sys

def binary_search(x):
    left = 0
    right = len(b) - 1
    while left <= right:
        mid = (left + right) // 2
        if x <= b[mid]:
            right = mid - 1
        if x > b[mid]:
            left = mid + 1
    return right + 1


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    b.sort()
    result = 0
    for i in a:
        result += binary_search(i)
    print(result)