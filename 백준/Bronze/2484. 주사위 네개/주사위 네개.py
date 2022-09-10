n = int(input())
max_reward = 0
for _ in range(n):
    eyes = [0 for _ in range(7)]
    dices = list(map(int, input().split()))
    for dice in dices:
        eyes[dice] += 1
    flag = 0
    high_eyes = 0
    for i in range(len(eyes)):
        if eyes[i] == 4:
            reward = 50000 + i * 5000
            break
        elif eyes[i] == 3:
            reward = 10000 + i * 1000
            break
        elif eyes[i] == 2:
            if flag == 0:
                flag = i
            else:
                reward = 2000 + (flag + i) * 500
                break
        elif eyes[i] == 1:
            if flag != 0:
                reward = 1000 + flag * 100
            else:
                high_eyes = i
        if i == 6:
            if flag != 0:
                reward = 1000 + flag * 100
            else:
                reward = high_eyes * 100
    if reward > max_reward:
        max_reward = reward
print(max_reward)