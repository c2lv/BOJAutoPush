# 입력
import sys
x = int(sys.stdin.readline())

# 분자(a): 1 12321 123454321 ...
# 분모(b): 121 1234321 12345654321 ...
a = 0
a_mid = 1
a_flag = -1
b = 1
b_mid = 0
b_flag = -1
for _ in range(x):
    if a == 0:
        a = 1
    elif a_flag == -1 and a == 1:
        a_flag = 1
        a_mid += 2
    elif a_flag == -1:
        a -= 1
    elif a_flag == 1 and a < a_mid:
        a += 1
    elif a == a_mid:
        a_flag = -1
        a -= 1
    
    if b_flag == -1 and b == 1:
        b_flag = 1
        b_mid += 2
    elif b_flag == -1:
        b -= 1
    elif b_flag == 1 and b < b_mid:
        b += 1
    elif b == b_mid:
        b_flag = -1
        b -= 1

print(str(a)+'/'+str(b))