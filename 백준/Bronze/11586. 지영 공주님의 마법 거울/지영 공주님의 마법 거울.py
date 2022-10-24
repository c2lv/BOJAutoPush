mirror = []
n = int(input())
for _ in range(n):
    mirror.append(input())
state = int(input())
if state == 1:
    for line in mirror:
        print(line)
elif state == 2:
    for line in mirror:
        for i in range(n):
            print(line[- i - 1], end='')
        print()
else:
    for i in range(n):
        print(mirror[- i - 1])