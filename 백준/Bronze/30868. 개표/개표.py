t = int(input())
for _ in range(t):
    n = int(input())
    plus = n // 5
    vbar = n % 5
    print("++++ "*plus + "|"*vbar)