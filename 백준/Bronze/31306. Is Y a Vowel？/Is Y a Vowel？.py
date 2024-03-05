s = input()
cnt1 = 0
cnt2 = 0
for c in s:
    if c in ['a', 'e', 'i', 'o', 'u']:
        cnt1 += 1
        cnt2 += 1
    elif c == 'y':
        cnt2 += 1
print(cnt1, cnt2)