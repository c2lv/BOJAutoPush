win = 0
for _ in range(6):
    char = input()
    if char == 'W':
        win += 1
if 5 <= win:
    print(1)
elif 3 <= win:
    print(2)
elif 1 <= win:
    print(3)
else:
    print(-1)