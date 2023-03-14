def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))

prime_num = 0
for number in numbers:
    if is_prime(number):
        prime_num += 1
print(prime_num)