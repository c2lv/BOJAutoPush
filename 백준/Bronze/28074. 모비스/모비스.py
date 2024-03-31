s = input()
target = "MOBIS"
count = [0]*5
for c in s:
    for i in range(5):
        if c == target[i]:
            count[i] = 1
            break
if sum(count) == 5:
    print("YES")
else:
    print("NO")