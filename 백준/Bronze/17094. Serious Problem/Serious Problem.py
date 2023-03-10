import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline()
digit_two = 0
for i in range(l):
    if s[i] == '2':
        digit_two += 1
if digit_two > l - digit_two:
    print(2)
elif digit_two < l - digit_two:
    print('e')
else:
    print('yee')