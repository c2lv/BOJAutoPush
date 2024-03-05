n, m = map(int, input().split())
cnt = 0
for _ in range(n):
    s = input()
    agree = 0
    for c in s:
        if c == 'O':
            agree += 1
    if agree > m // 2:
        cnt += 1
print(cnt)