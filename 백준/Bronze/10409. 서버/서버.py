n, t = map(int, input().split())
works = list(map(int, input().split()))
sum = 0
for i in range(len(works)):
    if sum + works[i] > t:
        print(i)
        break
    if i == len(works) - 1:
        print(i + 1)
    sum += works[i]