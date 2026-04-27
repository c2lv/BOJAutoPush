n, b, c = map(int, input().split())
need = list(map(int, input().split())) + [0, 0]

cost = 0

for i in range(n):
    if b > c:
        if need[i + 1] > need[i + 2]:
            buy = min(need[i], need[i + 1] - need[i + 2])
            cost += buy * (b+c)
            need[i] -= buy
            need[i + 1] -= buy

            buy = min(need[i], need[i + 1], need[i + 2])
            cost += buy * (b+2*c)
            need[i] -= buy
            need[i + 1] -= buy
            need[i + 2] -= buy
        else:
            buy = min(need[i], need[i + 1], need[i + 2])
            cost += buy * (b+2*c)
            need[i] -= buy
            need[i + 1] -= buy
            need[i + 2] -= buy

            buy = min(need[i], need[i + 1])
            cost += buy * (b+c)
            need[i] -= buy
            need[i + 1] -= buy

    cost += need[i] * b
    need[i] = 0

print(cost)