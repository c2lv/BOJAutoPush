t = int(input())
for _ in range(t):
    w1, w2 = input().split()
    print('Distances:', end=' ')
    for i in range(len(w1)):
        if ord(w1[i]) <= ord(w2[i]):
            distance = ord(w2[i]) - ord(w1[i])
        else:
            distance = (ord(w2[i]) + 26) - ord(w1[i])
        print(distance, end=' ')
    print()