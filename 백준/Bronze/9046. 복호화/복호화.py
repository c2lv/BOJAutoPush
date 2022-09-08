t = int(input())
for _ in range(t):
    alpha = {}
    s = input()
    for c in s:
        if c.isalpha():
            if c not in alpha:
                alpha[c] = 0
            else:
                alpha[c] += 1
    list = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
    # 선행 조건이 없으면 len(list)가 1일 때 IndexError: list index out of range
    # list가 아닌 s를 썼을 때 반례: '    a'
    if len(list) == 1 or list[0][1] != list[1][1]:
        print(list[0][0])
    else:
        print('?')