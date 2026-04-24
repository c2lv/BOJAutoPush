while True:
    M = input()
    if M == '0':
        break
    # 1
    D = 0
    D_i = 0
    for i in range(0, len(M)):
        if D < int(M[i]):
            D = int(M[i])
            D_i = i
    # 2, 3
    if D % 2 == 1:
        M = M[:D_i] + '0' + M[D_i + 1:]
    else:
        M = M[:D_i] + str((int(M[D_i]) + 4) % 10) + M[D_i + 1:]        
    print(M.lstrip('0'))