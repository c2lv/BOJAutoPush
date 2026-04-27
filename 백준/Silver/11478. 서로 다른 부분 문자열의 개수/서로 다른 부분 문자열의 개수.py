s = input()
piece = set()
for i in range(len(s)):
    for j in range(len(s)-i):
        piece.add(s[j:j+i+1])
print(len(piece))
