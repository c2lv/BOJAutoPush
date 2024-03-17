import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = input().split()
s = ""
up_n = 0
len_a = len(a)
len_b = len(b)
max_len = len_a if len_a > len_b else len_b
for i in range(max_len):
    if i >= len_a:
        num_a = 0
    else:
        num_a = int(a[-1-i])

    if i >= len_b:
        num_b = 0
    else:
        num_b = int(b[-1-i])
    
    if num_a + num_b + up_n < 10:
        s = str(num_a+num_b+up_n) + s
        up_n = 0
    else:
        s = str(num_a+num_b+up_n-10) + s
        up_n = 1
if up_n:
    s = "1" + s
print(s)