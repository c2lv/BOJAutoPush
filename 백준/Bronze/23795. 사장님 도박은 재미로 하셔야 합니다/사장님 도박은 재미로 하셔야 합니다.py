total = 0
while True:
    money = int(input())
    if money != -1:
        total += money
    else:
        print(total)
        break