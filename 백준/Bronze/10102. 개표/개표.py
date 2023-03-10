survey = {'A': 0, 'B': 0}
v = int(input())
votes = input()
for vote in votes:
    survey[vote] += 1
if survey['A'] > survey['B']:
    print('A')
elif survey['B'] > survey['A']:
    print('B')
else:
    print('Tie')