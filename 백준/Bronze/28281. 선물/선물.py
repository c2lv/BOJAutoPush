import sys
input = lambda: sys.stdin.readline().rstrip()

n, x = map(int, input().split())
a = list(map(int, input().split()))
price = float('inf')
for i in range(n-1):
    price = min(price, (a[i]+a[i+1])*x)
print(price)