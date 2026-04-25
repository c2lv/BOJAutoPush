while True:
    n = int(input())
    if n == 0:
        break
    ak = list(map(int, input().split()))
    bk = list(map(int, input().split()))
    ak_d = 0
    bk_d = 0
    overtaking = 0
    head = 0
    for i in range(n):
        ak_d += ak[i]
        bk_d += bk[i]
        if ak_d < bk_d:
            if head == 1:
                overtaking += 1
            head = 2
        elif ak_d > bk_d:
            if head == 2:
                overtaking += 1
            head = 1
    print(overtaking)