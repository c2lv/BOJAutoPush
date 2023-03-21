import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp
for i in range(1, n + 1):
    print(basket[i], end=' ')