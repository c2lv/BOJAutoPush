list = [0, 0, 0]
sum = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
for i in range(3):
    list[i] = int(input())
sum += list[0] * 1
sum += list[1] * 3
sum += list[2] * 1
print(f'The 1-3-sum is {sum}')