n = int(input())

for _ in range(n):
    str = input()
    l = len(str)
    if 5 < l < 10:
        print('yes')
    else:
        print('no')