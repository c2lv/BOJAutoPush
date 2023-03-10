while True:
    n = int(input())
    if n == -1:
        break
    sum = 1
    str = f"{n} = 1"
    for i in range(2, n):
        if n % i == 0:
            str += f' + {i}'
            sum += i
    if sum == n:
        print(str)
    else:
        print(n, 'is NOT perfect.')