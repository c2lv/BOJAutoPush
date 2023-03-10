n = int(input())
for _ in range(n):
    s = input()
    sum = 0
    pow = 1
    for i in range(24):
        sum += pow * int(s[-1-i])
        pow *= 2
    print(sum)