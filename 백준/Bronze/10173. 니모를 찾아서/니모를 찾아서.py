while True:
    s = input()
    if s == "EOI":
        break
    s = s.lower()
    nemo = False
    for i in range(len(s) - 3):
        if s[i] == 'n' and s[i + 1] == 'e' and s[i + 2] == 'm' and s[i + 3] == 'o':
            nemo = True
            break
    if nemo == True:
        print("Found")
    else:
        print("Missing")