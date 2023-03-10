list = []
for _ in range(28):
    n = int(input())
    list.append(n)
for i in range(30):
    if i + 1 not in list:
        print(i + 1)