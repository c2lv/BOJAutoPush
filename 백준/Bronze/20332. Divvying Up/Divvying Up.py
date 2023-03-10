n = int(input())
w = list(map(int, input().split()))
total = 0
for i in w:
    total += i
if total % 3 == 0:
    print('yes')
else:
    print('no')