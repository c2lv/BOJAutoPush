import sys
input = sys.stdin.readline

while True:
    s = input()
    if s[0] == '#':
        break
    cnt = 0
    target = s[0]
    sentence = s[2:]
    for c in sentence:
        if c.lower() == target:
            cnt += 1
    print(target, cnt)