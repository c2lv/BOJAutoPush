t = int(input())
for _ in range(t):
    y = 0
    k = 0
    for _ in range(9):
        n, m = map(int, input().split())
        y += n
        k += m
    if y > k:
        print('Yonsei')
    elif y < k:
        print('Korea')
    else:
        print('Draw')