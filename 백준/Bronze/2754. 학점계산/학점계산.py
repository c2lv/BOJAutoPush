grade = input()
result = .0

if grade[0] == 'A':
    result += 4
elif grade[0] == 'B':
    result += 3
elif grade[0] == 'C':
    result += 2
elif grade[0] == 'D':
    result += 1

if grade[0] == 'F':
    pass
elif grade[1] == '+':
    result += .3
elif grade[1] == '-':
    result -= .3

print(result)