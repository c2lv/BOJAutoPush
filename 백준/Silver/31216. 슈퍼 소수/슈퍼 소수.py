import sys
input = lambda: sys.stdin.readline().rstrip()

prime = []
super_prime = []
n = 2
while n <= 318137:
    is_prime = True
    for i in prime:
        if i > n**(1/2):
            break
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(n)
    n += 1
for i in range(3000):
    super_prime.append(prime[prime[i] - 1])

t = int(input())
for _ in range(t):
    n = int(input())
    print(super_prime[n-1])