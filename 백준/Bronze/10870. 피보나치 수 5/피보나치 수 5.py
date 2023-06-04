def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]  # 초기 피보나치 수열
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])  # Fn = Fn-1 + Fn-2
        return fib[n]

# 입력 받기
n = int(input())

# n번째 피보나치 수 계산 및 출력
result = fibonacci(n)
print(result)
