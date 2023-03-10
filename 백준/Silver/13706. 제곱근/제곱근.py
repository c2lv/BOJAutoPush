n = int(input())

def binary_search(x):
    left = 1
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == x:
            print(mid)
            return
        elif mid ** 2 < x:
            left = mid + 1
        elif mid ** 2 > x:
            right = mid - 1
        
binary_search(n)