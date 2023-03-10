t = int(input())
for _ in range(t):
    x = list(map(str, input().split()))
    sum = 0
    for i in range(len(x)):
        if i != 0:
            if x[i] == '@':
                sum *= 3
            elif x[i] == '%':
                sum += 5
            elif x[i] == '#':
                sum -= 7
        else:
            sum += float(x[i])
    print(f'{sum:.2f}')