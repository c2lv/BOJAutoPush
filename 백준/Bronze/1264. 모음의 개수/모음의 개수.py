import sys

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
while True:
    s = sys.stdin.readline().strip()
    if s != "#":
        count = 0
        for c in s:
            if c in vowels:
                count += 1
        print(count)
    else:
        break