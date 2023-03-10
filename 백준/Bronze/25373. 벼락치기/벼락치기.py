def video(n):
    i = n
    for _ in range(6):
        if n == 1:
            break
        n -= 1
        i += n
    return i

n = int(input())

if n <= 21:
    for i in range(1, 7):
        if n <= video(i):
            print(i)
            break
else:
    n -= 21
    i = n // 7
    j = n % 7
    if j == 0:
        print(i + 6)
    else:
        print(i + 7)
