s = input()
cnt = 0
for c in s:
    if c == ',':
        cnt += 1
print(cnt + 1)