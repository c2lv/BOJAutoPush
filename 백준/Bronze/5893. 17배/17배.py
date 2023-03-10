n = input()
dec = 0
power = 1
result = []

for i in range(len(n), 0, -1):
    dec += power * int(n[i - 1])
    power *= 2

dec *= 17

while dec // 2 > 0:
    if dec % 2 == 1:
        result.append(1)
    else:
        result.append(0)
    dec //= 2
result.append(dec)

for i in range(len(result), 0, -1):
    print(result[i - 1], end='')