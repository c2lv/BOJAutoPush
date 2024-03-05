n = int(input())
a = input().split()
num = {}
for i in range(n):
    if a[i] in num.keys():
        num[a[i]] += 1
    else:
        num[a[i]] = 1
print(max(num.values()))