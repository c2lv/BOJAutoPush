import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
ucpc = "UCPC"
i = 0
for c in s:
    if c == ucpc[i]:
        i += 1
        if i == 4:
            break
if i == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")