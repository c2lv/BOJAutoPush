n = int(input())
s = input()
cnt = [0] * 10

for c in s:
    for i in range(10):
        if c == "BRONZESILV"[i]:
            cnt[i] += 1
cnt[1] //= 2
cnt[5] //= 2
print(min(cnt))