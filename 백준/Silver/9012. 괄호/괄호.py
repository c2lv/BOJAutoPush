t = int(input())
for _ in range(t):
    str = input()
    open = 0
    is_valid = 1
    for i in str:
        if i == '(':
            open += 1
        elif open == 0:
            is_valid = 0
            break
        else:
            open -= 1
    if is_valid and open == 0:
        print('YES')
    else:
        print('NO')