import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = []
for i in range(n):
    word = input()
    s.append(word)
    if word == "?":
        q_index = i

m = int(input())
a = []
for _ in range(m):
    a.append(input())

for word in a:
    if (q_index == 0 or s[q_index - 1][-1] == word[0]) \
        and (q_index == n - 1 or s[q_index + 1][0] == word[-1]) \
        and (word not in s):
        print(word)
        break