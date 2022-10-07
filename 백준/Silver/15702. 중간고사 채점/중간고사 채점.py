n, m = map(int, input().split())
dic = {}
best = []

n_score = input().split()

for _ in range(m):
    inf = input().split()
    score = 0

    for j in range(n):
        if inf[j + 1] == 'O':
            score += int(n_score[j])

    dic[inf[0]] = score

for i in dic:
    if dic[i] == max(dic.values()):
        best.append(int(i))

best.sort()

print(best[0], dic[str(best[0])])