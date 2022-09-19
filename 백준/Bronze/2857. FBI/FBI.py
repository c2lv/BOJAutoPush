no_fbi = True
for i in range(5):
    spy = input()
    if "FBI" in spy:
        print(i + 1, end=' ')
        no_fbi = False
if no_fbi:
    print("HE GOT AWAY!")