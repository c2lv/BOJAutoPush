import sys
input = sys.stdin.readline

ans = 'start'
math_signs = ['+', '-', '*', '/']
sign = ''
while True:
    s = input().rstrip()
    if ans == 'start':
        ans = int(s)
    elif s in math_signs:
        sign = s
    elif s == '=':
        print(ans)
        break
    else: # if s is digit
        if sign == '+':
            ans += int(s) 
        elif sign == '-':
            ans -= int(s) 
        elif sign == '*':
            ans *= int(s) 
        else: # if sign == '//'
            ans //= int(s)