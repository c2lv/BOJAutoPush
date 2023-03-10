import decimal # 사사오입 방식의 반올림을 사용하기 위해 설정

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
D = decimal.Decimal

t = int(input())
average_grade = .0
total_credit = 0

for _ in range(t):
    subject, credit, grade = input().split()
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

    average_grade += result * int(credit)
    total_credit += int(credit)

average_grade /= total_credit
average_grade = D(str(average_grade)).quantize(D('0.01'))
print(average_grade)