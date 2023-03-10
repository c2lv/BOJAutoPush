L = int(input())
alphabet = list(list(input()))

i = 1
result = 0

for alpha in alphabet:
    result += (ord(alpha) - ord('a') + 1) * 31 ** (i-1)
    i += 1

print(result)