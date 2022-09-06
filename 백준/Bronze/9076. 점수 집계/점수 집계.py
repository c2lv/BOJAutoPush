t = int(input())
for _ in range(t):
    score = list(map(int, input().split()))
    score.sort()
    if score[-2] - score[1] >= 4:
        print("KIN")
    else:
        print(score[1] + score[2] + score[3])