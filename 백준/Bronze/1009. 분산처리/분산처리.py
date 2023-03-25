# 거듭 제곱의 일의 자리 규칙
def sol(a, b):
    if a % 10 == 0:
        return 10
    elif a % 10 == 1:
        return 1
    elif a % 10 == 2:
        last_num = [2, 4, 8, 6]
        return last_num[(b - 1) % 4]
    elif a % 10 == 3:
        last_num = [3, 9, 7, 1]
        return last_num[(b - 1) % 4]
    elif a % 10 == 4:
        last_num = [4, 6]
        return last_num[(b - 1) % 2]
    elif a % 10 == 5:
        return 5
    elif a % 10 == 6:
        return 6
    elif a % 10 == 7:
        last_num = [7, 9, 3, 1]
        return last_num[(b - 1) % 4]
    elif a % 10 == 8:
        last_num = [8, 4, 2, 6]
        return last_num[(b - 1) % 4]
    elif a % 10 == 9:
        last_num = [9, 1]
        return last_num[(b - 1) % 2]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(sol(a, b))