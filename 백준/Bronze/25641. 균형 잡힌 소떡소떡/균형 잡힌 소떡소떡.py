n = int(input())
stst = input()
s = 0
t = 0
for st in stst:
    if st == 's':
        s += 1
    else:
        t += 1
for i in range(len(stst)):
    if s == t:
        print(stst[i:])
        break
    else:
        if stst[i] == 's':
            s -= 1
        else:
            t -= 1