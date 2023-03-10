survey = {0: 0, 1: 0}
t = int(input())
for _ in range(t):
    i = int(input())
    survey[i] += 1
if survey[0] > survey[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')