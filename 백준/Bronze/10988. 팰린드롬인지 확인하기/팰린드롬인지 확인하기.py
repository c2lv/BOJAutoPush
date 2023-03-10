s = input()
pal = 1
for i in range(len(s) // 2):
    if s[i] != s[-1-i]:
        pal = 0
print(pal)