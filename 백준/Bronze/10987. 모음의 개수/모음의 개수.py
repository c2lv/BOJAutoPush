import sys

vowels = ['a', 'e', 'i', 'o', 'u']
total = 0
word = sys.stdin.readline()
for c in word:
    if c in vowels:
        total += 1
print(total)