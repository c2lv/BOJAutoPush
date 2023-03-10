import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

def insertion_sort(a, k):
    cnt = 0
    for i in range(n - 1):
        loc = i
        newItem = a[i + 1]

        while 0 <= loc and newItem < a[loc]:
            a[loc + 1] = a[loc]
            loc -= 1
            cnt += 1
            if k == cnt:
                return a[loc + 1]
        
        if loc != i:
            a[loc + 1] = newItem
            cnt += 1
            if k == cnt:
                return a[loc + 1]
    return -1

print(insertion_sort(a, k))