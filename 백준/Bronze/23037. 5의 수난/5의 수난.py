import sys

n = sys.stdin.readline().strip()
result = 0
for i in n:
    result += int(i) ** 5
print(result)