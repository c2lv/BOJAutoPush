n = int(input())
s = input()

is_digit = False
is_lower = False
is_upper = False
is_special = False
answer = len(s)

for c in s:
    if c in '!@#$%^&*()-+':
        is_special = True
    elif c.isupper():
        is_upper = True
    elif c.islower():
        is_lower = True
    elif c.isdigit():
        is_digit = True
if not is_digit:
    answer += 1
if not is_lower:
    answer += 1
if not is_upper:
    answer += 1
if not is_special:
    answer += 1
if answer < 6:
    answer += 6 - answer
print(answer - n)