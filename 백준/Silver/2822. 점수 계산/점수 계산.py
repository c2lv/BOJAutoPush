scores = []
total = 0
list = []
for i in range(8):
    score = int(input())
    scores.append([i + 1, score])
scores.sort(key=lambda x:x[1], reverse=True)
for i in range(5):
    list.append(scores[i][0])
    total += scores[i][1]
list.sort()
print(total)
for i in range(5):
    print(list[i], end=' ')