n = input()

lucky = False
for c in n:
    if c == '7':
        if int(n) % 7 == 0:
            print(3)
        else:
            print(2)
        lucky = True
        break
        
if not lucky:
    if int(n) % 7 == 0:
        print(1)
    else:
        print(0)