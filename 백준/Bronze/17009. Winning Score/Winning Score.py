list = [0 for _ in range(6)]
for i in range(6):
    list[i] = int(input())
A = list[0] * 3 + list[1] * 2 + list[2]
B = list[3] * 3 + list[4] * 2 + list[5]
if A < B:
    print('B')
elif A > B:
    print('A')
else:
    print('T')