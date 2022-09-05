CENSORED = 'CAMBRIDGE'
s = input()
for c in s:
    if c not in CENSORED:
        print(c, end='')