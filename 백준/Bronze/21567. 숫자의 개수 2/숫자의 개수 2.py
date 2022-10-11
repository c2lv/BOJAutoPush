a = int(input())
b = int(input())
c = int(input())
cnt = [0 for _ in range(10)]
s = str(a * b * c)
for c in s:
    cnt[int(c)] += 1
for i in cnt:
    print(i)