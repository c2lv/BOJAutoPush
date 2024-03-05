n = int(input())
stst = input()
magic = 0
for i in range(n//2):
    if stst[i] != stst[n-1-i]:
        magic += 1
print(magic)