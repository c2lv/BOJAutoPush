# 입력
n = int(input())

# 피보나치 수 재귀호출
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
'''
for i in range(5, 41):
    print(i, fib(i))
'''

# 피보나치 수 동적 프로그래밍
f = [0] * 41
def fibonacci(n):
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
'''
for i in range(5, 41):
    print(i, fibonacci(i))
'''

# 출력
code1 = fibonacci(n)
code2 = n - 2
print(code1, code2)