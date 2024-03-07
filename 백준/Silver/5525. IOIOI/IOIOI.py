import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
s = input()

i_start = False
diff = 0
cnt = 0

for i in range(m):
    if i_start:
        if s[i-1] != s[i]:
            diff += 1
            if s[i] == 'I' and diff // 2 >= n:
                cnt += 1
        else:
            diff = 0
            if s[i] == 'O':
                i_start = False
    else:
        if s[i] == 'I':
            i_start = True
print(cnt)