n = int(input())
for _ in range(n):
    c_max = 0 # 형식적인 선언/초기화
    p = int(input())
    for i in range(p):
        c, name = input().split()
        c = int(c)
        if i == 0 or c_max < c:
            c_max = c
            name_max = name
    print(name_max)