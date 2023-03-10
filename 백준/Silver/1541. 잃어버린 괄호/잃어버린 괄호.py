plus = 1
number = 0
result = 0
data = input()

def cal():
    global number, result
    if plus:
        result += number
    else:
        result -= number
    number = 0

for i in range(len(data)):
    if data[i] == '+' or data[i] == '-':
        cal()
        if data[i] == '+' and plus == 1:
            plus = 1
        else:
            plus = 0
    else:
        number *= 10
        number += int(data[i])

cal()
print(result)