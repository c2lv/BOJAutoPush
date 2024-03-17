import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []
stack = []
s = []
for _ in range(n):
    a.append(int(input()))
k = 1
while True:
    if a[0] >= k:
        stack.append(k)
        s.append("+")
        k += 1
    elif a[0] == stack[-1]:
        stack.pop()
        a.pop(0)
        s.append("-")
        if not a:
            print(*s, sep='\n')
            break
    else:
        print("NO")
        break