t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    for i in range(0, n, 2):
        result += i + 1
    print(result)