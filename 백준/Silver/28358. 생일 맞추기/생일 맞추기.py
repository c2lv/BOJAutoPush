t = int(input())
for t in range(t):
    a = list(map(int, input().split()))
    y = [f'{m}/{d}' for m in range(1, 13) for d in range(1, 32)]
    impossible_date = ['2/30', '2/31', '4/31', '6/31', '9/31', '11/31']
    for d in impossible_date:
        y.remove(d)
    for i in range(10):
        if a[i] == 1:
            y = [d for d in y if f'{i}' not in d]
    print(len(y))